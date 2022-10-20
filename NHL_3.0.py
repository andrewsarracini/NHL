import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import NHL
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import NHL_Teams
from PIL import Image



def getImage(path, zoom = 0.02):
    return OffsetImage(plt.imread(path), zoom = zoom) 

images = ['NHL_Teams/New_Jersey.png','NHL_Teams/Islanders.png', 'NHL_Teams/New York.png', 'NHL_Teams/Philly.png', 'NHL_Teams/Pitsburgh.png', 'NHL_Teams/Boston.png', 
            'NHL_Teams/Buffalo.png', 'NHL_Teams/Montreal.png', 'NHL_Teams/Ottawa.png', 'NHL_Teams/Toronto.png', 'NHL_Teams/Atlanta.png', 'NHL_Teams/Carolina.png', 
            'NHL_Teams/Florida.png', 'NHL_Teams/Tampa Bay.png', 'NHL_Teams/Washington.png', 'NHL_Teams/Chicago.png', 'NHL_Teams/Detroit.png', 'NHL_Teams/Nashville.png', 
            'NHL_Teams/St.Louis.png', 'NHL_Teams/Calgary.png', 'NHL_Teams/Colorado.png', 'NHL_Teams/Edmonton.png', 'NHL_Teams/Vancouver.png', 'NHL_Teams/Anaheim.png', 
            'NHL_Teams/Dallas.png', 'NHL_Teams/LA.png', 'NHL_Teams/Phoenix.png', 'NHL_Teams/San Jose.png', 'NHL_Teams/Colombus.png', 'NHL_Teams/Minnesota.png', 'NHL_Teams/Winnipeg.png', 
            'NHL_Teams/Arizona.png', 'NHL_Teams/Vegas.png']

x_alts = [250, 89, 13, 39, 846, 33, 597, 52, 236, 289, 997, 354, 3, 7, 10, 
            594, 610, 607, 883, 3432, 5272, 2172, 20, 3694, 435, 243, 1093, 
            92, 755, 791, 305, 1093, 2064]

y_wins = [55.595, 50.526, 52.463, 55.595, 58.683, 57.812, 51.100, 
            53.059, 54.350, 52.587, 44.961, 52.934, 46.764, 58.983, 
            59.159, 55.517, 56.973, 58.382, 57.614, 54.933, 55.357, 
            48.230, 56.316, 57.008, 58.519, 53.974, 52.579, 59.977,
            51.188, 54.644, 54.586, 45.938, 62.128]

fig, ax = plt.subplots() 
ax.scatter(x_alts, y_wins) 

for x_alt, y_win, image in zip(x_alts, y_wins, images):
    ab = AnnotationBbox(getImage(image), (x_alt, y_win), frameon=False) 
    ax.add_artist(ab) 

plt.xlabel('Altitude (ft.)')
plt.ylabel('Home Win Percentage')
plt.title('Altitude vs Home Win Percentage for NHL Teams')

plt.show() 

