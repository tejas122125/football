from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner


def main():
        # Read Video
    video_frames = read_video('input_videos/test1.mp4')

    # Initialize Tracker
    tracker = Tracker('models/finetuned.pt')
    testingframe = video_frames

    tracks = tracker.get_object_tracks(testingframe,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
        # Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0], 
                                    tracks['players'][0])
    
    for frame_num, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],   
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team 
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]
    
    # print(tracks['players'][0])
    # print(tracks)
    # print(len(tracks['referees']))
    # # for r,v in tracks.items() :
    # #     print(r)
    # #     # break
    
    output_video_frames = tracker.draw_annotations(testingframe, tracks)

    save_video(output_video_frames, 'output_videos/output_video.avi')
if __name__ == "__main__":
    
    main()    