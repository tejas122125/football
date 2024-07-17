import math
import pandas as pd
def get_center_of_bbox(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int((y1+y2)/2)

def get_bbox_width(bbox):
    return bbox[2]-bbox[0]

def measure_distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def measure_xy_distance(p1,p2):
    return p1[0]-p2[0],p1[1]-p2[1]

def get_foot_position(bbox):
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int(y2)


def are_rgb_close(rgb1, rgb2, threshold=80):
    """
    16,55
    Checks if two RGB tuples are close based on Euclidean distance.
    
    Args:
    - rgb1, rgb2: Tuple representing RGB values, e.g., (R, G, B).
    - threshold: Maximum distance threshold. Default is 50.
    
    Returns:
    - True if the Euclidean distance between rgb1 and rgb2 is <= threshold, False otherwise.
    """
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    
    # Calculate Euclidean distance
    distance = math.sqrt((r2 - r1)**2 + (g2 - g1)**2 + (b2 - b1)**2)
    
    # Check if distance is within threshold
    return distance <= threshold


def make_dataframe_passing(team1,team2):
    team1df = pd.DataFrame(team1)
    team1df.to_csv("./data/team1.csv")
    
    team2df = pd.DataFrame(team2)
    team2df.to_csv("./data/team2.csv")