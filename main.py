import tkinter as tk
from tkinter import filedialog #For the window
from prettytable import PrettyTable #Table
import json
from modules import parser

def InsertIntoDB():
    print("Under Construction")

# def InfoTeams(Value):
#     with open(json_file) as data_file:
#         data = json.load(data_file)

#     POS = list(range(len(data["matchData"]["teams"]))) #To define a list of x variables
#     SHOT_ACCURACY = ''
#     PASS_ACCURACY = ''
    
#     table = PrettyTable(['NAME', 'POSSESSION', 'CORNERS', 'DISTANCE COVERED', 'OFFSIDES', 'GOALS', 'SHOTS', 'SHOTS ON GOAL', 'SHOT ACCURACY', 'INTERCEPTIONS', 'PASSES', 'PASS ACCURACY', 'FOULS', 'YELLOW CARDS', 'RED CARDS', 'SAVES'])
#     for item in range(len(data["matchData"]["teams"])):
#         #INFORMATION TO SHOW
#         if Value == 0: #Total
#             JsonData = data["matchData"]["teams"][item]["matchTotal"]["statistics"]
#             if item == 0: #Calculate possession depending on requested info
#                 POS[0] = round(data["matchData"]["teams"][item]["matchTotal"]["statistics"][22]/(data["matchData"]["teams"][item]["matchTotal"]["statistics"][22]+data["matchData"]["teams"][item+1]["matchTotal"]["statistics"][22])*100,1)
#                 POS[1] = round(100 - POS[0],1)
#         elif Value == 1: #1st Half
#             JsonData = data["matchData"]["teams"][item]["matchPeriods"][0]["statistics"]
#             if item == 0: #Calculate possession depending on requested info
#                 POS[0] = round(data["matchData"]["teams"][item]["matchPeriods"][0]["statistics"][22]/(data["matchData"]["teams"][item]["matchPeriods"][0]["statistics"][22]+data["matchData"]["teams"][item+1]["matchPeriods"][0]["statistics"][22])*100,1)
#                 POS[1] = round(100 - POS[0],1)
#         elif Value == 2: #2nd half
#             JsonData = data["matchData"]["teams"][item]["matchPeriods"][1]["statistics"]
#             if item == 0: #Calculate possession depending on requested info
#                 POS[0] = round(data["matchData"]["teams"][item]["matchPeriods"][1]["statistics"][22]/(data["matchData"]["teams"][item]["matchPeriods"][1]["statistics"][22]+data["matchData"]["teams"][item+1]["matchPeriods"][1]["statistics"][22])*100,1)
#                 POS[1] = round(100 - POS[0],1)
        
#         if JsonData[7] >= 1 and JsonData[8] >= 1:
#                 SHOT_ACCURACY = round(JsonData[8]/JsonData[7]*100,1) 
#         if JsonData[15] >= 1 and JsonData[15]>= 1:
#                 PASS_ACCURACY = round(JsonData[9]/JsonData[15]*100,1)

#         table.add_row([
#                        data["matchData"]["teams"][item]["matchTotal"]["name"], #NAME
#                     #GENERAL
#                        POS[item],    #POSSESSION
#                        JsonData[18], #CORNERS
#                        round(JsonData[23]/1000,1), #DISTANCE COVERED
#                        JsonData[11], #OFFSIDES
#                     #ATTACK
#                        JsonData[12], #GOALS
#                        JsonData[7],  #SHOTS
#                        JsonData[8],  #SHOTS ON GOAL
#                        SHOT_ACCURACY, #SHOT ACCURACY
#                     #DEFENSE
#                        JsonData[1], #INTERCEPTIONS
#                     #DISTRIBUTION
#                        JsonData[15], #PASSES
#                        PASS_ACCURACY, #PASS ACCURACY
#                     #DISCIPLINE
#                        JsonData[2], #FOULS
#                        JsonData[1], #YELLOW CARDS
#                        JsonData[0], #RED CARDS
#                     #GOALKEEPER
#                        JsonData[20] #SAVES
#                     ])
#     print(table)

# def InfoPlayers():
#     with open(json_file) as data_file:
#         data = json.load(data_file)

