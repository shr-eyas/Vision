## Rough Entropy-Based Threshold Selection
This project implements a threshold selection algorithm based on **rough entropy** for image segmentation, as described in the paper *"Threshold Selection Algorithm Using Rough Entropy for Image Segmentation"* by Pal and Pal (2005).

The algorithm is particularly useful for images with noisy backgrounds or overlapping grayscale values between object and background regions. By maximizing the rough entropy, this approach finds an optimal threshold that balances uncertainty between object and background, making it a robust alternative to traditional methods like Otsu's method.

### Features

- **Automatic Threshold Selection**: Calculates an optimal threshold based on rough entropy.
- **Robust to Noise and Overlapping Grayscale Values**: Handles images with challenging segmentation boundaries.
- **Granule-Based Processing**: Uses non-overlapping pixel windows (granules) for robustness to small variations in pixel values.

### How It Works

1. **Granule Creation**: The image is divided into granules, or small, non-overlapping patches of pixels.
2. **Max-Min Grayscale Calculation**: For each granule, the maximum and minimum grayscale values are computed.
3. **Histogram Arrays Initialization**: Arrays are initialized to track potential object and background pixel distributions.
4. **Array Population**: Each granule contributes to object and background arrays based on grayscale values.
5. **Rough Entropy Calculation**: For each threshold, rough entropy is calculated using object and background roughness.
6. **Optimal Threshold Selection**: The threshold that maximizes rough entropy is chosen, offering the most balanced segmentation.


### Requirements
- Python 3.x
- OpenCV (optional, for image reading and processing)
- Numpy

### Usage
This project provides a Python script `rough_entropy_threshold.py` to run the algorithm on an input image.

### Background on Rough Entropy
Rough entropy is a measure of uncertainty or "fuzziness" in the boundary between object and background regions in an image. By maximizing rough entropy, we find a threshold that best captures this uncertainty, making it effective for images with noisy or overlapping grayscale values.

### References
Pal, N. R., & Pal, S. K. (2005). *Threshold Selection Algorithm Using Rough Entropy for Image Segmentation*. [LINK](https://doi.org/10.1016/j.patrec.2005.05.007).

### License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/shr-eyas/Vision/blob/main/LICENSE) file for more details.
