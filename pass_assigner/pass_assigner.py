from utils import make_dataframe_passing
from collections import defaultdict 
class Pass_Assigner:
    def __init__(self) -> None:
            pass
    
    
    def pass_assigner(self,tracks):
        past_1 = {}
        team1_dict = []
        count1 =-1
        count2 =-1
        past_2 ={}
        team2_dict = []
       
        player_stats = defaultdict(lambda: {'speed': [],'distance':[]})
        
        
        for frame_number,frame in enumerate(tracks['players']):
            for id,info in frame.items():
                if info.get('speed') and info.get('distance') is not None:
                    player_stats[id]['speed'].append(info['speed'])
                    player_stats[id]['distance'].append(info['distance'])
                if info.get('has_ball') and info.get('position_transformed') is not None :
                    startx = info['position_transformed'][0]
                    starty = info['position_transformed'][1]
                    
                    if info['team'] == 1:
                        if count1 == -1:
                            
                            past_1 = {
                                "from_id" : id,
                                 "startx" : startx,
                                 "starty" : starty,
                                 "to_id" : None,
                                 "endx" : None,
                                 "endy" : None
                            }
                            count1 = 1
                        else:
                            if past_1['from_id'] != id:
                                data = {
                                    "from_id" : past_1['from_id'],
                                    "startx" : past_1["startx"],
                                    "starty" : past_1['starty'],
                                    "to_id" : id,
                                    "endx" : startx,
                                    "endy" : starty
                                }
                                past_1 =  {
                                    "from_id" : id,
                                    "startx" : startx,
                                    "starty" : starty,
                                    "to_id" : None,
                                    "endx" :None,
                                    "endy" : None
                                }
                                team1_dict.append(data)
                            
                    if info['team'] == 2:
                        if count2 == -1:
                            past_2 = {
                                "from_id" : id,
                                 "startx" : startx,
                                 "starty" : starty,
                                 "to_id" : None,
                                 "endx" : None,
                                 "endy" : None
                            }
                            count2 =1
                        else:
                            if past_2['from_id'] != id:
                                data = {
                                    "from_id" : past_2['from_id'],
                                    "startx" : past_2["startx"],
                                    "starty" : past_2['starty'],
                                    "to_id" : id,
                                    "endx" : startx,
                                    "endy" : starty
                                }
                                past_2 =  {
                                        "from_id" : id,
                                        "startx" : startx,
                                        "starty" : starty,
                                        "to_id" : None,
                                        "endx" :None,
                                        "endy" : None
                                    }
                                team2_dict.append(data)
                                
                                # preprocess playrstas
                                
                                
                                
        make_dataframe_passing(team1=team1_dict,team2=team2_dict,player_stats = player_stats)                        

        print(team2_dict)        
                            
                            
                                
# [{'from_id': 21, 'startx': 17.37043571472168, 'starty': 60.942867279052734, 'to_id': 8, 'endx': 18.16698455810547, 'endy': 67.48077392578125}, {'from_id': 8, 'startx': 18.16698455810547, 'starty': 67.48077392578125, 'to_id': 12, 'endx': 0.8221856355667114, 'endy': 60.047794342041016}, {'from_id': 12, 'startx': 0.8221856355667114, 'starty': 60.047794342041016, 'to_id': 10, 'endx': 10.112043380737305, 'endy': 38.45918655395508}, {'from_id': 10, 'startx': 10.112043380737305, 'starty': 38.45918655395508, 'to_id': 125, 'endx': 15.273971557617188, 'endy': 20.66996955871582}, {'from_id': 125, 'startx': 15.273971557617188, 'starty': 20.66996955871582, 'to_id': 16, 'endx': 17.060165405273438, 'endy': 32.92456817626953}]


# [{'from_id': 83, 'startx': 0.03188326209783554, 'starty': 37.24459457397461, 'to_id': 109, 'endx': 0.15236268937587738, 'endy': 37.36738967895508}, {'from_id': 109, 'startx': 0.15236268937587738, 'starty': 37.36738967895508, 'to_id': 83, 'endx': 0.19868828356266022, 'endy': 37.37580871582031}, {'from_id': 83, 'startx': 0.19868828356266022, 'starty': 37.37580871582031, 'to_id': 116, 'endx': 0.8779093623161316, 'endy': 37.70035934448242}, {'from_id': 116, 'startx': 0.8779093623161316, 'starty': 37.70035934448242, 'to_id': 83, 'endx': 0.9206735491752625, 'endy': 37.60769271850586}, {'from_id': 83, 'startx': 0.9206735491752625, 'starty': 37.60769271850586, 'to_id': 3, 'endx': 8.427682876586914, 'endy': 39.97071075439453}, {'from_id': 3, 'startx': 8.427682876586914, 'starty': 39.97071075439453, 'to_id': 7, 'endx': 19.412517547607422, 'endy': 28.095239639282227}]
