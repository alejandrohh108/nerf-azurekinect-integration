# Evaluation Dataset

This dataset has been prepared by CITSEM specifically to evaluate and compare different variants of the NeRF model, including those that integrate depth maps from COLMAP and YUV-formatted files.

## Dataset Contents

The dataset folder includes the following elements:

### 1. `depth_align_undistort/`
Contains depth images in .yuv format. These images are used as additional input for training and supervising the models.

### 2. `images/`
Contains the input RGB images corresponding to the scene. These images have been used as input for both COLMAP and NeRF.

### 3. `sparse/`
Output from the COLMAP sparse reconstruction process. It contains camera calibration data and the reconstructed 3D structure:

- `cameras.txt`: Intrinsic camera parameters.
- `images.txt`: Camera poses and feature correspondences.
- `points3D.txt`: Reconstructed 3D point cloud.

### 4. Additional Files

- `database.db`: COLMAP database containing extracted features, matches, and other information.
- `poses_bounds.npy`: File generated using the DS-NeRF script to extract camera poses and scene bounds from COLMAP data.
- `project.ini`: Configuration file accompanying the COLMAP project.

## Dataset Usage

This dataset has been used to:

- Train NeRF variants with and without depth maps.
- Integrate additional depth data in YUV format.
- Compare the accuracy and robustness of 3D reconstructions under different configurations.
