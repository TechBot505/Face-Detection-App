﻿# Face Detection App
This is a simple yet powerful Face Detection application built with Streamlit and OpenCV. The application not only detects faces but also identifies smiles and eyes within the uploaded image. Additionally, it provides features to enhance images by adjusting brightness, contrast, blurring, as well as transforming images into cartoon-like or canny versions.

### Features
1. Face Detection
   * Upload an image and detect faces within it.
   * Displays the number of faces detected.
     
2. Smile Detection
   * Detect smiles within the uploaded image.
   * Displays the number of smiles detected.
     
3. Eye Detection
   * Detect eyes within the uploaded image.
   * Displays the number of eyes detected.

4. Image Enhancement
   * **Gray-Scale**: Convert the uploaded image to grayscale.
   * **Contrast**: Adjust the contrast of the image.
   * **Brightness**: Adjust the brightness of the image.
   * **Blurrying**: Apply Gaussian blurring to the image.
  
5. Image Transformation
   * **Cartoonize**: Transform the image into a cartoon-like version.
   * **Cannize**: Convert the image into a canny edge detection version.

### How to Use
1. **Upload Image**: Click on the "Upload Image" button and select an image file (supported formats: jpg, png, jpeg).
2. **Enhance Image**: Choose from different enhancement options available in the sidebar such as Gray-Scale, Contrast, Brightness, or Blurring. Adjust the sliders accordingly for Contrast, Brightness, and Blurring options.
3. **Detect Features**: Select the feature you want to detect from the dropdown menu: Faces, Smiles, Eyes, Cannize, or Cartoonize.
4. **Process**: Click on the "Process" button to execute the selected operation.
5. **View Results**: The processed image with detected features or enhanced version will be displayed.

### Requirements
* Python 3.x
* Streamlit
* NumPy
* Pillow (PIL)
* OpenCV

### Installation
1. Clone this repository:
   `git clone https://github.com/yourusername/facedetection-app.git`
2. Install the required dependencies:
   `pip install -r requirements.txt`
3. Run the application:
   `streamlit run app.py`
