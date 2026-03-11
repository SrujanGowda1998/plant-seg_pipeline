from plantseg.tasks.prediction_tasks import unet_prediction_task
from plantseg.tasks.segmentation_tasks import dt_watershed_task, clustering_segmentation_task
from plantseg.core.image import PlantSegImage


def predict_boundaries(image: PlantSegImage, model_name, model_id) -> PlantSegImage:

    predictions = unet_prediction_task(
        image=image,
        model_name=model_name,
        model_id=None
    )
    # unet_prediction_task returns a list of PlantSegImage
    boundary_prediction = predictions[0]

    return boundary_prediction

def boundary_to_superpixels(boundary_prediction: PlantSegImage, threshold, min_size, stacked) -> PlantSegImage:

    superpixels = dt_watershed_task(
        image = boundary_prediction,
        threshold = threshold,
        min_size = min_size,
        stacked = stacked
    )

    return superpixels

def superpixels_to_instance_segmentation(boundary_map: PlantSegImage, superpixels: PlantSegImage, mode: str, beta: float, post_min_size: int) -> PlantSegImage:

    segmentation = clustering_segmentation_task(
        image=boundary_map,
        over_segmentation=superpixels,
        mode=mode,
        beta=beta,
        post_min_size=post_min_size
    )

    return segmentation