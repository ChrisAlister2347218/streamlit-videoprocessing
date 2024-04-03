import uuid
from pathlib import Path

import av
import cv2
import streamlit as st
from aiortc.contrib.media import MediaRecorder
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import os
import base64
import tempfile 

from sample_utils.turn import get_ice_servers


def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")

    # perform edge detection
    img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


RECORD_DIR = Path("./records")
RECORD_DIR.mkdir(exist_ok=True)

def crop_and_resize_video(input_path, output_path, x, y, width, height):
    """
    Crop and resize a video.

    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the cropped and resized video.
        x (int): X-coordinate of the top-left corner of the crop region.
        y (int): Y-coordinate of the top-left corner of the crop region.
        width (int): Width of the crop region.
        height (int): Height of the crop region.
    """
    cap = cv2.VideoCapture(input_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Crop the frame
        cropped_frame = frame[y:y+height, x:x+width]

        # Resize the cropped frame
        resized_frame = cv2.resize(cropped_frame, (width, height))

        # Write the resized frame to the output video
        out.write(resized_frame)

    cap.release()
    out.release()
    


def app():
    st.set_page_config(page_title="Video Processing App", page_icon="📷")
    if "prefix" not in st.session_state:
        st.session_state["prefix"] = str(uuid.uuid4())
    prefix = st.session_state["prefix"]
    in_file = RECORD_DIR / f"{prefix}_input.mp4"
    out_file = RECORD_DIR / f"{prefix}_output.mp4"

    

    def out_recorder_factory() -> MediaRecorder:
        return MediaRecorder(str(out_file), format="mp4")

    webrtc_streamer(
        key="record",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": get_ice_servers()},
        media_stream_constraints={
            "video": True,
            "audio": True,
        },
        
        
        out_recorder_factory=out_recorder_factory,
    )

    
    if out_file.exists():
        with out_file.open("rb") as f:
            st.download_button(
                "Download the recorded video", f, "output.mp4"
            )
            st.title("Video Crop and Resize Tool")
    st.markdown("---")

    # Upload a video file
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4"])

    if uploaded_file:
        # Save the uploaded file to a temporary location
        temp_file_path = os.path.join(tempfile.gettempdir(), "temp_video.mp4")
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.read())

        # Display the uploaded video
        st.video(temp_file_path)

        # User input for crop region
        st.subheader("Crop Region")
        x = st.slider("X-coordinate", 0, 1920, 100)
        y = st.slider("Y-coordinate", 0, 1080, 100)
        width = st.slider("Width", 1, 1920, 640)
        height = st.slider("Height", 1, 1080, 480)

        # Process the video
        output_path = "output_video.mp4"
        crop_and_resize_video(temp_file_path, output_path, x, y, width, height)

        # Provide option for downloading the processed video
        st.markdown("---")
        st.write("### Options:")
        st.write("Download the cropped and resized video:")
        
        with open(output_path, "rb") as file:
            video_bytes = file.read()
        st.download_button(label="Click here to download", data=video_bytes, file_name="output_video.mp4", mime="video/mp4")
        st.markdown("---")


if __name__ == "__main__":
    app()


