from plantseg.tasks.dataprocessing_tasks import gaussian_smoothing_task, image_rescale_to_shape_task
from plantseg.core.image import PlantSegImage
from skimage.filters import threshold_triangle, threshold_otsu, threshold_yen
import numpy as np


def gaussian_smoothing(image: PlantSegImage, sigma: float) -> PlantSegImage:
    """Apply Gaussian smoothing to a PlantSeg image."""
    
    smoothed_image = gaussian_smoothing_task(
        image=image,
        sigma=sigma
    )

    return smoothed_image


def rescale_image(image: PlantSegImage, factor, order):
    """Applying rescaling to the plantseg image"""
    current_shape = image.get_data().shape
    print("Original shape:", current_shape)

    new_shape = tuple(
        int(round(s * f)) for s, f in zip(current_shape, factor)
    )

    print("New shape:", new_shape)

    rescaled_image = image_rescale_to_shape_task(
        image=image,
        new_shape=new_shape,
        order=order
    )

    return rescaled_image


def filtered_boundary_map(boundary_map, rescaled_image, filter_name):

    filtered_boundary_map = boundary_map

    image_np = rescaled_image.get_data()
    boundary_np = boundary_map.get_data()

    # Threshold
    if filter_name == "triangle":
        threshold_value = threshold_triangle(image_np)
    else:
        threshold_value = threshold_otsu(image_np)

    # Mask
    mask = image_np > threshold_value # Pixel wise comoarision
    mask = mask.astype(np.float32) # Required for multiplication

    filtered_boundary_np = boundary_np * mask
    filtered_boundary_map = filtered_boundary_map.derive_new(filtered_boundary_np, name=f"{filtered_boundary_map.name}_filtered")

    return filtered_boundary_map