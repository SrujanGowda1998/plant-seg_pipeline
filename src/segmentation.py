from plantseg.tasks.prediction_tasks import unet_prediction_task
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