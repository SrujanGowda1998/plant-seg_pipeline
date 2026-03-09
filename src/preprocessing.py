from plantseg.tasks.dataprocessing_tasks import gaussian_smoothing_task, image_rescale_to_shape_task
from plantseg.core.image import PlantSegImage


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