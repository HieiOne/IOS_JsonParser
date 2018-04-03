#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog #For the window
from prettytable import PrettyTable #Table
import json

TEAMS_TOTAL = [] #Full time list
TEAMS_1ST_HALF = [] #1st time list
TEAMS_2ND_HALF = [] #2nd time list
PLAYERS = [] #Full time players list

#STATISTICS TYPES
RED_CARDS = 0
YELLOW_CARDS = 1
FOULS = 2
FOULS_SUFFERED = 3
SLIDING_TACKLES = 4
SLIDING_TACKLES_COMPLETED = 5
GOALS_CONCEDED = 6
SHOTS = 7
SHOTS_ON_GOAL = 8
PASSES_COMPLETED = 9
INTERCEPTIONS = 10
OFFSIDES = 11
GOALS = 12
OWNGOALS = 13
ASSISTS = 14
PASSES = 15
FREEKICKS = 16
PENALTIES = 17
CORNERS = 18
THROW_INS = 19
KEEPER_SAVES = 20
GOAL_KICKS = 21
POSSESSION = 22
DISTANCE_COVERED = 23
KEEPER_SAVES_CAUGHT = 24

def getJsonFile(): #Simple function to ask the user where the JSON file at
    window = tk.Tk()
    window.withdraw()
    file_path = filedialog.askopenfilename(filetypes = (("JSON files", "*.json"),("All files", "*.*") )) #Window and the extensions for an easier search
    return file_path #We return the file path

def parseJson(JsonFile): #Parsing the JSON
    with open(JsonFile) as data_file:
        data = json.load(data_file)
    fullTimeTeams(data)

def fullTimeTeams(data):
    PosTotal = 0

    for item in range(len(data["matchData"]["teams"])):
        PosTotal += data["matchData"]["teams"][item]["matchTotal"]["statistics"][POSSESSION]
    
    for item in range(len(data["matchData"]["teams"])):
        JsonData = data["matchData"]["teams"][item]["matchTotal"]["statistics"]
        
        #MAYBE I COULD PUT THIS ALL IN A METHOD
        teamName = data["matchData"]["teams"][item]["matchTotal"]["name"]
        possession = round(JsonData[POSSESSION]/PosTotal*100,1)
        corners = JsonData[CORNERS]
        distanceCovered = round(JsonData[DISTANCE_COVERED]/1000,1)
        offsides = JsonData[OFFSIDES]
        goals = JsonData[GOALS]
        shots = JsonData[SHOTS]
        shotsOnGoal = JsonData[SHOTS_ON_GOAL]
        shotAccuracy = 1 #TODO
        interceptions = JsonData[INTERCEPTIONS]
        passes = JsonData[PASSES]
        passesAccuracy = 1 #TODO
        fouls = JsonData[FOULS]
        yellowCards = JsonData[YELLOW_CARDS]
        redCards = JsonData[RED_CARDS]
        saves = JsonData[KEEPER_SAVES]

        teamList = [teamName,possession,corners,distanceCovered,offsides,goals,shots,shotsOnGoal,shotAccuracy,interceptions,passes,passesAccuracy,fouls,yellowCards,redCards,saves]
        TEAMS_TOTAL.append(teamList)
    


#JsonFile = getJsonFile()
JsonFile = 'd:/REPOSITORY/IOS_JsonParser/2018.03.20_20h.42m.07s_nextgen-vs-phoenix_5-1.json'
#JsonFile = 'd:/REPOSITORY/IOS_JsonParser/2018.04.02_16h.19m.43s_phoenix-vs-nextgen_0-2.json'
parseJson(JsonFile)
