# import tifffile
# import numpy as np
# from src.io_utils import load_tiff
# import os

# tif_path = "data/tiff_files/ced3Gfp_worm1_01_488.tif"
# image, axes = load_tiff(tif_path)

# print("Image shape:", image.shape)
# print("Axes order:", axes)

# z_axis = axes.index("Z")

# # Compute max intensity projection
# mip = np.max(image, axis=z_axis)

# # Save MIP
# os.makedirs("outputs/results", exist_ok=True)
# output_path = "outputs/results/mip_z_projection.tif"
# tifffile.imwrite(output_path, mip)
# print(f"MIP saved to: {output_path}")

print("Hello")