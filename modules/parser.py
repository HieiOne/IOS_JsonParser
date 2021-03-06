import tkinter as tk
from tkinter import filedialog #For the window
from prettytable import PrettyTable #Table
import json

TEAMS_TOTAL = [] #Full time list
PLAYERS_HOME = [] #Home players 
PLAYERS_AWAY = [] #Away players
TEAMS_1ST_HALF = [] #1st time list
TEAMS_2ND_HALF = [] #2nd time list
EVENTS = [] #Events list
HOME_TEAM = '' #Contains name of home team
AWAY_TEAM = '' #Contains name of away team
PLAYERS_WITH_ID = [] #Contains every player with its name and ID

#INFO STORED:
#name | possession | goals | assist |shots | shots ot | corners | offsides | passes | pass % | passes completion | interceptions | saves | fouls | yellow | red | distance

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
    #For every time we ask for a JSON we empty the lists
    del TEAMS_TOTAL[:]
    del PLAYERS_HOME[:]
    del PLAYERS_AWAY[:]
    del TEAMS_1ST_HALF[:]
    del TEAMS_2ND_HALF[:]
    del EVENTS[:]
    del PLAYERS_WITH_ID[:]

    window = tk.Tk()
    window.withdraw()
    file_path = filedialog.askopenfilename(filetypes = (("JSON files", "*.json"),("All files", "*.*") )) #Window and the extensions for an easier search
    return file_path #We return the file path

def checkPlayer(STEAMID):
    for player in PLAYERS_WITH_ID:
        if player[0] == STEAMID:
            return player[1] #We return the name
            

def parseEvents(data):
    for event in range(len(data["matchData"]["matchEvents"])):
        second = data["matchData"]["matchEvents"][event]["second"]
        eventType = data["matchData"]["matchEvents"][event]["event"]
        team = data["matchData"]["matchEvents"][event]["team"]
        player_1 = data["matchData"]["matchEvents"][event]["player1SteamId"]
        player_2 = data["matchData"]["matchEvents"][event]["player2SteamId"]
        
        if (eventType != "(null)"):
            eventList = [second,eventType,team,player_1,player_2]
            EVENTS.append(eventList)

def statsInsert(teamName, PosTotal, JsonData, dataList):
    possession = round(JsonData[POSSESSION]/PosTotal*100,1)
    position = "X"
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
    passesCompleted = JsonData[PASSES_COMPLETED]
    fouls = JsonData[FOULS]
    yellowCards = JsonData[YELLOW_CARDS]
    redCards = JsonData[RED_CARDS]
    saves = JsonData[KEEPER_SAVES]
    assist = JsonData[ASSISTS]
    owngoals = JsonData[OWNGOALS]

    if shots >= 1:
        shotAccuracy = round(shotsOnGoal/shots*100,1)
    if passes >= 1:
        passesAccuracy = round(JsonData[PASSES_COMPLETED]/passes*100,1)

    teamList = [teamName,str(possession)+"%",goals,assist,shots,shotsOnGoal,corners,offsides,passes,str(passesAccuracy)+"%",interceptions,saves,fouls,yellowCards,redCards,distanceCovered,owngoals,position]
    dataList.append(teamList)

def fullTimeTeams(data): #INCLUDES OG
    PosTotal = 0
    
    for item in range(len(data["matchData"]["teams"])):
        PosTotal += data["matchData"]["teams"][item]["matchTotal"]["statistics"][POSSESSION]
    
    for item in range(len(data["matchData"]["teams"])):
        JsonData = data["matchData"]["teams"][item]["matchTotal"]["statistics"]
        teamName = data["matchData"]["teams"][item]["matchTotal"]["name"]
        statsInsert(teamName,PosTotal,JsonData,TEAMS_TOTAL)

