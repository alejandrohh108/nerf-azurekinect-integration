# DS-NeRF MOD Implementation

This repository contains a modified version of the DS-NeRF (Depth Supervised-Neural Radiance Fields) code, incorporating new features to  improve training using additional depth maps (depth in YUV format) and monitoring of metrics during rendering and optimization.

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

- Incorporate a second type of depth input (YUV) alongside the one provided by COLMAP.
- Add control over depth limits in non-NDC scenes.
- Log training and rendering metrics using a custom monitoring class (`TrainingMonitor`).

## Configuration
This repository includes the configuration file `DS-NeRF_CITSEM_conf_llff.txt`, which contains the architecture-specific parameters used to train the model. This file is essential for tuning the model’s settings and controlling key aspects of training.

## Implemented Changes

### New Features:

- **Support for YUV depth**:
  - Loaded, reformatted and normalized using `load_yuv_depth()`.
  - Associated training rays are generated (`yuv_rays_depth`).
  - Random ray sampling is adjusted to include a fixed proportion of YUV rays.

- **`TrainingMonitor` class**:
  - Logs in real-time the loss, PSNR, and time per iteration or rendered image.

- **Custom depth limits (`no_ndc`)**:
  - Computed dynamically from YUV depth images.

### Modified Files:

- `run_NeRF_MOD.py`:  training logic and ray sampling.
- `load_llff_MOD.py`: added functions for YUV data loading.
- `TrainingMonitor.py`: new file defining the monitoring class.

Each new code block is **clearly marked** with comments such as:
```python
# INICIO MODIFICACIÓN - ...
# ...
# FIN MODIFICACIÓN
```

For a detailed explanation of the original DS-NeRF model, refer to the original paper.