import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Video Processing App",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add some CSS styles
with open("styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title
st.title("📽️ Video Processing App")

# Introduction
st.write("""
    ### Introduction
    Video processing is an essential field in computer vision and multimedia applications. It involves manipulating and analyzing video data to extract meaningful information, enhance quality, or apply creative effects.

    This project is focused on exploring various aspects of video processing, including video cropping, resizing, live recording, frame capturing, and applying filters using the powerful OpenCV library.
""")

# OpenCV section
st.header("OpenCV")
st.write("""
    OpenCV (Open Source Computer Vision Library) is a popular open-source library for computer vision and image processing tasks. It provides a wide range of tools and functions for image and video manipulation, object detection, and many other applications.

    In this project, we leverage OpenCV's capabilities to perform various video processing tasks, such as:
""")

# Project features
st.subheader("Project Features")
st.write("""
    1. **Video Cropping and Resizing**: Crop and resize videos to desired dimensions, aspect ratios, or regions of interest.
    2. **Live Video Recording and Capturing**: Record live video from a webcam or external camera and capture individual frames for further processing or analysis.
    3. **OpenCV Filters**: Apply various filters to video frames, including:
        - **Noop Filter**: No filter applied, original video frame.
        - **Cartoon Filter**: Convert the video frame into a cartoon-like style.
        - **Edges Filter**: Detect and highlight edges in the video frame.
        - **Rotate Filter**: Rotate the video frame by a specified angle.
""")

# Video Cropping and Resizing
st.write("""
    #### Video Cropping and Resizing
    Video cropping and resizing are essential techniques for adjusting video dimensions, aspect ratios, and regions of interest. This feature allows you to:

    - Crop videos by specifying the region of interest (ROI) coordinates or using a graphical interface.
    - Resize videos to match desired dimensions or aspect ratios.
    - Maintain or adjust the aspect ratio during resizing.
    - Apply padding or cropping to handle aspect ratio changes.

    These operations are useful for various purposes, such as removing unwanted areas from the video, adjusting the video size for different displays or devices, or preparing the video for further processing or analysis.
""")

# Live Video Recording and Capturing
st.write("""
    #### Live Video Recording and Capturing
    The live video recording and capturing feature allows you to:

    - Access and control connected webcams or external cameras.
    - Preview the live video feed in real-time.
    - Record video from the selected camera source.
    - Capture individual frames from the live video stream.
    - Save recorded videos and captured frames to disk.
    - Video Delay feature while recording real-time

    This functionality is beneficial for tasks like video conferencing, surveillance, and creating datasets for computer vision models.
""")

# OpenCV Filters
st.write("""
    #### OpenCV Filters
    OpenCV provides a wide range of image and video processing functions, including various filters. In this project, we explore the following filters:

    **Noop Filter**:
    The Noop (No Operation) filter simply displays the original video frame without any modifications. This can be useful as a baseline for comparing the effects of other filters.

    **Cartoon Filter**:
    The Cartoon filter applies a stylized, non-photorealistic rendering technique to the video frame, giving it a cartoon-like appearance. This filter is achieved by a combination of edge detection, quantization, and selective blurring/sharpening.

    **Edges Filter**:
    The Edges filter detects and highlights the edges in the video frame. It uses edge detection algorithms like Canny, Sobel, or Laplacian to identify the boundaries between different regions or objects in the frame.

    **Rotate Filter**:
    The Rotate filter allows you to rotate the video frame by a specified angle. This can be useful for correcting the orientation of the video or applying creative rotations for artistic purposes.
""")

# Add some example images
col1, col2, col3 = st.columns(3)
with col1:
    st.image(Image.open("example1.png"), caption="Amazing Dashboard", use_column_width=True)
with col2:
    st.image(Image.open("example2.png"), caption="Crop & Resize Options", use_column_width=True)
with col3:
    st.image(Image.open("example3.png"), caption="OpenCv Filters", use_column_width=True)

# Conclusion
st.write("""
    ### Conclusion
    This video processing app provides a comprehensive set of tools and features for manipulating videos, capturing frames, and applying creative filters. By leveraging the powerful OpenCV library, we can explore various techniques and algorithms in the field of computer vision and multimedia processing.

    Stay tuned for more exciting updates and functionalities!
""")