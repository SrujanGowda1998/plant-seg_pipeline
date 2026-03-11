#!/bin/bash

#SBATCH --job-name=plantseg_pipeline
#SBATCH --partition=gpu
#SBATCH --gres=gpu:8
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=02:00:00
#SBATCH --output=logs/plantseg_%j.out
#SBATCH --error=logs/plantseg_%j.err

cd /g/koehler/Srujan/Projects/plant-seg_pipeline

module load Miniforge3

# conda activate /g/koehler/Srujan/conda_envs/plantseg_env
# python src/main.py
/g/koehler/Srujan/conda_envs/plantseg_env/bin/python src/main.py 
