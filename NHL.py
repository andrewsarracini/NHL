from operator import index
from turtle import color, home
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
import matplotlib.image as mpimg

game_df = pd.read_csv('game.csv')
 
home_outcomes = game_df[['home_team_id', 'outcome', 'date_time_GMT']].copy()


city_alt = { 
                1:250, # New Jersey 
                2:89, # NY Islanders 
                3:13, # NY Rangers 
                4:39, # Philly 
                5:846, # Pitsburgh
                6:33, # Boston 
                7:597, # Buffalo
                8:52, # Montreal
                9:236, # Ottawa
                10:289, # Toronto
                11:997, # Atlanta
                12:354, # Carolina
                13:3, # Florida
                14:7, # Tampa
                15:10, # Washington
                16:594, # Chicago
                17:610, # Detroit 
                18:607, # Nashville
                19:883, # St.Louis
                20:3432, # Calgary 
                21:5272, # Colorado
                22:2172, # Edmonton
                23:20, # Vancouver 
                24:3694, # Anaheim
                25:435, # Dallas
                26:243, # Los Angeles
                27:1093, # Phoenix --- Note: Phoenix = Arizona! 
                28:92, # San Jose 
                29:755, # Colombus
                30:791, # Minnesota
                52:305, # Winnipeg
                53:1093, # Arizona --- Note: Arizona = Phoneix! 
                54:2064, # Vegas 
                87:0, # TBD, All-Star Game, maybe? 
                89:0, # TBD, All-Star Game, maybe? 
                90:0 # TBD, All-Star Game, maybe? 
                }   

id_team = {
                1:'New Jersey',
                2:'New York Long Island',
                3: 'New York',
                4: 'Philidelphia', 
                5: 'Pitsburgh', 
                6: 'Boston', 
                7: 'Buffalo', 
                8: 'Montreal',
                9: 'Ottawa',
                10: 'Toronto',
                11: 'Atlanta',
                12: 'Carolina',
                13: 'Florida',
                14: 'Tampa Bay', 
                15: 'Washington',
                16: 'Chicago', 
                17: 'Detroit', 
                18: 'Nashville',
                19: 'St.Louis',
                20: 'Calgary', 
                21: 'Colorado', 
                22: 'Edmonton',
                23: 'Vancouver', 
                24: 'Anaheim',
                25: 'Dallas', 
                26: 'Los Angles', 
                27: 'Phoenix', 
                28: 'San Jose', 
                29: 'Colombus', 
                30: 'Minessota', 
                52: 'Winnipeg', 
                53: 'Arizona', 
                54: 'Vegas', 
                87: 'All-Star Game1?',
                89: 'All-Star Game2?', 
                90: 'All-Star Game3?' 
                }

home_total_pct = { 
                'New Jersey': 55.595, 
                'New York Long Island': 50.526,
                'New York': 52.463,
                'Philidelphia' : 55.595, 
                'Pitsburgh' : 58.683, 
                'Boston' : 57.812, 
                'Buffalo' : 51.100, 
                'Montreal' : 53.059, 
                'Ottawa' : 54.350, 
                'Toronto' : 52.587, 
                'Atlanta' : 44.961, 
                'Carolina' : 52.934, 
                'Florida' : 46.764, 
                'Tampa Bay' : 58.983, 
                'Washington' : 59.159, 
                'Chicago' : 55.517, 
                'Detroit' : 56.973, 
                'Nashville' : 58.382, 
                'St. Louis' : 57.614, 
                'Calgary' : 54.933, 
                'Colorado' : 55.357, 
                'Edmonton' : 48.230,
                'Vancouver' : 56.316, 
                'Anaheim' : 57.008, 
                'Dallas' : 58.519, 
                'Boston' : 57.812, 
                'Los Angles' : 53.974, 
                'Phoenix' : 52.579, 
                'San Jose' : 59.977, 
                'Colombus' : 51.188, 
                'Minessota' : 54.644, 
                'Winnipeg' : 54.586, 
                'Arizona' : 45.938, 
                'Vegas' : 62.128, 
                'All-Star Game1?' : 0,
                'All-Star Game2?' : 0, 
                'All-Star Game3?' : 0
                }


