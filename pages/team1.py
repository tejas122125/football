import pandas as pd 
import streamlit as st
import plotly.graph_objects as go

from utils import pass_percernt_gauge,total_distance_gauge,ball_touch_count,max_speed_guage

def get_max_speed_fig(value):
    return max_speed_guage(value=value)

def get_ball_touch_count_fig(value):
    return ball_touch_count(value=value)

def get_total_distance_fig(value):
    return total_distance_gauge(value=value)

def get_pass_percent_fig(value):
    return pass_percernt_gauge(value=value)
    

def team1():
    dfteam1 = pd.read_csv("./data/player_stats1.csv")
    ids = dfteam1.columns.to_list()
    for id in ids : 
        maxspeed =  dfteam1[id][0]
        balltouch = dfteam1[id][4]
        passpercent = dfteam1[id][3]
        totaldist  = dfteam1[id][2]
        avgspeed= dfteam1[id][1]
        st.write("  ")
        st.write(f"Statistics for the player id {id}")
        with st.container():
            col1,col2 = st.columns([1,1])
            col3,col4  =  st.columns([1,1])
            
            with col1:
                st.write(" Maximum Speed ")
                fig = get_max_speed_fig(value=maxspeed)
                st.plotly_chart(fig)
            with col2:
                st.write("Ball control ")
                fig = get_ball_touch_count_fig(value=balltouch)
                st.plotly_chart(fig)
        with st.container():        
            with col3:
                st.write(" Passing percent")
                fig = get_pass_percent_fig(value=passpercent)
                st.plotly_chart(fig)
                
            with col4:
                st.write(" Total running distance in meters")
                fig = get_total_distance_fig(value=totaldist)
                st.plotly_chart(fig)    
                    
                    


def main():
    st.title("TEAM 1")
    team1()

if __name__ == "__main__":
    main()