from utils import read_video, save_video
from trackers import Tracker
import cv2
import numpy as np
from team_assigner import TeamAssigner
from player_ball_assigner import PlayerBallAssigner
from camera_movement_estimator import CameraMovementEstimator
from view_transformer import ViewTransformer
from speed_and_distance_estimator import SpeedAndDistance_Estimator
from pass_assigner import Pass_Assigner

def mastertejas( path):
        # Read Video
    video_frames = read_video(path)

    # Initialize Tracker
    tracker = Tracker('models/finetuned.pt')
    testingframe = video_frames

    tracks = tracker.get_object_tracks(testingframe,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
    
        # Get object positions 
    tracker.add_position_to_tracks(tracks)
    
    # camera movement estimator
    camera_movement_estimator = CameraMovementEstimator(video_frames[0])
    camera_movement_per_frame = camera_movement_estimator.get_camera_movement(video_frames,
                                                                                read_from_stub=True,
                                                                                stub_path='stubs/camera_movement_stub.pkl')
    camera_movement_estimator.add_adjust_positions_to_tracks(tracks,camera_movement_per_frame)
    
        # View Trasnformer
    view_transformer = ViewTransformer()
    view_transformer.add_transformed_position_to_tracks(tracks)
    
    
    # Interpolate Ball Positions
    tracks["ball"] = tracker.interpolate_ball_positions(tracks["ball"])
    
        # Speed and distance estimator
    speed_and_distance_estimator = SpeedAndDistance_Estimator()
    speed_and_distance_estimator.add_speed_and_distance_to_tracks(tracks)
    
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
            
    # Assign Ball Aquisition
    player_assigner =PlayerBallAssigner()
    team_ball_control= []
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True
            teamnumber = 0
            teamnumber = tracks['players'][frame_num][assigned_player]['team']
            
            if (teamnumber is not None):
             team_ball_control.append(teamnumber)
                
            else:
                
                print("invalid")  
                team_ball_control.append(0)
                
        else:
            
            
            team_ball_control.append(team_ball_control[-1])
    team_ball_control= np.array(team_ball_control)        
    # print(team_ball_control)
    test1 = Pass_Assigner()
    test1.pass_assigner(tracks)
    # print(tracks['players'][0])
    # print(tracks)
    # print(len(tracks['referees']))
    # # for r,v in tracks.items() :
    # #     print(r)
    # #     # break
    
    output_video_frames = tracker.draw_annotations(testingframe, tracks,team_ball_control)
    
    ## Draw Camera movement
    output_video_frames = camera_movement_estimator.draw_camera_movement(output_video_frames,camera_movement_per_frame)

    ## Draw Speed and Distance
    speed_and_distance_estimator.draw_speed_and_distance(output_video_frames,tracks)
    # print(tracks['players'][0])


    save_video(output_video_frames, 'output_videos/output_video.avi')
