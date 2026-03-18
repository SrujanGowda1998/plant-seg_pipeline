# PlantSeg Pipeline Automation (Snakemake) @ EMBL, Heidelberg (!!! Still under development)


This project focuses on automating a 3D cell segmentation pipeline for microscopy images using PlantSeg. The goal is to build a reproducible and scalable workflow, with ongoing integration into Snakemake.

# The pipeline includes:
Image preprocessing (smoothing, rescaling)
CNN-based boundary prediction
Superpixel generation and instance segmentation
Postprocessing and filtering

# Collaboration

This project is being developed in collaboration with researchers at the European Molecular Biology Laboratory (EMBL), using real microscopy datasets and practical segmentation challenges.

# Motivation

Microscopy images (e.g., roundworm datasets) often contain large background regions and small cells. This leads to:
- Unnecessary computation during CNN prediction
- False boundary predictions in background
To address this, the pipeline includes custom steps
- Foreground masking using thresholding (Triangle, Otsu, Yen)
- Boundary correction by masking


# Usage

# Author

Srujan Gowda
https://github.com/SrujanGowda1998
