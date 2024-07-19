from utils import make_dataframe_passing,pre_process_stats,make_dataframe_passing_player
import pandas as pd
from collections import defaultdict 



def get_pass_percent_team1(id):
        team1df = pd.read_csv("./data/team1.csv")
        team1df['id'] = range(1, len(team1df) + 1)
        #now we need to find the average locations and counts of the passes
        average_locations = team1df.groupby('from_id').agg({'startx':['mean'],'starty':['mean','count']})
        average_locations.columns = ['startx','starty','count']
        average_locations = average_locations.reset_index()
        totalpass = sum(average_locations['count'])
        totalpass
        passpercent = []
        if id in average_locations['from_id']:
            for i in average_locations['count']:
                passpercent.append(round(((i/totalpass)*100),2))
            average_locations['passpercent'] = passpercent
            passpercent = average_locations[average_locations['from_id'] == id]['passpercent']
            print(passpercent)
            return passpercent
        else:
            return 0
    
    
def get_pass_percent_team2(id):
        team2df = pd.read_csv("./data/team2.csv")
        team2df['id'] = range(1, len(team2df) + 1)
        #now we need to find the average locations and counts of the passes
        average_locations = team2df.groupby('from_id').agg({'startx':['mean'],'starty':['mean','count']})
        average_locations.columns = ['startx','starty','count']
        average_locations = average_locations.reset_index()
        totalpass = sum(average_locations['count'])
        totalpass
        passpercent = []
        if id in average_locations['from_id']:
            for i in average_locations['count']:
                passpercent.append(round(((i/totalpass)*100),2))
            average_locations['passpercent'] = passpercent
            passpercent = average_locations[average_locations['from_id'] == id]['passpercent']
            print(passpercent)
            return passpercent
        else:
            return 0
            
        


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
       
        player_stats1 = defaultdict(lambda: {'speed': [],'distance':[],'balltouchcount' : 0,"passpercent":0})
        player_stats2 = defaultdict(lambda: {'speed': [],'distance':[],'balltouchcount':0,"passpercent":0})
        
        
        
        for frame_number,frame in enumerate(tracks['players']):
            for id,info in frame.items():
                if info['team'] == 1:
                    if info.get('speed') and info.get('distance') is not None:
                        player_stats1[id]['speed'].append(info['speed'])
                        player_stats1[id]['distance'].append(info['distance'])
                        
                if info['team'] == 2:
                    if info.get('speed') and info.get('distance') is not None:
                        player_stats2[id]['speed'].append(info['speed'])
                        player_stats2[id]['distance'].append(info['distance'])        

                if info.get('has_ball') and info.get('position_transformed') is not None :
                    startx = info['position_transformed'][0]
                    starty = info['position_transformed'][1]
                    
                    if info['team'] == 1:
                        player_stats1[id]['balltouchcount']+=1
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
                        player_stats2[id]['balltouchcount']+=1

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
                                
                     
                           
    # very dirty written code  
        make_dataframe_passing(team1=team1_dict,team2=team2_dict)          
        
        for team1 in team1_dict:
            id = team1['from_id']
            passpercent = get_pass_percent_team1(id=id)
            player_stats1[id]['passpercent']=passpercent
            
        for team1 in team2_dict:
            id = team1['from_id']
            passpercent = get_pass_percent_team2(id=id)
            player_stats2[id]['passpercent']=passpercent    
                      
        pro_stats1 =  pre_process_stats(data=player_stats1)    
        pro_stats2 =  pre_process_stats(data=player_stats2)  
        make_dataframe_passing_player(pro_stats1,pro_stats2)
        print(pro_stats1)        
                            
                            
                                
# [{'from_id': 21, 'startx': 17.37043571472168, 'starty': 60.942867279052734, 'to_id': 8, 'endx': 18.16698455810547, 'endy': 67.48077392578125}, {'from_id': 8, 'startx': 18.16698455810547, 'starty': 67.48077392578125, 'to_id': 12, 'endx': 0.8221856355667114, 'endy': 60.047794342041016}, {'from_id': 12, 'startx': 0.8221856355667114, 'starty': 60.047794342041016, 'to_id': 10, 'endx': 10.112043380737305, 'endy': 38.45918655395508}, {'from_id': 10, 'startx': 10.112043380737305, 'starty': 38.45918655395508, 'to_id': 125, 'endx': 15.273971557617188, 'endy': 20.66996955871582}, {'from_id': 125, 'startx': 15.273971557617188, 'starty': 20.66996955871582, 'to_id': 16, 'endx': 17.060165405273438, 'endy': 32.92456817626953}]


# [{'from_id': 83, 'startx': 0.03188326209783554, 'starty': 37.24459457397461, 'to_id': 109, 'endx': 0.15236268937587738, 'endy': 37.36738967895508}, {'from_id': 109, 'startx': 0.15236268937587738, 'starty': 37.36738967895508, 'to_id': 83, 'endx': 0.19868828356266022, 'endy': 37.37580871582031}, {'from_id': 83, 'startx': 0.19868828356266022, 'starty': 37.37580871582031, 'to_id': 116, 'endx': 0.8779093623161316, 'endy': 37.70035934448242}, {'from_id': 116, 'startx': 0.8779093623161316, 'starty': 37.70035934448242, 'to_id': 83, 'endx': 0.9206735491752625, 'endy': 37.60769271850586}, {'from_id': 83, 'startx': 0.9206735491752625, 'starty': 37.60769271850586, 'to_id': 3, 'endx': 8.427682876586914, 'endy': 39.97071075439453}, {'from_id': 3, 'startx': 8.427682876586914, 'starty': 39.97071075439453, 'to_id': 7, 'endx': 19.412517547607422, 'endy': 28.095239639282227}]
