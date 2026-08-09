import io
import os
import tempfile

import av
import cv2
import numpy as np
import streamlit as st

from PIL import Image
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

from services.image_service import process_image
from services.video_service import process_video_live
from services.webcam_service import process_webcam_frame


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Safety Monitoring System",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #0b1120;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #263244;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #f8fafc;
}

/* Main title */

.main-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 0.2rem;
}

.main-subtitle {
    color: #94a3b8;
    font-size: 1rem;
    margin-bottom: 1.5rem;
}

/* Metrics */

div[data-testid="stMetric"] {
    background-color: #111827;
    border: 1px solid #263244;
    border-radius: 14px;
    padding: 15px;
}

div[data-testid="stMetricLabel"] {
    color: #94a3b8;
}

div[data-testid="stMetricValue"] {
    color: #f8fafc;
}

/* File uploader */

section[data-testid="stFileUploaderDropzone"] {
    background-color: #111827;
    border: 2px dashed #334155;
    border-radius: 14px;
}

/* Buttons */

.stButton > button {
    border-radius: 10px;
    font-weight: 600;
}

/* Divider */

hr {
    border-color: #263244;
}

/* Alerts */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Footer */

.footer-text {
    color: #64748b;
    text-align: center;
    margin-top: 3rem;
    font-size: 0.85rem;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# WEBCAM PROCESSOR
# ============================================================

class WebcamProcessor(VideoProcessorBase):

    def __init__(self):

        self.mode = "fire"
        self.object_count = 0

    def recv(self, frame):

        image = frame.to_ndarray(
            format="bgr24"
        )

        result, count = process_webcam_frame(
            self.mode,
            image
        )

        self.object_count = count

        return av.VideoFrame.from_ndarray(
            result,
            format="bgr24"
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🔥 AI Safety")

    st.caption(
        "Monitoring & Detection System"
    )

    st.divider()

    st.subheader(
        "Detection Mode"
    )

    detection_mode = st.radio(
        "Choose detection",
        [
            "🔥 Fire Detection",
            "🚬 Cigarette Smoking Detection"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.subheader(
        "Input Source"
    )

    input_source = st.radio(
        "Choose input",
        [
            "🖼️ Image",
            "🎬 Video",
            "📷 Webcam"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.caption(
        "AI Safety Monitoring System"
    )

    st.caption(
        "OpenCV • YOLO • Streamlit"
    )


# ============================================================
# DETECTION MODE
# ============================================================

if detection_mode == "🔥 Fire Detection":

    mode = "fire"

    detection_name = "Fire"

    detection_icon = "🔥"

    description = (
        "AI-powered detection of fire and flames."
    )

else:

    mode = "smoking"

    detection_name = "Smoking"

    detection_icon = "🚬"

    description = (
        "AI-powered detection of cigarette smoking."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🔥 AI Safety Monitoring System'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Intelligent computer vision for real-time '
    'safety monitoring and detection.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# STATUS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        label="SYSTEM",
        value="● Ready"
    )


with col2:

    st.metric(
        label="DETECTION",
        value=f"{detection_icon} {detection_name}"
    )


with col3:

    st.metric(
        label="INPUT",
        value=input_source
    )


st.divider()


# ============================================================
# WORKSPACE
# ============================================================

st.subheader(
    "AI Detection Workspace"
)

st.caption(
    f"{detection_icon} "
    f"{detection_name} detection model selected"
)

st.write(
    description
)


# ============================================================
# IMAGE DETECTION
# ============================================================

if input_source == "🖼️ Image":

    st.info(
        f"Upload an image for "
        f"{detection_name.lower()} detection."
    )

    uploaded_image = st.file_uploader(
        "Choose an image",
        type=[
            "jpg",
            "jpeg",
            "png",
            "webp"
        ],
        label_visibility="collapsed"
    )

    if uploaded_image:

        image = Image.open(
            uploaded_image
        ).convert("RGB")

        image_np = np.array(
            image
        )

        image_cv = cv2.cvtColor(
            image_np,
            cv2.COLOR_RGB2BGR
        )

        st.success(
            f"Image loaded: "
            f"{uploaded_image.name}"
        )

        image_col1, image_col2 = st.columns(2)

        # ----------------------------------------
        # ORIGINAL
        # ----------------------------------------

        with image_col1:

            st.subheader(
                "Original Image"
            )

            st.image(
                image,
                use_container_width=True
            )

        # ----------------------------------------
        # DETECTION
        # ----------------------------------------

        with image_col2:

            st.subheader(
                "AI Detection Result"
            )

            with st.spinner(
                f"Running "
                f"{detection_name.lower()} "
                f"detection..."
            ):

                result, count = process_image(
                    mode,
                    image_cv
                )

            result_rgb = cv2.cvtColor(
                result,
                cv2.COLOR_BGR2RGB
            )

            st.image(
                result_rgb,
                use_container_width=True
            )

        # ----------------------------------------
        # RESULT
        # ----------------------------------------

        st.divider()

        st.subheader(
            "Detection Result"
        )

        if count > 0:

            st.success(
                f"{detection_icon} "
                f"{detection_name} detected"
            )

        else:

            st.success(
                f"✓ No "
                f"{detection_name.lower()} "
                f"detected"
            )

        # ----------------------------------------
        # METRICS
        # ----------------------------------------

        metric1, metric2, metric3 = st.columns(3)

        with metric1:

            st.metric(
                "Objects Detected",
                count
            )

        with metric2:

            st.metric(
                "Model",
                detection_name
            )

        with metric3:

            st.metric(
                "Status",
                "Completed"
            )

        # ----------------------------------------
        # DOWNLOAD
        # ----------------------------------------

        result_image = Image.fromarray(
            result_rgb
        )

        buffer = io.BytesIO()

        result_image.save(
            buffer,
            format="PNG"
        )

        st.download_button(
            label="⬇️ Download Detection Result",
            data=buffer.getvalue(),
            file_name="detection-result.png",
            mime="image/png",
            use_container_width=True
        )


# ============================================================
# VIDEO DETECTION
# ============================================================

elif input_source == "🎬 Video":

    st.info(
        f"Upload a video for "
        f"{detection_name.lower()} detection."
    )

    uploaded_video = st.file_uploader(
        "Choose a video",
        type=[
            "mp4",
            "avi",
            "mov",
            "mkv"
        ],
        label_visibility="collapsed"
    )

    if uploaded_video:

        st.success(
            f"Video loaded: "
            f"{uploaded_video.name}"
        )

        # ----------------------------------------
        # ORIGINAL VIDEO
        # ----------------------------------------

        st.subheader(
            "Original Video"
        )

        st.video(
            uploaded_video
        )

        st.divider()

        # ----------------------------------------
        # START DETECTION
        # ----------------------------------------

        start_detection = st.button(
            "▶️ Start Live Detection",
            use_container_width=True
        )

        if start_detection:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            ) as temp_file:

                temp_file.write(
                    uploaded_video.getbuffer()
                )

                input_path = temp_file.name

            st.subheader(
                "🔴 Live Detection Processing"
            )

            frame_placeholder = st.empty()

            status_placeholder = st.empty()

            metric1, metric2, metric3 = st.columns(3)

            frame_metric = metric1.empty()

            object_metric = metric2.empty()

            fps_metric = metric3.empty()

            def update_frame(
                frame,
                count,
                frame_number,
                fps
            ):

                frame_rgb = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                frame_placeholder.image(
                    frame_rgb,
                    channels="RGB",
                    use_container_width=True
                )

                frame_metric.metric(
                    "Frames Processed",
                    frame_number
                )

                object_metric.metric(
                    "Objects in Frame",
                    count
                )

                fps_metric.metric(
                    "Video FPS",
                    f"{fps:.1f}"
                )

                status_placeholder.info(
                    f"🔴 Processing frame "
                    f"{frame_number}..."
                )

            try:

                frame_count, total_objects = (
                    process_video_live(
                        mode,
                        input_path,
                        update_frame
                    )
                )

                status_placeholder.success(
                    "✅ Video detection completed."
                )

                st.success(
                    f"Processed {frame_count} "
                    f"frames • "
                    f"Total detections: "
                    f"{total_objects}"
                )

            except Exception as error:

                status_placeholder.error(
                    "❌ Video detection failed."
                )

                st.exception(
                    error
                )

            finally:

                if os.path.exists(
                    input_path
                ):

                    os.remove(
                        input_path
                    )


# ============================================================
# WEBCAM / LIVE DETECTION
# ============================================================

elif input_source == "📷 Webcam":

    st.info(
        f"Live {detection_name.lower()} "
        f"detection using your camera."
    )

    ctx = webrtc_streamer(
        key="ai-safety-webcam",
        video_processor_factory=WebcamProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        },
        async_processing=True
    )

    if ctx.video_processor:

        ctx.video_processor.mode = mode

        st.success(
            "🔴 Live detection is active"
        )

        st.metric(
            "Objects Detected",
            ctx.video_processor.object_count
        )

    else:

        st.info(
            "Click START to enable "
            "the webcam."
        )


# ============================================================
# GENERAL STATISTICS
# ============================================================

st.divider()

st.subheader(
    "Detection Statistics"
)

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:

    st.metric(
        "Objects Detected",
        "—"
    )

with stat2:

    st.metric(
        "Confidence",
        "—"
    )

with stat3:

    st.metric(
        "FPS",
        "—"
    )

with stat4:

    st.metric(
        "Status",
        "Ready"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer-text">'
    'AI Safety Monitoring System '
    '• OpenCV • YOLO • Streamlit'
    '</div>',
    unsafe_allow_html=True
)