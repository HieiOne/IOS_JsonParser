import tkinter as tk
from tkinter import filedialog #For the window
from prettytable import PrettyTable #Table
import json

TEAMS_TOTAL = [] #Full time list
TEAMS_1ST_HALF = [] #1st time list
TEAMS_2ND_HALF = [] #2nd time list
PLAYERS = [] #Full time players list

#INFO STORED:
# 0 -> name 1 -> possession | 2 -> corners | 3 -> distance covered | 4 -> offsides | 5 -> goals | 6 -> shots | 7 -> shots on goal
# 8 -> shot accuracy | 9 -> interceptions | 10 -> passes | 11 -> passes accuracy | 12 -> fouls | 13 -> y cards | 14 -> red cards | 15 -> saves

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

def statsInsert(teamName, PosTotal, JsonData, dataList):
    possession = round(JsonData[POSSESSION]/PosTotal*100,1)
    corners = JsonData[CORNERS]
    distanceCovered = round(JsonData[DISTANCE_COVERED]/1000,1)
    offsides = JsonData[OFFSIDES]
    goals = JsonData[GOALS]
    shots = JsonData[SHOTS]
    shotsOnGoal = JsonData[SHOTS_ON_GOAL]
    shotAccuracy = 0 #DEFAULT VALUE
    interceptions = JsonData[INTERCEPTIONS]
    passes = JsonData[PASSES]
    passesAccuracy = 0 #DEFAULT VALUE
    fouls = JsonData[FOULS]
    yellowCards = JsonData[YELLOW_CARDS]
    redCards = JsonData[RED_CARDS]
    saves = JsonData[KEEPER_SAVES]

    if shots >= 1:
        shotAccuracy = round(shotsOnGoal/shots*100,1)
    if passes >= 1:
        passesAccuracy = round(JsonData[PASSES_COMPLETED]/passes*100,1)

    teamList = [teamName,possession,corners,distanceCovered,offsides,goals,shots,shotsOnGoal,shotAccuracy,interceptions,passes,passesAccuracy,fouls,yellowCards,redCards,saves]
    dataList.append(teamList)

def fullTimeTeams(data):
    PosTotal = 0
    
    for item in range(len(data["matchData"]["teams"])):
        PosTotal += data["matchData"]["teams"][item]["matchTotal"]["statistics"][POSSESSION]
    
    for item in range(len(data["matchData"]["teams"])):
        JsonData = data["matchData"]["teams"][item]["matchTotal"]["statistics"]
        teamName = data["matchData"]["teams"][item]["matchTotal"]["name"]
        statsInsert(teamName,PosTotal,JsonData,TEAMS_TOTAL)

def halfTimeTeams(data):
    HALFS_LIST = [TEAMS_1ST_HALF, TEAMS_2ND_HALF]
    for half in range(len(data["matchData"]["teams"][0]["matchPeriods"])):
        PosTotal = 0
        for item in range(len(data["matchData"]["teams"])):
            PosTotal += data["matchData"]["teams"][item]["matchPeriods"][half]["statistics"][POSSESSION]
        
        for item in range(len(data["matchData"]["teams"])):
            JsonData = data["matchData"]["teams"][item]["matchPeriods"][half]["statistics"]
            teamName = data["matchData"]["teams"][item]["matchTotal"]["name"]
            statsInsert(teamName,PosTotal,JsonData,HALFS_LIST[half])

def playersFullTime(data):
    PosTotal = 0
    for player in range(len(data["matchData"]["players"])): #For every player
        for period in range(len(data["matchData"]["players"][player]["matchPeriodData"])): #And for every period
            PosTotal += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][22]
    
    JsonData = data["matchData"]["players"][player]["matchPeriodData"][period]['statistics']
    for player in range(len(data["matchData"]["players"])):
        playerName = data["matchData"]["players"][player]["info"]["name"]

        possession = 0
        corners = 0
        distanceCovered = 0
        offsides = 0
        goals = 0
        shots = 0
        shotsOnGoal = 0
        shotAccuracy = 0 #DEFAULT VALUE
        interceptions = 0
        passes = 0
        passesAccuracy = 0 # DEFAULT VALUE
        passesCompleted = 0
        fouls = 0
        yellowCards = 0
        redCards = 0
        saves = 0
        
        for period in range(len(data["matchData"]["players"][player]["matchPeriodData"])):
            possession += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][POSSESSION]
            corners += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][CORNERS]
            distanceCovered += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][DISTANCE_COVERED]
            offsides += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][OFFSIDES]
            goals += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][GOALS]
            shots += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][SHOTS]
            shotsOnGoal += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][SHOTS_ON_GOAL]
            interceptions += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][INTERCEPTIONS]
            passes += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][PASSES]
            passesCompleted += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][PASSES_COMPLETED]
            fouls += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][FOULS]
            yellowCards += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][YELLOW_CARDS]
            redCards += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][RED_CARDS]
            saves += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][KEEPER_SAVES]

        possession = round(possession/PosTotal*100,1)
        distanceCovered = round(distanceCovered/1000,1)
        if shots >= 1:
            shotAccuracy = round(shotsOnGoal/shots*100,1)
        if passes >= 1:
            passesAccuracy = round(passesCompleted/passes*100,1)
        teamList = [playerName,possession,corners,distanceCovered,offsides,goals,shots,shotsOnGoal,shotAccuracy,interceptions,passes,passesAccuracy,fouls,yellowCards,redCards,saves]
        PLAYERS.append(teamList)

def printTable(dataList):
    table = PrettyTable(['NAME', 'POS', 'CORNERS', 'D_COVERED', 'OFFSIDES', 'GOALS', 'SHOTS', 'SHOTS ON GOAL', 'SHOT  %', 'INTERCEP', 'PASSES', 'PASS %', 'FOULS', 'YELLOW', 'RED', 'SAVES'])
    for item in dataList:
        table.add_row([
            item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],
            item[8],item[9],item[10],item[11],item[12],item[13],item[14],item[15]
        ])
    print(table)

def parseJson(JsonFile): #Parsing the JSON
    with open(JsonFile) as data_file:
        data = json.load(data_file)
    fullTimeTeams(data) #Parse full time
    halfTimeTeams(data) #Parse half times
    playersFullTime(data) #Parse players
    return TEAMS_TOTAL, TEAMS_1ST_HALF, TEAMS_2ND_HALF, PLAYERS