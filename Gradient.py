from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import pandas as pd
import seaborn as sns

sem_grades = [[8, 3, 6, 0, 8],
              [6, 5, 4, 3, 6],
              [9, 10, 11, 11, 8],
              [9, 8, 8, 9, 3],
              [4, 8, 7, 8, 11],
              [7, 9, 11, 11],
              [6, 11, 10, 12],
              [12, 11, 11, 12],
              [12, 10, 11, 11, 12]]


Y1 = sem_grades[0] + sem_grades[1]
Y2 = sem_grades[2] + sem_grades[3]
Y3 = sem_grades[4] + sem_grades[5]
Y4 = sem_grades[6] + sem_grades[7]
Y5 = sem_grades[8]

''' ---------------------------------'''

# x = np.linspace(0, 3 * np.pi, 500)
# y = np.sin(x)
# dydx = np.cos(0.5 * (x[:-1] + x[1:]))  # first derivative

# # Create a set of line segments so that we can color them individually
# # This creates the points as a N x 1 x 2 array so that we can stack points
# # together easily to get the segments. The segments array for line collection
# # needs to be (numlines) x (points per line) x 2 (for x and y)
# points = np.array([x, y]).T.reshape(-1, 1, 2)
# segments = np.concatenate([points[:-1], points[1:]], axis=1)

# fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

# # Create a continuous norm to map from data points to colors
# norm = plt.Normalize(dydx.min(), dydx.max())
# lc = LineCollection(segments, cmap='viridis', norm=norm)
# # Set the values used for colormapping
# lc.set_array(dydx)
# lc.set_linewidth(2)
# line = axs[0].add_collection(lc)
# fig.colorbar(line, ax=axs[0])

# plt.show()

''' ----------------------- Copy-Pasting in some Grades code to test out Seaborn 'count plot' ----------------------------------------------'''

my_dict = {'First Year': [8, 3, 6, 0, 8, 6, 5, 4, 3, 6],
           'Second Year': [9, 10, 11, 11, 8, 9, 8, 8, 9, 3],
           'Third Year': [4, 8, 7, 8, 11, 7, 9, 11, 11],
           'Fourth Year': [6, 11, 10, 12, 12, 11, 11, 12],
           'Fifth Year': [12, 10, 11, 11],
           'Postbac': [12]}

grades_df = pd.DataFrame({key: pd.Series(value)
                         for key, value in my_dict.items()})

# all_avg = grades_df.mean()

# fir_avg = grades_df['First Year'].mean()
# sec_avg = grades_df['Second Year'].mean()
# thir_avg = grades_df['Third Year'].mean()
# four_avg = grades_df['Fourth Year'].mean()
# fif_avg = grades_df['Fifth Year'].mean()

# total_avg = (grades_df['First Year'].sum() + grades_df['Second Year'].sum() + grades_df['Third Year'].sum() +
#              grades_df['Fourth Year'].sum() + grades_df['Fifth Year'].sum() + grades_df['Postbac'].sum()) / 42

''' Separating the data by semester, 2D array '''
sem_grades = [[8, 3, 6, 0, 8],
              [6, 5, 4, 3, 6],
              [9, 10, 11, 11, 8],
              [9, 8, 8, 9, 3],
              [4, 8, 7, 8, 11],
              [7, 9, 11, 11],
              [6, 11, 10, 12],
              [12, 11, 11, 12],
              [12, 10, 11, 11, 12]]

sem_avgs = [np.average(sem) for sem in sem_grades]
sem_sum = [sum(grade) for grade in sem_grades]

df = pd.DataFrame(sem_grades)
print(df)

sns.countplot(df)
plt.show()
