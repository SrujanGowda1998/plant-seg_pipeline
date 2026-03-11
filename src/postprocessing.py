from plantseg.tasks.dataprocessing_tasks import remove_false_positives_by_foreground_probability_task
from plantseg.core.image import PlantSegImage


def remove_bg_objects(segmentation: PlantSegImage, foreground: PlantSegImage, threshold: float) -> PlantSegImage:

    results = remove_false_positives_by_foreground_probability_task(
        segmentation=segmentation,
        foreground=foreground,
        threshold=threshold
    )

    cleaned_segmentation = results[0]

    return cleaned_segmentation