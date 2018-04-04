import tkinter as tk
from tkinter import filedialog #For the window
from prettytable import PrettyTable #Table
import json
from modules import parser
import signal

def IgnoreKeyboardInterrupt():
    return signal.signal(signal.SIGINT,signal.SIG_IGN)


def InsertIntoDB():
    print("Under Construction")

def subMenu():
    JsonFile = parser.getJsonFile()
    TEAMS_TOTAL, TEAMS_1ST_HALF, TEAMS_2ND_HALF, PLAYERS_HOME, PLAYERS_AWAY = parser.parseJson(JsonFile)
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
            print("7.- Exit Submenu")
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
            elif choice == '7': #Exits submenu
                break
            else:
                print("Sorry I didn't get what you wanted to do?")
            choice = '0' #Only way of exiting this loop is manually
            pass
        except EOFError:
            pass
            print("")


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



if __name__ == '__main__':
    IgnoreKeyboardInterrupt()
    main()