#     POS_TOTAL = 0
#     for item in range(len(data["matchData"]["players"])): #For every player
#         for period in range(len(data["matchData"]["players"][item]["matchPeriodData"])): #And every period it plays
#             POS_TOTAL += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][22] #We plus the possession

    
#     table = PrettyTable(['NAME', 'POSSESSION', 'CORNERS', 'DISTANCE COVERED', 'OFFSIDES', 'GOALS', 'SHOTS', 'SHOTS ON GOAL', 'SHOT ACCURACY', 'INTERCEPTIONS', 'PASSES', 'PASS ACCURACY', 'FOULS', 'YELLOW CARDS', 'RED CARDS', 'SAVES'])
#     for item in range(len(data["matchData"]["players"])): #For every player
#         POSSESSION = 0
#         CORNERS = 0
#         FREEKICKS = 0
#         OFFSIDES = 0
#         GOALS = 0
#         SHOTS = 0
#         SHOTS_ON_GOAL = 0
#         DISTANCE_COVERED = 0
#         INTERCEPTIONS = 0
#         PASSES = 0
#         COMPLETED_PASSES = 0
#         FOULS = 0
#         YELLOW_CARDS = 0
#         RED_CARDS = 0
#         SAVES = 0
#         SHOT_ACCURACY = ''
#         PASS_ACCURACY = ''
#         for period in range(len(data["matchData"]["players"][item]["matchPeriodData"])): #And every period it plays
#             POSSESSION += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][22]
#             CORNERS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][18]
#             FREEKICKS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][16]
#             OFFSIDES += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][11]
#             GOALS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][12]
#             SHOTS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][7]
#             SHOTS_ON_GOAL += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][8]
#             DISTANCE_COVERED += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][23]
#             INTERCEPTIONS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][1]
#             PASSES += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][15]
#             COMPLETED_PASSES += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][9]
#             FOULS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][2]
#             YELLOW_CARDS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][1]
#             RED_CARDS += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][0]
#             SAVES += data["matchData"]["players"][item]["matchPeriodData"][period]['statistics'][20]
        
#         if (SHOTS >= 1 and SHOTS_ON_GOAL >= 1):
#             SHOT_ACCURACY = round(SHOTS_ON_GOAL/SHOTS*100,1)   
#         if PASSES >= 1 and COMPLETED_PASSES >= 1:
#             PASS_ACCURACY = round(COMPLETED_PASSES/PASSES*100,1)
            

#         table.add_row([
#                        data["matchData"]["players"][item]["info"]["name"], #NAME
#                     #GENERAL
#                        round(POSSESSION/POS_TOTAL*100,1),    #POSSESSION
#                        CORNERS, #CORNERS
#                        round(DISTANCE_COVERED/1000,1), #DISTANCE COVERED
#                        OFFSIDES, #OFFSIDES
#                     #ATTACK
#                        GOALS, #GOALS
#                        SHOTS,  #SHOTS
#                        SHOTS_ON_GOAL,  #SHOTS ON GOAL
#                        SHOT_ACCURACY,  #SHOT ACCURACY
#                     #DEFENSE
#                        INTERCEPTIONS, #INTERCEPTIONS
#                     #DISTRIBUTION
#                        PASSES, #PASSES
#                        PASS_ACCURACY, #PASSES ACCURACY
#                     #DISCIPLINE
#                        FOULS, #FOULS
#                        YELLOW_CARDS, #YELLOW CARDS
#                        RED_CARDS,  #RED CARDS
#                     #GOALKEEPER
#                         SAVES   #SAVES
#                     ])
#     print(table)

def parseMenu():
    choice = '0'
    while choice == '0': # Simple Menu
        print("")
        print("-------- SUBMENU ---------")
        print("1.- Show total info of teams")
        print("2.- Show first half of teams")
        print("3.- Show second half of teams")
        print("4.- Show total info of every player in the game")
        print("5.- Exit Submenu")
        print("")
        choice = input("So what is it gonna be? ")

        if choice == '1': #Show total info of teams
            TEST = parser.parseJson
            print(TEST)
        elif choice == '2': #Show first half of teams
            parser.parseJson
        elif choice == '3': #Show second half of teams
            parser.parseJson
        elif choice == '4': #Show total info of every player in the game
            parser.parseJson
        elif choice == '5': #Exits submenu
            break
        else:
            print("Sorry I didn't get what you wanted to do?")
        choice = '0' #Only way of exiting this loop is manually

def main():
    choice = '0'
    while choice == '0': # Simple Menu
        print("")
        print("---------- MENU -----------")
        print("1.- Insert JSON file into DB (It will ask for JSON file path)")
        print("2.- Check JSON data (It will ask for JSON file path)")
        print("3.- Exit")
        print("")
        choice = input("So what is it gonna be? ")

        if choice == '1': #Inserts data into the DB
            #getJsonFile()
            InsertIntoDB()
        elif choice == '2': #Shows parsed data
            parser.filedialog
            parseMenu()
        elif choice == '3': #Exits
            print("Goodbye..")
            break
        else:
            print("Sorry I didn't get what you wanted to do?")
        choice = '0' #Only way of exiting this loop is manually


if __name__ == '__main__':
    main()