''' This one works! '''
home_outcomes['altitude'] = home_outcomes['home_team_id'].map(city_alt).fillna(0)

home_outcomes['team_name'] = home_outcomes['home_team_id'].map(id_team).fillna('N/A') 

home_outcomes['home_win_pct'] = home_outcomes['team_name'].map(home_total_pct).fillna(0)


# this creates a series of team names
teams_ser = home_outcomes['team_name'].drop_duplicates()
# print(len(teams_ser))

teams = home_outcomes.groupby('team_name')['team_name'].nunique() 
# print(teams) 

record = home_outcomes.loc[home_outcomes['team_name'] == 'All-Star Game?'] 

# set index of dataframe: 
home_outcomes.set_index('team_name', inplace = True)

record = home_outcomes.loc['Toronto']

''' Making a new Dataframe, called condensed_outcomes'''
# on second thought, use a dict (seen in the documentation) and then .to_frame, should be easier that way 
condensed_outcomes = pd.DataFrame({'teams': ['New Jersey', 'New York Long Island','New York',
                                            'Philidelphia', 'Pitsburgh', 'Boston', 'Buffalo', 
                                            'Montreal','Ottawa','Toronto','Atlanta','Carolina',
                                            'Florida','Tampa Bay', 'Washington','Chicago', 'Detroit', 
                                            'Nashville','St.Louis','Calgary', 'Colorado', 'Edmonton',
                                            'Vancouver', 'Anaheim','Dallas', 'Los Angles', 'Phoenix', 
                                            'San Jose', 'Colombus', 'Minessota', 'Winnipeg', 'Arizona', 
                                            'Vegas'],
                                    
                                    'alt': [250, 89, 13, 39, 846, 33, 597, 52, 236, 289, 997, 354, 3, 7, 10, 
                                            594, 610, 607, 883, 3432, 5272, 2172, 20, 3694, 435, 243, 1093, 
                                            92, 755, 791, 305, 1093, 2064], 
                                    
                                    'win_percent' : [55.595, 50.526, 52.463, 55.595, 58.683, 57.812, 51.100, 
                                                    53.059, 54.350, 52.587, 44.961, 52.934, 46.764, 58.983, 
                                                    59.159, 55.517, 56.973, 58.382, 57.614, 54.933, 55.357, 
                                                    48.230, 56.316, 57.008, 58.519, 53.974, 52.579, 59.977,
                                                     51.188, 54.644, 54.586, 45.938, 62.128],

                                    'images' : ['New_Jersey.png','Islanders.png', 'New York.png', 'Philly.png', 'Pitsburgh.png', 
                                            'Boston.png',  'Buffalo.png', 'Montreal.png', 'Ottawa.png', 'Toronto.png', 'Atlanta.png', 
                                            'Carolina.png', 'Florida.png', 'Tampa Bay.png', 'Washington.png',  'Chicago.png', 
                                            'Detroit.png', 'Nashville.png', 'St.Louis.png', 'Calgary.png', 'Colorado.png', 
                                            'Edmonton.png', 'Vancouver.png', 'Anaheim.png', 'Dallas.png', 'LA.png', 'Phoenix.png', 
                                            'San Jose.png', 'Colombus.png', 'Minnesota.png', 'Winnipeg.png', 'Arizona.png', 'Vegas.png']
                                    }) 

condensed_outcomes.set_index('teams' , inplace = True)

