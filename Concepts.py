from cgitb import handler
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.colors import ListedColormap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

''' This works as a great example!'''
# fig, ax = plt.subplots()

# x = [1, 2, 3, 4, 5]
# y = [3, 6, 9, 12, 15]

# values = [0,1,2,3,4]
# values_str = ['red', 'blue', 'green', 'cyan', 'magenta']
# colours = ListedColormap(['r', 'b', 'g', 'c', 'm']) 


# scattery = plt.scatter(x, y, c = values, cmap = colours) 
# plt.legend(handles = scattery.legend_elements()[0], labels = values_str) 
# ax.grid(True) 
# plt.show() 

# x = [1, 3, 4, 6, 7, 9]
# y = [0, 0, 5, 8, 8, 8]

# classes = ['A', 'B', 'C']
# values = [0, 0, 1, 2, 2, 2]
# colors = ['red','blue','green']

# scatter = plt.scatter(x, y, c=values)
# plt.legend(handles=scatter.legend_elements()[0], labels=classes)
# plt.show() 

''' Proof of concept -- logos in place of points '''
# def getImage(path, zoom = 0.015):
#     return OffsetImage(plt.imread(path), zoom = zoom) 

# paths = [
#     'Toronto.png',
#     'Seattle.png', 
#     'Ottawa.png', 
#     'Vancouver.png', 
#     'Calgary.png'] 

# x = [0, 1, 2, 3, 4]
# y = [0, 1, 2, 3, 4]

# fig, ax = plt.subplots() 
# ax.scatter(x, y) 

# for x0, y0, path in zip(x, y, paths): 
#     ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False) 
#     ax.add_artist(ab) 

# plt.show()

''' Plotting Toronto's win pct over five seasons '''

df = pd.DataFrame(np.random.random((200,3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')

df = df.set_index(['date']) 
print(df.loc['1800-6-1':'2023-6-10']) 

