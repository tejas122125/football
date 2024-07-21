import streamlit as st
import tempfile
import os

# Function to load sample video
def load_sample_video():
    sample_video_path = "./input_videos/test1.mp4"  
    return sample_video_path

# Streamlit app
def main():
    st.title("Video Upload App")

    # Initialize session state for storing the video file path
    if 'video_path' not in st.session_state:
        st.session_state.video_path = None

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_file.write(uploaded_file.read())
        temp_file.close()
        st.session_state.video_path = temp_file.name
        st.success("Uploaded video successfully")

    # Option to select a sample video
    if st.button("Use Sample Video"):
        st.session_state.video_path = load_sample_video()
        st.success("Sample video selected")

    # Display the selected or uploaded video
    if st.session_state.video_path:
        st.video(st.session_state.video_path)
        st.write(f"Current video path: {st.session_state.video_path}")

if __name__ == "__main__":
    main()
