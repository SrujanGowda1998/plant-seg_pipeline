from plantseg.tasks.dataprocessing_tasks import gaussian_smoothing_task
from plantseg.core.image import PlantSegImage


def gaussian_smoothing(image: PlantSegImage, sigma: float) -> PlantSegImage:
    """Apply Gaussian smoothing to a PlantSeg image."""
    
    smoothed_image = gaussian_smoothing_task(
        image=image,
        sigma=sigma
    )

    return smoothed_image