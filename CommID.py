"""
Source https://developer.valvesoftware.com/wiki/SteamID

Following that guide, we can convert a SteamID to it's community id.
"""

def SteamToComm():
    SteamID    = raw_input("Enter SteamID: ")

    # Doesn't really need to be caps, but I prefer it
    if not SteamID.startswith("STEAM_"):
        print "Please use a valid steam id!"
        
    splitID    = SteamID.split(":")

    Universe   = int(splitID[1])
    # User entered a SteamID with a universe greater than one, which is basically impossible
    if Universe > 1:
        print "Please use a valid steam id!"
        
    LastDigits = int(splitID[2])*2
    # User entered a SteamID with an id less than 1, which is impossible
    if LastDigits < 1:
        print "Please use a valid steam id!"

    # Valve uses 0x0110000100000000 as the SteamID64 identifier  
    Algo       = 76561197960265728

    CommunityID = Algo + LastDigits + Universe
    print "\nCommunity ID:", CommunityID

def CommToSteam():
    CommID = long(raw_input("Enter community id: "))

    Algo     = 76561197960265728
    Universe = CommID % 2
    SteamID  = (CommID - Algo - Universe) / 2
    print "\nSteamID: STEAM_0:%s:%s" % (int(Universe), SteamID)

def main():
    choise     = raw_input("1: SteamID->CommunityID\n" \
                           "2: CommunityID->SteamID\n" \
                           "-> ")

    if choise   == '1':
        SteamToComm()
    elif choise == '2':
        CommToSteam()
    else:
        print "Please enter 1 or 2!"

while True:
    main()
raw_input()
