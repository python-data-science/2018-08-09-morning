import pandas as pd
import morestats as m

df = pd.read_csv('baseball.csv')

# Find avg height, weight, age for all players using morestats

avg_height = m.mean(df.Height)
avg_weight = m.mean(df.Weight)
avg_age = m.mean(df.Age)

# Group by a team name and show mean height, weight, age
teams = df.groupby(['Team']).mean()

# Find aggregate stats for Arizona
arizona = teams.loc['ARZ']

# Find team with highest avg Height
tallest_team = teams.idxmax()['Height']

# Find a subset of the data
teams.loc['BAL':'CLE','Height':'Weight']
