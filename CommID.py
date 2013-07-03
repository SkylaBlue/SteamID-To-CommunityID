"""
Source https://developer.valvesoftware.com/wiki/SteamID

Following that guide, we can convert a SteamID to it's community id.
"""

SteamID    = raw_input("Enter SteamID: ")

# Doesn't really need to be caps, but I prefer it
if not SteamID.startswith("STEAM_"):
    print "Please use a valid steam id!"
    
splitID    = SteamID.split(":")

Universe   = int(splitID[1])
# User entered a SteamID with a universe greater than one, which is basically impossible
if len(Universe) > 1:
    print "Please use a valid steam id!"
    
LastDigits = int(splitID[2])*2
# User entered a SteamID with an id less than 1, which is impossible
if len(LastDigits) < 1:
    print "Please use a valid steam id!"

# Valve uses 0x0110000100000000 as the SteamID64 identifier  
Algo       = 76561197960265728

CommunityID = Algo + LastDigits + Universe
print "Community ID:", CommunityID

raw_input()
