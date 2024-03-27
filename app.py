import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os


def main():
    """Face Detection App"""

    st.title("Face Detection App")
    st.text("Build with Streamlit and OpenCV")

    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Detection":
        st.subheader("Face Detection")

        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

    elif choice == "About":
        st.subheader("About")


if __name__ == '__main__':
    main()