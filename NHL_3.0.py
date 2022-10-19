import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import NHL
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def getImage(path, zoom = 0.02):
    return OffsetImage(plt.imread(path), zoom = zoom) 

images = ['New_Jersey.png','Islanders.png', 'New York.png', 'Philly.png', 'Pitsburgh.png', 'Boston.png', 
            'Buffalo.png', 'Montreal.png', 'Ottawa.png', 'Toronto.png', 'Atlanta.png', 'Carolina.png', 
            'Florida.png', 'Tampa Bay.png', 'Washington.png', 'Chicago.png', 'Detroit.png', 'Nashville.png', 
            'St.Louis.png', 'Calgary.png', 'Colorado.png', 'Edmonton.png', 'Vancouver.png', 'Anaheim.png', 
            'Dallas.png', 'LA.png', 'Phoenix.png', 'San Jose.png', 'Colombus.png', 'Minnesota.png', 'Winnipeg.png', 
            'Arizona.png', 'Vegas.png']

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

