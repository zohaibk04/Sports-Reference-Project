import pandas as pd
import dtale as dt
import json
import sys

# Accepting filename input from command line
args = sys.argv
if len(args) < 2:
    print("Error: Please input a filename.")
    exit()
filename = args[1]

# Trying to load in the JSON data
info = dict()
try:
    file = open(filename)
    info = json.load(file)
    file.close()
except:
    print("Error: Invalid file, please ensure you are inputting the name of a JSON file.")
    exit()

# Getting first column for the table
tm_list = []
for team in info:
    tm_list.append(team)
tm_series = pd.Series(tm_list)

# Building the rest of the table
table = {"Tm":tm_series}
for team1 in tm_list:
    losses = []
    for team2 in tm_list:
        if team1 == team2:
            losses.append("--")
        else:
            losses.append(info[team1][team2]["L"])
    table[team1] = losses
df = pd.DataFrame(table)
df.loc[len(df)] = df.columns
print(df)