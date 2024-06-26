import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/haarcascade_smile.xml')


def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img, faces


def detect_eyes(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img, eyes


def detect_smiles(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return img, smiles


def cartonize_image(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon


def cannize_image(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    canny = cv2.Canny(img, 100, 150)
    return canny


def main():
    """Face Detection App"""

    st.title("Face Detection App")
    st.text("Build with Streamlit and OpenCV")

    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Detection":
        st.subheader("Face Detection")

        image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

        enhance_type = st.sidebar.radio("Enhance Type",
                                        ["Original", "Gray-Scale", "Contrast", "Brightness", "Blurring"])

        task = ["Faces", "Smiles", "Eyes", "Cannize", "Cartoonize"]
        feature_choice = st.sidebar.selectbox("Find Features", task)

        if image_file is not None:
            our_image = Image.open(image_file)
            # st.text("Original Image")
            # st.image(our_image, width=300)

            if enhance_type == "Gray-Scale":
                new_img = np.array(our_image.convert('RGB'))
                img = cv2.cvtColor(new_img, 1)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                st.image(gray)

            if enhance_type == "Contrast":
                c_rate = st.sidebar.slider("Contrast", 0.5, 3.5)
                enhancer = ImageEnhance.Contrast(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            if enhance_type == "Brightness":
                c_rate = st.sidebar.slider("Brightness", 0.5, 3.5)
                enhancer = ImageEnhance.Brightness(our_image)
                img_output = enhancer.enhance(c_rate)
                st.image(img_output)

            if enhance_type == "Blurring":
                new_img = np.array(our_image.convert('RGB'))
                blur_rate = st.sidebar.slider("Blur Rate", 0.5, 3.5)
                img = cv2.cvtColor(new_img, 1)
                blur = cv2.GaussianBlur(img, (11, 11), blur_rate)
                st.image(blur)

            else:
                st.text("Original Image")
                st.image(our_image, width=300)

            # Face Detection

            if st.button("Process"):

                if feature_choice == "Faces":
                    result_img, result_faces = detect_faces(our_image)
                    st.image(result_img)

                    st.success("Found {} faces".format(len(result_faces)))

                if feature_choice == "Smiles":
                    result_img, result_smiles = detect_smiles(our_image)
                    st.image(result_img)

                    st.success("Found {} smiles".format(len(result_smiles)))

                if feature_choice == "Eyes":
                    result_img, result_eyes = detect_eyes(our_image)
                    st.image(result_img)

                    st.success("Found {} eyes".format(len(result_eyes)))

                if feature_choice == "Cannize":
                    result_img = cannize_image(our_image)
                    st.image(result_img)

                if feature_choice == "Cartoonize":
                    result_img = cartonize_image(our_image)
                    st.image(result_img)

    elif choice == "About":
        st.subheader("About")


if __name__ == '__main__':
    main()
