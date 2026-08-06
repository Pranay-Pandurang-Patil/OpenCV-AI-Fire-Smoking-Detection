import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile
from services.video_service import process_video

from services.image_service import process_image

# ---------------- PAGE ---------------- #

st.set_page_config(
    page_title="AI Safety Monitoring System",
    page_icon="🔥",
    layout="wide"
)

st.title("🔥 AI Safety Monitoring System")

st.markdown("---")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("Detection Settings")

mode = st.sidebar.radio(
    "Detection Mode",
    [
        "Fire Detection",
        "Cigarette Smoking Detection"
    ]
)

mode = "fire" if mode == "Fire Detection" else "smoking"

input_type = st.sidebar.radio(
    "Input Source",
    [
        "Image",
        "Video",
        "Webcam"
    ]
)

# ---------------- IMAGE ---------------- #

if input_type == "Image":

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image is not None:

        image = Image.open(uploaded_image)

        image_np = np.array(image)

        image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        result, count = process_image(mode, image_cv)

        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image, use_container_width=True)

        with col2:
            st.subheader("Detection Result")
            st.image(result, use_container_width=True)

        st.success(f"Objects Detected : {count}")

# ---------------- VIDEO ---------------- #

elif input_type == "Video":

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4", "avi", "mov"]
    )

    if uploaded_video is not None:

        temp_video = tempfile.NamedTemporaryFile(delete=False)

        temp_video.write(uploaded_video.read())

        temp_video.close()

        with st.spinner("Running AI Detection..."):

            output_video = process_video(
                mode,
                temp_video.name
            )

        st.success("Detection Completed!")

        st.video(output_video)

        with open(output_video, "rb") as file:

            st.download_button(
                "Download Result",
                file,
                file_name="detected_video.mp4"
            )