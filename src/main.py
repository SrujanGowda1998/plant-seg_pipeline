from config_loader import load_config
from pathlib import Path
from image_io import import_image, export_image
from preprocessing import gaussian_smoothing

# Paths - Later to be moved to config file

input_path = "data/tiff_files/ced3Gfp_worm1_01_488.tif"
output_path = "outputs/results/"

# Load config file

config = load_config(Path("config/config.yaml"))
sigma = config["preprocessing"]["gaussian_sigma"]

# plant-seg pipeline


img = import_image(input_path)
export_image(img, output_path, "imported")

smoothened_image = gaussian_smoothing(img, sigma)
export_image(smoothened_image, output_path, "smoothed")