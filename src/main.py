from config_loader import load_config
from pathlib import Path
from image_io import import_image, export_image
from preprocessing import gaussian_smoothing, rescale_image
from segmentation import predict_boundaries

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