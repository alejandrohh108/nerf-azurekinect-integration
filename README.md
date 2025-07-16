# NeRF + Azure Kinect Integration: Enhancing NeRF and DS-NeRF with Depth Supervision

This repository contains the final degree project of a Telematics Engineering student, focused on enhancing Neural Radiance Fields (NeRF) and Depth-Supervised NeRF (DS-NeRF) architectures by incorporating depth data from Microsoft Azure Kinect DK. The objective is to improve the geometric accuracy of 3D scene reconstruction using RGB-D information from these ToF depth cameras.

## Project Overview

NeRF and DS-NeRF are neural rendering techniques used for photo-realistic 3D reconstruction from 2D images. This project explores their performance and extends them by integrating real-world depth data captured from Azure Kinect DK, leading to significant improvements in reconstruction quality.

### Key Contributions

- Analysis and adaptation of NeRF and DS-NeRF base models.
- Implementation of custom modifications to incorporate RGB-D input from Azure Kinect.
- Quantitative evaluation showing improvements in geometric fidelity.
- Use of depth supervision in training loss functions.

## Repository Structure

├── CITSEM_dataset # Prepared specifically to evaluate new modifications
├── NeRF_MOD/ # Modified version of original NeRF 
├── DS-NeRF_MOD/ # Modified DS-NeRF with the new data
├── results/ # Visual and numerical output from experiments
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files and folders
├── README.md # Project documentation
└── TFG_Memoria_Alejandro_Hernandez_Herrera.pdf # Project report

Each model modification has its own detailed documentation inside:
- `CITSEM_dataset/README.md`
- `NeRF_MOD/README.md`
- `DS-NeRF_MOD/README.md`
- `results/README.md`

## Dataset

The dataset used to reproduce the results is included in the `/dataset/` folder.

Total size: ~57 MB

If you use this dataset, please reference this repository and cite the author.

##  Setup & Installation

Clone the repo:

``` bash
git clone https://github.com/alejandrohh108/nerf-azurekinect-integration.git
cd nerf-azurekinect-integration
```

Download Dataset:

If the dataset is hosted separately, clone it inside the project folder:

``` bash
git clone https://github.com/alejandrohh108/nerf-azurekinect-dataset.git citsem_DATASET
```
(Skip this step if the dataset is already included in the repository)

Create a virtual environment (recommended):

``` bash
python -m venv venv
source venv/bin/activate  # on Linux/macOS
venv\Scripts\activate     # on Windows
```

Install dependencies:

Each modification of the model has its own dependencies. Navigate to the corresponding folder and install its `requirements.txt`:

For DS-NeRF_MOD:

``` bash
cd DS-NeRF_MOD
pip install -r requirements.txt
cd ..
```

For NeRF_MOD:

``` bash
cd NeRF_MOD
pip install -r requirements.txt
cd ..
```

Tip: You can also create separate virtual environments for each variant if you want to keep them fully isolated.

## Usage

Run training or evaluation from the respective folders:

``` bash
cd DS-NeRF_MOD
python run_nerf_MOD.py --config ../configs/kinect_example.txt
```

## Results

The project showed measurable improvement in reconstruction accuracy, particularly in edge preservation and volumetric consistency.

A **representative sample of results** is included in the `/results/` folder, which contains:

- Short videos comparing RGB rendering across the evaluated models (`/results/RGB_results/`)
- Visual comparisons of scene depth reconstruction (`/results/depth_results/`)
- Training metrics and objective performance data (`/results/training_metrics.txt`)

## Technologies & Libraries

- Python, PyTorch, NumPy, Matplotlib, OpenCV, Open3D

- Azure Kinect SDK (depth camera)

- NeRF / DS-NeRF architectures

## License

This repository is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)**.

You are free to use, modify, and share the content for **non-commercial purposes**, as long as appropriate credit is given.

More details: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

## Project Report

This repository is part of an academic project and provided for educational purposes. 

Created as part of the Final Degree Project at Universidad Politécnica de Madrid (UPM), 2025.

You can read the full final degree project report (Spanish, PDF) here: [TFG_Memoria_Alejandro_Hernandez_Herrera.pdf](./TFG_Memoria_Alejandro_Hernandez_Herrera.pdf)
