#!/usr/bin/env python

"""JsonParser - Parses IOS Json file to a more understandable format and easier display of them"""

__author__ = "Hiei"
__copyright__ = "No copyright, just share the author"
__version__ = "1.2.2"
__maintainer__ = "Hiei"

import tkinter as tk
from tkinter import filedialog #For the window
import json
import csv
import os
import ntpath
import signal
from modules import prettytable # Table
from modules import parser

def IgnoreKeyboardInterrupt():
    return signal.signal(signal.SIGINT,signal.SIG_IGN)


def InsertIntoDB():
    print("Under Construction")

def ExportToCSV(id,JsonFile,*argv):
    FOLDER = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents\\IOS_CSV_PARSEDFILES')
    
    if not os.path.exists(FOLDER):
        os.mkdir(FOLDER)

    FILE_NAME = ["TotalTeams","FirstHalfTeams","SecondHalfTeams","HomePlayers","AwayPlayers","TotalPlayers"]
    FULL_NAME = os.path.basename(JsonFile)
    (NAME,ext) = os.path.splitext(FULL_NAME)

    CSV_FILE = FOLDER+"\\"+NAME+"-"+FILE_NAME[id]+".csv"
    
    STATS_DISPLAY = [["Player", "Poss (%)", "Goals","Assists", "Shots", "Shots OT", "Corners", "Offsides", "Passes", "Pass (%)", "IC", "Saves", "Fouls", "YC", "RC", "Dist (km)","OG"]] #EFA FORMAT
    with open(CSV_FILE, 'w') as filename:
        writer = csv.writer(filename, lineterminator='\n')

        writer.writerows(STATS_DISPLAY)
        for arg in argv:
            writer.writerows(arg)

def ExportSubmenu(JsonFile, TEAMS_TOTAL, TEAMS_1ST_HALF, TEAMS_2ND_HALF, PLAYERS_HOME, PLAYERS_AWAY, EVENTS):
    choice = '0'
    while choice == '0': # Simple Menu
        try:
            print("-------- EXPORT MENU ---------")
            print("1.- EXPORT total info of teams")
            print("2.- EXPORT first half of teams")
            print("3.- EXPORT second half of teams")
            print("4.- EXPORT HOME team players stats")
            print("5.- EXPORT AWAY team players stats")
            print("6.- EXPORT total info of every player in the game")
            print("7.- Exit Submenu")
            print("")
            choice = input("So what is it gonna be? ")

            if choice == '1': #Exports total info of teams
                ExportToCSV(0,JsonFile,TEAMS_TOTAL)
            elif choice == '2': #Exports first half of teams
                ExportToCSV(1,JsonFile,TEAMS_1ST_HALF)
            elif choice == '3': #Exports second half of teams
                ExportToCSV(2,JsonFile,TEAMS_2ND_HALF)
            elif choice == '4': #Exports HOME team players stats
                ExportToCSV(3,JsonFile,PLAYERS_HOME)
            elif choice == '5': #Exports AWAY team players stats
                ExportToCSV(4,JsonFile,PLAYERS_AWAY)
            elif choice == '6': #Exports total info of every player in the game
                ExportToCSV(5,JsonFile,PLAYERS_HOME,PLAYERS_AWAY)
            elif choice == '7': #Exits submenu
                break
            else:
                print("Sorry I didn't get what you wanted to do?")
            choice = '0' #Only way of exiting this loop is manually
        except EOFError:
            pass

def subMenu():
    JsonFile = parser.getJsonFile()
    TEAMS_TOTAL, TEAMS_1ST_HALF, TEAMS_2ND_HALF, PLAYERS_HOME, PLAYERS_AWAY, EVENTS = parser.parseJson(JsonFile)
    choice = '0'
    while choice == '0': # Simple Menu
        try:
            print("-------- SUBMENU ---------")
            print("1.- Show total info of teams")
            print("2.- Show first half of teams")
            print("3.- Show second half of teams")
            print("4.- Show HOME team players stats")
            print("5.- Show AWAY team players stats")
            print("6.- Show total info of every player in the game")
            print("7.- Show events")
            print("8.- Export JSON to .CSV")
            print("9.- Exit Submenu")
            print("")
            choice = input("So what is it gonna be? ")

            if choice == '1': #Show total info of teams
                parser.printTable(TEAMS_TOTAL)
            elif choice == '2': #Show first half of teams
                parser.printTable(TEAMS_1ST_HALF)
            elif choice == '3': #Show second half of teams
                parser.printTable(TEAMS_2ND_HALF)
            elif choice == '4': #Show HOME team players stats
                parser.printTable(PLAYERS_HOME)
            elif choice == '5': #Show AWAY team players stats
                parser.printTable(PLAYERS_AWAY)
            elif choice == '6': #Show total info of every player in the game
                parser.printTable(PLAYERS_HOME,PLAYERS_AWAY)
            elif choice == '7': #Show events
                parser.printEvents(EVENTS)
            elif choice == '8': #Export to CSV
                ExportSubmenu(JsonFile,TEAMS_TOTAL, TEAMS_1ST_HALF, TEAMS_2ND_HALF, PLAYERS_HOME, PLAYERS_AWAY, EVENTS)
            elif choice == '9': #Exits submenu
                break
            else:
                print("Sorry I didn't get what you wanted to do?")
            choice = '0' #Only way of exiting this loop is manually
        except EOFError:
            pass


def main():
    choice = '0'
    while choice == '0': # Simple Menu
        try:
            print("")
            print("---------- MENU -----------")
            print("1.- Insert JSON file into DB (It will ask for JSON file path)")
            print("2.- Check JSON data (It will ask for JSON file path)")
            print("3.- Exit")
            print("")
            choice = input("So what is it gonna be? ")

            if choice == '1': #Inserts data into the DB
                subMenu()
            elif choice == '2': #Shows parsed data
                subMenu()
            elif choice == '3': #Exits
                print("Goodbye..")
                break
            else:
                print("Sorry I didn't get what you wanted to do?")
            choice = '0' #Only way of exiting this loop is manually
        except EOFError:
            pass
            print("")



if __name__ == '__main__':
    IgnoreKeyboardInterrupt()
    main()