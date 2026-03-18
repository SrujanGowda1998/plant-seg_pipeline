from config_loader import load_config
from pathlib import Path
from image_io import import_image, export_image
from preprocessing import gaussian_smoothing, rescale_image, filtered_boundary_map
from segmentation import predict_boundaries, boundary_to_superpixels, superpixels_to_instance_segmentation
from postprocessing import remove_bg_objects

# Paths - Later to be moved to config file

input_path = "data/tiff_files/ced3Gfp_worm1_01_488.tif"
output_path = "outputs/results/"

# # Create individual output folder
# output_root = Path("outputs/results")
# file_name = input_path.stem
# output_path = output_root / file_name
# output_path.mkdir(parents=True, exist_ok=True)

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
export_image(region_of_interest, output_path, "boundary_prediction_filtered")

############################################################################################

#### correct boundary map
# threshold_function='triangle' ### parameter from config file
# from scipy import threshold_function as mythreshold ##or whatever python package has the image thresholding functions (look for otsu, yen, ...)
# threshold_value = mythreshold(smootehned_image[:])  ### needs to run on the npy array of the image
# filtered_image  = smoothened_image > threshold_value  ### maybe also rescaled? not sure what size the boundary_map is
# boundary_map_corrected = boundary_map * filtered_image+


# from skimage.filters import threshold_triangle, threshold_otsu, threshold_yen
# import numpy as np
# from plantseg.core.image import PlantSegImage

# boundary_map_filtered = boundary_map

# image_np = rescaled_image.get_data()
# boundary_np = boundary_map.get_data()

# Threshold
# threshold_value = threshold_triangle(image_np)
# # threshold_value = threshold_otsu(image_np)
# threshold_value = threshold_yen(image_np)

# # Mask
# mask = image_np > threshold_value # Pixel wise comoarision
# mask = mask.astype(np.float32) # Required for multiplication

# boundary_filtered_np = boundary_np * mask
# boundary_map_filtered = boundary_map_filtered.derive_new(boundary_filtered_np, name=f"{boundary_map_filtered.name}_filtered")
# export_image(boundary_map_filtered, output_path, "boundary_prediction_filtered")

############################################################################################

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