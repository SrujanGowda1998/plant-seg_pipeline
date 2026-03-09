from pathlib import Path
from plantseg.tasks.io_tasks import import_image_task, export_image_task
from plantseg.core.image import PlantSegImage


def import_image(input_path: str):

    image = import_image_task(
        input_path=Path(input_path),
        semantic_type="raw",
        stack_layout="ZYX"
    )

    return image


def export_image(image: PlantSegImage, export_directory: Path, stage: str):

    name_pattern = "{file_name}_" + stage

    export_image_task(
        image=image,
        export_directory=export_directory,
        name_pattern=name_pattern,
        export_format="tiff"
    )