# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd

df = pd.read_csv('dsp/python/football.csv') #Read the data into a pandas dataframe

df["Goal_Difference"] = df['Goals'] - df['Goals Allowed'] #Create Goal Difference column

team_index = df["Goal_Difference"].abs().idxmin() #Identify index which has smallest Goal Difference 

print df.iloc[team_index] #Index 7, Team Aston Villa has the smallest goal difference
