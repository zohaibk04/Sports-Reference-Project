import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
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

# Setting up the figure and axis to display the table
figure, axis = plt.subplots()
figure.patch.set_visible(False)
axis.axis('off')
axis.axis('tight')

# Getting the column header/cell colors depending on the row
cell_colors = [['white' for _ in range(len(df.columns))]] * len(df)
col_colors = ['#eeeeee' for _ in range(len(df.columns))]
for i in range(len(df)):
    if i in range(len(df)-1):
        cell_colors[i] = ['white' for _ in df.iloc[i]]
    else:
        cell_colors[i] = ['#eeeeee' for _ in df.iloc[i]]

# Creating the table and configuring the text style based on row
table = axis.table(cellText=df.values, cellLoc='center', colLabels=df.columns, cellColours=cell_colors, loc='center', colColours=col_colors)
for (row, col), cell in table.get_celld().items():
    if (row == 0):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))
        cell.get_text().set_color('#990609')
    elif (row == len(df)):
        cell.set_text_props(fontproperties=FontProperties(weight='bold'))

# Used to make the table size correspond to cell content
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(df.columns))))

# Displaying the table in a popup window
figure.tight_layout()
plt.show()