# color_dict = {
#     'New Jersey':'red', 'New York Long Island':'orange', 'New York':'powderblue', 'Philidelphia':'sandybrown', 'Pitsburgh':'darkgoldenrod', 'Boston':'gold',
#     'Buffalo':'darkgray', 'Montreal':'dodgerblue', 'Ottawa':'tomato', 'Toronto':'blue', 'Atlanta':'bisque', 'Carolina':'orangered', 'Florida':'wheat', 
#     'Tampa Bay':'slategrey', 'Washington':'maroon', 'Chicago':'black', 'Detroit':'crimson', 'Nashville':'yellow', 'St.Louis':'silver', 'Calgary': 'firebrick', 
#     'Colorado':'purple', 'Edmonton':'darkblue', 'Vancouver':'teal', 'Anaheim':'peru', 'Dallas':'lime', 'Los Angles':'gainsboro', 'Phoenix':'saddlebrown', 
#     'San Jose':'lightseagreen', 'Colombus':'navy', 'Minessota':'darkgreen', 'Winnipeg':'indigo', 'Arizona':'chocolate', 'Vegas':'goldenrod'
#     }

# color2 = [
#     'red', 'orange', 'powderblue', 'sandybrown', 'darkgoldenrod','gold','darkgray', 'dodgerblue', 'tomato', 'blue', 'bisque', 'orangered', 'wheat', 
#     'slategrey', 'maroon', 'black', 'crimson', 'yellow', 'silver', 'firebrick', 'purple', 'darkblue', 'teal', 'peru', 'lime', 'gainsboro', 'saddlebrown', 
#     'lightseagreen', 'navy', 'darkgreen', 'indigo', 'chocolate', 'goldenrod'
#     ]   

# ''' ---'''
''' Most successful model so far'''
# # creating a scatter plot -- build on this to make more elaborate plots 
# fig, ax = plt.subplots() 
# x = condensed_outcomes['alt'] 
# y = condensed_outcomes['win_percent']
# color = [color_dict[i] for i in condensed_outcomes.index]

# scattery = ax.scatter(x, y, c = color, cmap = color2) 

# # creating a trendline for the scatter plot and printing the equation 
# z = np.polyfit(x, y, 1) 
# p = np.poly1d(z) 
# plt.plot(x,p(x),'r--')
# print("Trend Line Equation y=%.6fx+(%.6f)"%(z[0],z[1]))

# plt.xticks(rotation = 90) 
# plt.title('Altitude vs Home Win Percentage for each NHL team')
# ax.set_ylabel('Win Percentage')
# ax.set_xlabel('Altitudes') 
# plt.legend(handles = scattery.legend_elements()[0], labels = labels1) 
# plt.show() 


''' creates a scatter plot that has 26000 + points, Legend still does not work properly'''
# fig, ax = plt.subplots()
# x = home_outcomes['altitude']
# y = home_outcomes['home_win_pct']

# scatters = plt.scatter(x, y, c = home_outcomes['home_team_id']) 
# plt.legend(handles = scatters.legend_elements()[0]) 
# plt.show()


''' Testing out a different way to get 34 different colours into my scatter plot and legend'''
# x = condensed_outcomes['alt']
# y = condensed_outcomes['win_percent'] 
# new_list = [] 
# for i in range(1000): 
#     r = np.random.randint(1,34)
#     if r not in new_list:
#         new_list.append(r) 

# fig, ax = plt.subplots()
# scatter = ax.scatter(x, y, c = new_list) 

# legend1 = ax.legend( * scatter.legend_elements(), title = 'NHL Teams')
# ax.add_artist(legend1) 

# plt.show() 

''' Toronto Maple Leafs Win Percentage over time '''

# Limiting the unecessary columns in this new df 
date_outcomes = home_outcomes.drop(columns=['altitude', 'home_win_pct', 'home_team_id']).copy() 

# Selecting all games Toronto played from within date_outcomes, called toronto_outcomes
toronto_outcomes = date_outcomes.loc['Toronto'].copy() 


# Setting up to have short_date as the index (to easily access season-specific dates) 
toronto_outcomes['long_date']= pd.to_datetime(toronto_outcomes['date_time_GMT'])

# Cutting down the date time to year-month-day. The extra hourly data was messing with the 'date':'date' method! 
toronto_outcomes['short_date'] = toronto_outcomes['long_date'].dt.date

