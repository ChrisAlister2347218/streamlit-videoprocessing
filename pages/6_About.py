import streamlit as st

def about_page():
    st.set_page_config(page_title="About", page_icon=":movie_camera:")
    st.title("About the Author")
    st.markdown(
        """
        Hi there! My name is Chris Alister, and I'm a Student with a passion for Learning and exploring various python libraries and functionalities. 
        This video processing application is a project I've been working on to explore various aspects of video manipulation, including cropping, resizing, live recording, frame capturing, and applying creative filters using the powerful OpenCV library. 
        The primary goal of this project is to provide a user-friendly interface for individuals to experiment with video processing techniques and leverage the capabilities of OpenCV. 
        Whether you're a hobbyist, a content creator, or a professional in the field, this application aims to offer a range of tools and features to meet your video processing needs.
        """
    )
    st.markdown(
        """
        **Social Media and Contact:**
        - LinkedIn: [Chris Alister](https://in.linkedin.com/in/chris-alister-5713b2284)
        - GitHub: [ChrisAlister2347218](https://github.com/ChrisAlister2347218)
        - Email: [chris.alister@mca.christuniversity.in](mailto:chris.alister@mca.christuniversity.in)
        """
    )
    st.markdown(
        """
        I'm excited to continue exploring and expanding the functionalities of this video processing application. Stay tuned for more updates and exciting features! 
        Thank you for your interest and support! Best regards, Chris Alister
        """
    )

if __name__ == "__main__":
    about_page()
