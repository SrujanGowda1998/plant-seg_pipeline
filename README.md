# PlantSeg Pipeline Automation (Snakemake) (!!! Still under development)

This project focuses on automating a 3D cell segmentation pipeline for microscopy images using PlantSeg. The goal is to build a reproducible, scalable, and efficient workflow using Snakemake.

The pipeline integrates:

Image preprocessing

CNN-based boundary prediction

Graph-based segmentation

Postprocessing and filtering

In addition, the project explores methods to improve segmentation quality and reduce unnecessary computation in images with large background regions.

Collaboration

This project is being developed in collaboration with researchers at the European Molecular Biology Laboratory (EMBL).

The collaboration provides:

Real-world microscopy datasets

Domain-specific insights for segmentation challenges

Guidance for improving biological relevance of results

Motivation

Microscopy datasets (e.g., roundworm images) often contain:

Large background regions

Small and densely packed cells

This leads to:

High computational cost during CNN inference

False boundary predictions in background areas

To address this, this project introduces:

Foreground masking using intensity-based thresholding

Boundary map correction

Future optimization via region cropping and patch filtering

Pipeline Overview
Raw Image
   ↓
Gaussian Smoothing
   ↓
Rescaling
   ↓
Boundary Prediction (CNN)
   ↓
Boundary Filtering (custom step)
   ↓
Superpixel Generation
   ↓
Instance Segmentation
   ↓
Postprocessing (background removal)
Key Features
1. Modular Pipeline

The pipeline is structured into independent modules:

preprocessing

segmentation

postprocessing

This makes it easy to modify, extend, and debug individual steps.