# Dropping the extra date columns that are no longer needed 
toronto_short = toronto_outcomes.drop(columns=['date_time_GMT', 'long_date']).copy()

# Reset the current index, and setting the new index to be short_date
toronto_short = toronto_short.reset_index().copy() 
toronto_short['short_date'] = pd.to_datetime(toronto_short['short_date']) 
toronto_short.set_index('short_date', inplace=True)


# Sorting the values by date, called toronto_sorted
''' This shows the DatetimeIndex is functioning as expected! It's dtype is 'datetime64[ns]' '''
# print(toronto_short.index.dtype) 
 
''' This FINALLY works! Sorted list of all dates from earliest to latest, for any specified team!''' 
toronto_short.sort_index(inplace=True, ascending=True)
print(toronto_short) 


print(len(toronto_short.loc['2012-1-19' : '2013-6-24']))

''' There is a MYSTERY to solve here, the repeating 41 games is not a fluke '''
''' Either it indicates that this data is ONLY from the Regular Season, or just a COINCIDENCE '''
''' There IS NO SUCH THING as A COINCIDENCE! '''
# Year by Year Games Recorded: # 
# - 2000-10-4 - 2001-6-9: 41 games -- Lost in semis 
# - 2001-10-3 - 2002-6-13: 41 games
# - 2002-10-9 - 2003-6-9: 41 games
# - 2003-10-8 - 2004-6-7: 41 games
# - 2004 - 2005: 0 games (NHL Lockout)
# - 2005-10-5 - 2006-6-19: 41 games 
# - 2006-10-4 - 2007-6-6: 41 games 
# - 2007-9-29 - 2008-6-4: 41 games 
# - 2008-10-4 - 2009-6-12: 41 games 
# - 2009 - 2010: 44 games 
# - 2010 - 2011: 41 games 
# - 2011 - 2012: 38 games 
# - 2012-1-19 - 2013-6-24: 45 games (playoff run)









'''------------------------------------------------------------------------------------------------------------'''

''' Helpful Video, "Pandas Conditional Columns: Set Pandas Conditional Columns Based on Values of Another Column" '''
# df = pd.DataFrame.from_dict(
#     {
#         'Name':['Kate', 'Melissa', 'John', 'Matt'],
#         'Age': [33, 45, 35, 64],
#         'Birth City':['London', 'Paris', 'Toronto', 'Atlanta'],
#         'Gender':['F', 'F', 'M', 'M'] 
#     }
# ) 

# conditions = [
#     (df['Age'] < 30),
#     (df['Age'] >= 30) & (df['Age'] < 40), 
#     (df['Age'] >= 40) & (df['Age'] < 50),
#     (df['Age'] >= 50) & (df['Age'] < 60),
#     (df['Age'] > 60)
# ] 


''' USEFUL NP.SELECT! '''
# values = ['< 30 Years Old', '30-39 Years Old', '40-49 Years Old', '50-59 Years Old', '> 60 Years Old']

# df['Age Group'] = np.select(conditions, values)

# print(df)  


''' VERY USEFUL .MAP, good for applying dictionaries to dfs!'''
# city_countries = {'London':'England', 'Paris':'France', 'Atlanta':'USA'} 

# df['Birth Countries'] = df['Birth City'].map(city_countries).fillna('Other') 

# print(df)

''' USEFUL application of .apply(), pass in functions to dfs!'''
# df['Name Length'] = df['Name'].apply(len)
# print(df)  


''' Another example of the power of .apply() -- should note that this can cause performance issues with large datasets'''
# def age_group(x): 
#     if x < 30: 
#         return '> 30 years old'
#     elif x < 40: 
#         return '30 - 39 years old'
#     elif x < 50: 
#         return '40 - 49 years old'
#     elif x < 60:
#         return '50-59 years old'
#     elif x > 60: 
#         return '> 60 years old'

# df['Age Cat'] = df['Age'].apply(age_group) 
# print(df) 