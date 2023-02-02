# Python file which will allow usage of Call of Duty API to retrieve stats.

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
while loop != "q" or loop != "Q".lower():
    # user inputs
    game = input("Enter the Call of Duty Title (mw, mw2, cw, vg, wz): ")
    platform = input("Enter your platform: ")
    username = input("Enter your username: ")
    if game == "mw":
        profile = api.ModernWarfare.fullData(platforms.XBOX, username)
    elif game == "mw2":
        profile = api.ModernWarfare2.fullData(platforms.XBOX, "Moe613")
    elif game == "cw":
        profile = api.ColdWar.fullData(platforms.XBOX, "Moe613")
    elif game == "vg":
        profile = api.Vanguard.fullData(platforms.XBOX, "Moe613")
    elif game == "wz":
        profile = api.Warzone.fullData(platforms.XBOX, "Moe613")

    # retrieve profile data from api for specified game data returned as dictionary
    # relevant player information is nested in multiple dictionaries,
    # which is now stored in info
    info = profile["data"]["lifetime"]["all"]["properties"]
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

    # quit to exit while loop
    print()
    loop = input("Q or q to quit, anything else to continue \n")


