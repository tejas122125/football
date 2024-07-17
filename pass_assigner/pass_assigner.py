class Pass_Assigner:
    def __init__(self) -> None:
            pass
    
    
    def pass_assigner(self,tracks):
        past_1 = {}
        team1_dict = []
        count1 =-1
        count2 =-1
        past_2 ={}
        team2_dict = {}
        
        
        for frame_number,frame in enumerate(tracks['players']):
            for id,info in frame.items():
                if info.get('has_ball',None)is not None :
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
                            count1 =1
                        else:
                            data = {
                                 "from_id" : past_1['from_id'],
                                 "startx" : past_1["startx"],
                                 "starty" : past_1['starty'],
                                 "to_id" : id,
                                 "endx" : startx,
                                 "endy" : starty
                            }
                            past_1 =data
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
                            data = {
                                 "from_id" : past_2['from_id'],
                                 "startx" : past_2["startx"],
                                 "starty" : past_2['starty'],
                                 "to_id" : id,
                                 "endx" : startx,
                                 "endy" : starty
                            }
                            past_2 =data
                            team2_dict.append(data)

        print(team2_dict)        
                            
                            
                                
                           