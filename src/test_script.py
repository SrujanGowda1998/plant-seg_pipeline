from plantseg.tasks.dataprocessing_tasks import remove_false_positives_by_foreground_probability_task
from plantseg.core.image import PlantSegImage
from image_io import import_image, export_image
from postprocessing import remove_bg_objects

segmentation_path = "outputs/results/run_1/ced3Gfp_worm1_01_488_instance_segmentation.tiff"
segmentation_img = import_image(segmentation_path)

foreground_path = "outputs/results/run_1/ced3Gfp_worm1_01_488_rescaled.tiff"
foreground_img = import_image(foreground_path)

output_path = "tests/"

bg_removed = remove_bg_objects(segmentation_img, foreground_img, 0.1)

export_image(bg_removed, output_path, "bg_removed")
