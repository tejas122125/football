import streamlit as st

import os

# Function to load sample video
def load_sample_video():
    sample_video_path = "./input_videos/test1.mp4"  
    return sample_video_path

# Function to save uploaded file
def save_uploaded_file(uploaded_file):
    save_dir = "user_input/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, "hui.mp4")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path


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
        file_path = save_uploaded_file(uploaded_file)

        st.session_state.video_path = file_path
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
