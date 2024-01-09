# Sports-Reference-Project
Python script for reading in JSON files with win/loss data and displaying it as a head-to-head chart. Solving the Sports Reference 2024 - Summer Engineering Internship prompt.

## Setup
(Python 3 REQUIRED)
To setup this project, either clone the repository to your computer or download this project'smain.py file. Then, make sure you have installed the proper packages as outlined in requirements.py

## Running
Open a terminal window and navigate to the directory that the project/main.py is located in, then enter the following commands accordingly with your operating system:

> python3 main.py PATH/TO/filename.json

A window should popup and display the graph that corresponds to the data that is inputted

## Explanation
This project works by first reading the JSON file into a Python dictionary, then compiling an initial list of teams from the keys. Using this list, the script then parses the dictionary to find the losses each team has against every other team, building the table column by column. This is then converted to a Pandas DataFrame, which is used to create a matplotlib table figure that can be better styled to fit the table style from Sports Reference. Finally, plt.show() is used to display the figure as a popup.