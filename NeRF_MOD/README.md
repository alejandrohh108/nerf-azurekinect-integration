# NeRF MOD Implementation

This repository contains a modified version of the original NeRF (Neural Radiance Fields) code, extended to incorporate depth maps in YUV format alongside standard RGB rays. The goal is to enrich the 3D reconstruction process with additional depth supervision and improve model training while leveraging the strengths of the original architecture.

## Requirements
- Python 3.10.8+
- Dependencies listed in `requirements.txt`

## Installation
```bash
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
```

## Project Description

The base implementation has been extended to:

- Integrate depth maps extracted from `.yuv` images.
- Combine traditional RGB rays with depth data using `rays_rgb_d`.
- Automatically compute depth limits when NDC is not used.
- Apply an additional supervised loss based on YUV depth.
- Log training and rendering metrics using a custom monitoring class (`TrainingMonitor`).

## Configuration
This repository includes the configuration file `CITSEM_conf_llff.txt`, which contains the architecture-specific parameters used to train the model. This file is essential to adjust the model’s settings and control key aspects of training.

## Implemented Changes

### New Features:

- **Support for YUV depth**:
  - Loaded, reformatted, and normalized using `load_yuv_depth()`.
  - `yuv_images_raw` is expanded and concatenated with RGB rays to form `rays_rgb_d`.
  - Supervised depth loss is calculated using `img2mse()`with masking to ignore pixels without valid depth values and incorporated into the total loss.

- **`TrainingMonitor`class**:
  - Logs loss, PSNR, and time per iteration or rendered image in real time.

- **Custom depth limits (`no_ndc`)** :
  - Dynamically computed from YUV depth images.

### Modified Files:

- `run_NeRF_MOD.py`: logic for ray construction, RGB + YUV data fusion, limit calculation, and loss computation.
- `load_llff_MOD.py`: added functions for loading YUV data.
- `TrainingMonitor.py`: new file defining the monitoring class.

Each new code block is  **clearly marked** with comments such as:
```python
# INICIO MODIFICACIÓN - ...
# ...
# FIN MODIFICACIÓN
```