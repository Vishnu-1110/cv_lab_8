# Computer Vision Lab 8 — Image Filtering

This project demonstrates **image filtering using a mean (average) filter** implemented with Python, OpenCV, NumPy, and Matplotlib.

## Objective

To apply a spatial mean filter to a grayscale image and observe the smoothing effect produced by the filter.

## Libraries Used

- Python
- OpenCV
- NumPy
- Matplotlib

## Python Code

The complete program is available in [cv_lab_8.py](cv_lab_8.py).

## How It Works

The program:

1. Reads the input image in grayscale.
2. Creates a **9 × 9 mean filter kernel**.
3. Applies the kernel manually using a sliding-window operation.
4. Produces a smoothed/filtered image.
5. Displays the original and filtered images side by side.
6. Prints the dimensions of the original and filtered images.

### Mean Filter

The mean filter replaces each pixel with the average value of the pixels covered by the kernel. It is commonly used for smoothing an image and reducing small variations.

## How to Run

Install the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

Place the input image in the project folder as:

```text
dove.jpg
```

Run:

```bash
python cv_lab_8.py
```

This version uses a normal local image path. **No Google Colab or Google Drive connection is required.**

## Output

The program displays two images:

### Original

The original grayscale image.

### Filtered

The image after applying the 9 × 9 mean filter.

### Output Image

<img width="1224" height="591" alt="image" src="https://github.com/user-attachments/assets/43589ed1-51cf-4609-9ecf-39c932293c58" />


## Result

The mean filter smooths the image by averaging neighboring pixel values. Fine details and sharp variations are reduced, producing the blurred/smoothed output shown above.

## Author

**Vishnu Vardhan**

GitHub: [Vishnu-1110](https://github.com/Vishnu-1110)
