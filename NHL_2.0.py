import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Dictionaries
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def read_clean(csv):
    # reads in a .csv file into a df called game_df
    game_df = pd.read_csv(csv)

    # filter game_df to limit it to 3 columns, becoming 'cleaned'
    cleaned = game_df[['home_team_id', 'outcome', 'date_time_GMT']].copy()

    # add two columns to cleaned called 'altitude' and 'team_name', both mapping to team id
    cleaned['altitude'] = cleaned['home_team_id'].map(
        Dictionaries.city_alt).fillna('Other')
    cleaned['team_name'] = cleaned['home_team_id'].map(
        Dictionaries.id_team).fillna('Other')

    # add new column to cleaned called 'home_win_pct' -- contains total home win percentage over 5 seasons
    cleaned['home_total_pct'] = cleaned['team_name'].map(
        Dictionaries.home_total_pct).fillna('N/A')

    # Note: home_total_pct is NOT useful for determining home record season by season! This requires a different function.
    return cleaned

 # creating a new condensed dataframe, containing only 3 columns and 33 rows

# Input the team name, and gain access to their reccord, win_pct is an int
# Future idea: pass all the team names into record_finder, then use the output to populate the corresponding rows in the new column


def record_finder(name):
    record = home_outcomes.loc[home_outcomes['team_name'] == name]

    # determines total home wins
    home_wins = record.loc[record['outcome'].isin(
        ['home win REG', 'home win OT'])].shape[0]

    # determines total home losses (counted as away wins)
    home_losses = record.loc[record['outcome'].isin(
        ['away win REG', 'away win OT'])].shape[0]

    # now find the total home win percentage
    win_pct = round((home_wins / (home_wins + home_losses) * 100), 3)

    return win_pct

# Setup for images in the Scatter Plot


def get_image(path, zoom=0.02):
    return OffsetImage(plt.imread(path), zoom=zoom)


# Create a scatter plot comparing alt and win percentage, using team logos in place of points
def make_scatter(x, y, xlab, ylab, images):

    # setting up the scatter plot, passing in x and y
    fig, ax = plt.subplots()
    scattery = plt.scatter(x, y)

    # Connects coordinates on the plot to a given image, in this case -- the appropriate team logo from the images column
    for x_alt, y_win, image in zip(x, y, images):
        ab = AnnotationBbox(get_image(image), (x_alt, y_win), frameon=False)
        ax.add_artist(ab)

    # Creating a trendline for the scatter plot and printing the equation
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), 'r--')
    print("Trend Line Equation y=%.6fx+(%.6f)" % (z[0], z[1]))

    # Title, labels for x and y axes and gridlines
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title('Altitude vs Home Win Percentage for NHL Teams')

    # plt.show()

    return scattery


# main()
home_outcomes = read_clean('game.csv')

team_record = record_finder('Toronto')

# Establishing condensed_outcomes outside the scope of functions
condensed_outcomes = Dictionaries.condensed_outcomes

scatter_plot = make_scatter(
    condensed_outcomes['alt'], condensed_outcomes['win_percent'], 'Altitude (ft.)', 'Home Win Percentage', condensed_outcomes['images'])

imager = get_image(condensed_outcomes['images'], 0.02)