def halfTimeTeams(data): #INCLUDES OG
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
    
    for player in range(len(data["matchData"]["players"])):
        playerId = data["matchData"]["players"][player]["info"]["steamId"]       
        playerName = data["matchData"]["players"][player]["info"]["name"]
        
        if data["matchData"]["players"][player]["matchPeriodData"]:
            team = data["matchData"]["players"][player]["matchPeriodData"][0]["info"]["team"]
            #position = "X"
            position = data["matchData"]["players"][player]["matchPeriodData"][0]["info"]["position"]
            possession = 0
            corners = 0
            distanceCovered = 0
            offsides = 0
            goals = 0
            assist = 0
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
            owngoals = 0
            
            for period in range(len(data["matchData"]["players"][player]["matchPeriodData"])):
                possession += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][POSSESSION]
                corners += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][CORNERS]
                distanceCovered += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][DISTANCE_COVERED]
                offsides += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][OFFSIDES]
                goals += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][GOALS]
                assist += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][ASSISTS]
                shots += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][SHOTS]
                shotsOnGoal += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][SHOTS_ON_GOAL]
                interceptions += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][INTERCEPTIONS]
                passes += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][PASSES]
                passesCompleted += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][PASSES_COMPLETED]
                fouls += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][FOULS]
                yellowCards += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][YELLOW_CARDS]
                redCards += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][RED_CARDS]
                saves += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][KEEPER_SAVES]
                owngoals += data["matchData"]["players"][player]["matchPeriodData"][period]['statistics'][OWNGOALS]

            possession = round(possession/PosTotal*100,1)
            distanceCovered = round(distanceCovered/1000,1)
            if shots >= 1:
                shotAccuracy = round(shotsOnGoal/shots*100,1)
            if passes >= 1:
                passesAccuracy = round(passesCompleted/passes*100,1)
            
            teamList = [playerName,str(possession)+"%",goals,assist,shots,shotsOnGoal,corners,offsides,passes,str(passesAccuracy)+"%",interceptions,saves,fouls,yellowCards,redCards,distanceCovered,owngoals,position]
            if team == 'home':
                PLAYERS_HOME.append(teamList)
            else:
                PLAYERS_AWAY.append(teamList)
            
            playerList = [playerId,playerName]
            PLAYERS_WITH_ID.append(playerList) #We append to the players info list
                

def printTable(dataList,dataList_2='Empty'):
    table = PrettyTable(['NAME','POS', 'GOALS','ASSISTS', 'SHOTS', 'SHOTS OT', 'CORNERS', 'OFFSIDES', 'PASSES', 'PASS %', 'INTERCEP', 'SAVES', 'FOULS', 'YELLOW', 'RED', 'DISTANCE','OG','POSITION'])
    for item in dataList:
        table.add_row([
            item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],
            item[8],item[9],item[10],item[11],item[12],item[13],item[14],str(item[15]) + " km",item[16],item[17]
        ])
    if dataList_2 != 'Empty':
        for item in dataList_2:
            table.add_row([
                item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],
                item[8],item[9],item[10],item[11],item[12],item[13],item[14],str(item[15]) + " km",item[16],item[17]
            ])
    print(table)

def printEvents(dataList):
    table = PrettyTable(['EVENT', 'MINUTE', 'TEAM', 'Player 1', 'Player 2'])
    for item in dataList:
        if item[2] == "home":
            team = HOME_TEAM
        else:
            team = AWAY_TEAM

        player1 = checkPlayer(item[3])
        player2 = checkPlayer(item[4])
        table.add_row([
            item[1],round(item[0]/60),team,player1,player2
        ])
    print(table)

def parseJson(JsonFile): #Parsing the JSON
    with open(JsonFile) as data_file:
        data = json.load(data_file)
    fullTimeTeams(data) #Parse full time
    halfTimeTeams(data) #Parse half times
    playersFullTime(data) #Parse players
    parseEvents(data) #Parse events
    global HOME_TEAM ; HOME_TEAM = data["matchData"]["teams"][0]["matchTotal"]["name"] #Getting HOME TEAM name
    global AWAY_TEAM ; AWAY_TEAM = data["matchData"]["teams"][1]["matchTotal"]["name"] #Getting AWAY TEAM name
    return TEAMS_TOTAL, TEAMS_1ST_HALF, TEAMS_2ND_HALF, PLAYERS_HOME, PLAYERS_AWAY, EVENTS