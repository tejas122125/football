import cv2
import plotly.graph_objects as go


def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(ouput_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (ouput_video_frames[0].shape[1], ouput_video_frames[0].shape[0]))
    for frame in ouput_video_frames:
        out.write(frame)
    out.release()
    
    
    

def max_speed_guage(value,threshhold =20, title = "Max Speed Meter"):
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        title={'text': title, 'font': {'size': 24}},
        delta={'reference': threshhold, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#677AF6"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'red'},
                {'range': [10, 20], 'color': 'orange'},
                {'range': [20, 30], 'color': 'yellow'},
                {'range': [30, 40], 'color': 'lightgreen'},
                {'range': [40, 70], 'color': 'green'}],
            'threshold': {
                'line': {'color': "#DF5E14", 'width': 4},
                'thickness': 0.75,
                'value': threshhold}}))

    fig.update_layout(
        # title={'text': title, 'font': {'size': 24}}
        font={'color': "darkblue", 'family': "Arial"},
                paper_bgcolor="#0A0F2F",

        plot_bgcolor="white")

    # fig.show()
    return fig    