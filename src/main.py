from config_loader import load_config
from pathlib import Path
from image_io import import_image, export_image
from preprocessing import gaussian_smoothing, rescale_image, filtered_boundary_map
from segmentation import predict_boundaries, boundary_to_superpixels, superpixels_to_instance_segmentation
from postprocessing import remove_bg_objects

# Paths - Later to be moved to config file

input_path = "data/tiff_files/ced3Gfp_worm1_01_488.tif"
output_path = "outputs/results/"

# Load config file

config = load_config(Path("config/config.yaml"))
sigma = config["preprocessing"]["gaussian_sigma"]

# plant-seg pipeline

# Image Import
img = import_image(input_path)
export_image(img, output_path, "imported")

# Gaussian Smoothing
smoothened_image = gaussian_smoothing(img, sigma)
export_image(smoothened_image, output_path, "smoothed")

# Rescaling
rescale_factor = config["preprocessing"]["rescale_factor"]
interpolation_order = config["preprocessing"]["interpolation_order"]

rescaled_image = rescale_image(smoothened_image, factor=tuple(rescale_factor), order=interpolation_order)
export_image(rescaled_image, output_path, "rescaled")

# Predict Boundaries
model_name = config["segmentation"]["model_name"]
model_id = config["segmentation"]["model_id"]

boundary_map = predict_boundaries(rescaled_image, model_name, model_id )
export_image(boundary_map, output_path, "boundary_prediction")

# Filter out only the region of interest from the boundary map
filter_name = config["preprocessing"]["filter_name"]

filtered_boundary_map = filtered_boundary_map(boundary_map, rescaled_image, filter_name)
export_image(filtered_boundary_map, output_path, "boundary_prediction_filtered")

# Boundaries to Superpixels
threshold = config["segmentation"]["threshold"]
min_size = config["segmentation"]["min_size"]
stacked = config["segmentation"]["stacked"]

superpixels = boundary_to_superpixels(filtered_boundary_map, threshold, min_size, stacked)
export_image(superpixels, output_path, "superpixels")

# Superpixels to Instance Segmentation
mode = config["segmentation"]["mode"]
beta = config["segmentation"]["beta"]
post_min_size = config["segmentation"]["post_min_size"]

instance_segmentation = superpixels_to_instance_segmentation(boundary_map, superpixels, mode, beta, post_min_size)
export_image(instance_segmentation, output_path, "instance_segmentation")

# Remove Objects with Low Foreground Probability
foreground_threshold = config["postprocessing"]["foreground_threshold"]

instance_segmentation_bg_removed = remove_bg_objects(instance_segmentation, rescaled_image, foreground_threshold)
export_image(instance_segmentation_bg_removed, output_path, "instance_segmentation_bg_removed")