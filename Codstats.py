# Python file which will allow usage of Call of Duty API to retrieve stats.
import json
import time
from pathlib import Path

import data as data
# import API module with classes from cod_api package
from cod_api import API, platforms

api = API()

# login with sso token retrievd from www.callofduty.com
SSO_TOKEN = 'MTczNDU2MjIxNzQ2NDgwNDA0OTQ6MTY3NjUyNDM2MDU1OTo5ZTM5MmI4ZTdiZTVmYzdlNzA3NTFjZmMzYzczMDM0Ng'
api.login(SSO_TOKEN)

# uncomment following line to print the Warzone docstring
# print(api.Warzone.__doc__)
print("Call of Duty Stats Tracker"
      "\n---------------------------")
loop = ''
while loop != "q" or loop != "Q":
    # input Call of Duty title
    game = input("Enter the Call of Duty Title (mw, cw, vg, wz): ")
    if game == "mw":
        profile = api.ModernWarfare
    elif game == "cw":
        profile = api.ColdWar
    elif game == "vg":
        profile = api.Vanguard
    elif game == "wz":
        profile = api.Warzone

    # input platform
    platform = input("Enter your platform: ")
    if platform == "xbox" or platform == "Xbox" or platform == "XBOX":
        client = platforms.XBOX
    elif platform == "psn" or platform == "Psn" or platform == "PSN":
        client = platforms.PSN
    elif platform == "activision" or platform == "Activision":
        client = platforms.Activision
    elif platform == "battlenet" or platform == "Battlenet":
        client = platforms.Battlenet

    # input username
    username = input("Enter your username: ")

    user = profile.fullData(client, username)
    # retrieve profile data from api for specified game data returned as dictionary
    # relevant player information is nested in multiple dictionaries,
    # which is now stored in info
    info = user
    print(info)
    print("---------------------------")

    # get KD/Ratio from properties dictionary and round to 2 decimal places
    if info.get("kdRatio"):
        kd = round(info.get("kdRatio"), 2)
        print("KD/Ratio: ", kd)
    elif info.get("kdratio"):
        kd = round(info.get("kdratio"), 2)
        print("KD/Ratio: ", kd)

    # get Highest kills from properties dictionary and round to 2 decimal places
    if info.get("recordKillsInAMatch"):
        kills = int(info.get("recordKillsInAMatch"))
        print("Highest Kills (match): ", kills)
    elif info.get("recordKillsInAMatch"):
        kills = int(info.get("recordKillsInAMatch"))
        print("Highest Kills (match): ", kills)

    # get Longest killstreak from properties dictionary and round to 2 decimal places
    if info.get("longestKillstreak"):
        ks = int(info.get("longestKillstreak"))
        print("Longest Killstreak: ", ks)
    elif info.get("recordKillStreak"):
        ks = int(info.get("recordKillStreak"))
        print("Longest Killstreak: ", ks)

    # get WL/Ratio from properties dictionary and round to 2 decimal places
    if info.get("wlratio"):
        wl = round(info.get("wlratio"), 2)
        print("WL/Ratio: ", wl)
    elif info.get("winLossRatio"):
        wl = round(info.get("winLossRatio"), 2)
        print("WL/Ratio: ", wl)

    # This is where the captured statistics will be saved in the local directory
    csv_file = Path("C:/Users/moham/Desktop/")
    # Initialize counters
    timePlayed = 0
    kdRatio = 0
    score = 0
    xp = 0
    level = 0
    prestige = 0
    platforms = ['battle']

    fileName = "callOfDuty" + platform + ".csv"
    outputFile = csv_file / fileName

    user = profile.fullData(client, username)
    # Pull the metrics for this player into a variable.
    thisMetrics = user['data']['lifetime']['all']['properties']
    timePlayed = thisMetrics['timePlayedTotal']

    print("timePlayed:" + str(timePlayed) + " hours\n")
    # print(thisMetrics)
    title = user['data']['title']
    kdRatio = thisMetrics['kdRatio']
    kills = thisMetrics['kills']
    longestKillStreak = thisMetrics['recordKillStreak']
    bestKd = thisMetrics['bestKD']
    mostKills = thisMetrics['recordKillsInAMatch']

    # Create summary line for the csv file
    outputCSV = "Time played: " + str(timePlayed) + "\n" + "Title: " + str(title) + "\n" + "K/D ratio: " + str(kdRatio) + "\n" + "Kills: " + str(
        kills) + "\n" + "Longest Killstreak" + str(longestKillStreak) + "\n" + "Best K/D: " + str(bestKd) + "\n" + "Most Kills: " + str(mostKills) + "\n "
    # Now populate the csv file for this platform
    with open(outputFile, "w", newline='') as file:
        file.write(outputCSV)

    # quit to exit while loop
    loop = input("Q or q to quit, anything else to continue \n")
    if loop == 'q' or loop == 'Q':
        exit()
