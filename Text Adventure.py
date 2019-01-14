#---------------- Room Setup ----------------
class Room(object): #characteristics of every room in the program
    def __init__(self, Name, Desc, Connect, Items = [], Locks = []):
        self.Name = Name
        self.Desc = Desc
        self.Connect = Connect
        self.Items = Items #optional
        self.Locks = Locks #optional
Rooms = {}
Rooms["Start Location"] = Room("Start Location",open("startlocation.txt"),{"W": "The Spaniel", "N": "Forest", "E": "Appartment Complex"}, ["WALTHERPPK"], ["E"])
Rooms["The Spaniel"] = Room("The Spaniel",open("Pubname.txt"),{"E": "Start Location"},["Beer"])
Rooms["Appartment Complex"] = Room("Appartment Complex",open("AppartmentComplex.txt"),{"W": "Start Location", "N": "HighwayExit"}, ["CANOPENER"], ["N"])
Rooms["Forest"] = Room("Forest",open("Forest.txt"),{"S": "Start Location", "N": "Cave"}, ["KEYCARD"])
Rooms["HighwayExit"] = Room("HighwayExit",open("Highwayexit.txt"), {"S": "Appartment Complex"})
Rooms["Cave"] = Room("Cave",open("Cave.txt"),{"S": "Forest", "E": "Internet Tower"})
Rooms["Internet Tower"] = Room("Internet Tower",open("InternetTower.txt"), {"W": "Cave"})

class Player(object):
    def __init__(self):
        self.CurrentLocation = Rooms["Start Location"]
        self.Inventory = []
Player = Player()
#---------------- Item Setup ----------------
class Items(object):
    def __init__ (self, Name, Description):
        self.Name = Name
        self.Description = Description
ItemDict = {}
ItemDict["WALTHERPPK"] = Items("WALTHERPPK", "A nine milimeter handgun that could be used to shoot locks off...")
ItemDict["BEER"] = Items("BEER", "An alcoholic beverage that requires a certain taste to enjoy.")
ItemDict["CANOPENER"] = Items("CANOPENER", "A tool used to open cans... it even comes with a bottle opener attatchment")
ItemDict["KEYCARD"] = Items("KEYCARD", "This Key card can be used to open a lokced door to escape this simulation")

#---------------- Player Movement ----------------
def WrongDrirection():
    print("You cannot proceed in this direction")
def PlayerMovement(PlayerChoice):
    if len(PlayerChoice) < 2:
        print("Please choose a direction")
    elif PlayerChoice[1] == "NORTH":
        if "N" in Player.CurrentLocation.Connect:
            if "N" in Player.CurrentLocation.Locks:
                print("The Door is Locked")
            else:
                print("Going North")
                Player.CurrentLocation = Rooms[Player.CurrentLocation.Connect["N"]]
        else:
            WrongDirection()
    elif PlayerChoice[1] == "EAST":
        if "E" in Player.CurrentLocation.Connect:
            if "E" in Player.CurrentLocation.Locks:
                print("The Door is Locked")
            else:
                print("Going East")
                Player.CurrentLocation = Rooms[Player.CurrentLocation.Connect["E"]]
        else:
            WrongDirection()
    elif PlayerChoice[1] == "SOUTH":
        if "S" in Player.CurrentLocation.Connect:
            if "S" in Player.CurrentLocation.Locks:
                print("The Door is Locked")
            else:
                print("Going South")
                Player.CurrentLocation = Rooms[Player.CurrentLocation.Connect["S"]]
        else:
            WrongDirection()
    elif PlayerChoice[1] == "WEST":
        if "W" in Player.CurrentLocation.Connect:
            if "W" in Player.CurrentLocation.Locks:
                print("The Door is Locked")
            else:
                print("Going West")
                Player.CurrentLocation = Rooms[Player.CurrentLocation.Connect["W"]]
        else:
            WrongDirection()
    else:
        print("That is not a valid direction to travel in")

#---------------- Interacting with world ----------------
def Look(PlayerChoice):
    if len(PlayerChoice) < 2:
        print(Player.CurrentLocation.Desc.read())
    elif PlayerChoice[1] in Player.CurrentLocation.Items:
        print(ItemDict[PlayerChoice[1]].Description)

#------------ Player Interacting With Items ----------------
def Take(PlayerChoice):
    if len(PlayerChoice) < 2:
        print("Please Specify the Item You Want To Pick Up")
    elif PlayerChoice[1] in Player.CurrentLocation.Items:
        Player.Inventory.append(PlayerChoice[1])
        Player.CurrentLocation.Items.remove(PlayerChoice[1])
        print (PlayerChoice[1] + " was placed in your bag")
    else:
        print("That item isn't here...")
def Toss(PlayerChoice):
    if len(PlayerChoice) < 2:
        print("Please Choose An Item To Toss")
    elif PlayerChoice[1] in Player.Inventory:
        Player.Inventory.remove(PlayerChoice[1])
        print("You Tossed " + PlayerChoice[1])
    else:
        print("This item is not in your inventory... unable to toss")
def UnableToUse():
    print("There's a time and a place for everything but not now!")

def UsingItem(PlayerChoice):
   if len(PlayerChoice) < 2:
        print ("Please select an item to use")
   elif PlayerChoice[1] in Player.Inventory:
        if PlayerChoice[1] == "WALTHERPPK":
            if  Player.CurrentLocation == Rooms["Start Location"]:
                Player.CurrentLocation.Locks = []
                print("You shoot off the lock, you can now enter the room")
            else:
                UnableToUse()
        elif PlayerChoice[1] == "KEYCARD":
            if Player.CurrentLocation == Rooms["Appartment Complex"]:
               Player.CurrentLocation.Locks = []
               print("The keycard enabled the locked door to open")
            else:
                UnableToUse()
#---------------- Help Logic ----------------
def Help():
    print("""Use These commands throughout the game
GO (+ direction of choice) to move your character
LOOK - Gives you a summary of the room you are in
LOOK (Item) - Gives you a description of a certain item
TAKE (Item) - Enables you to pick up items and have them in your bag
TOSS (ITEM) - Removes items from your inventory
USE (ITEM) - uses an item to remove locks or access pannels in a certain room
""")

#---------------- Processing Inputs ----------------
def ProcessInput(PlayerChoice):
    if PlayerChoice[0] == "GO":
        PlayerMovement(PlayerChoice)
        print(PlayerChoice)
    elif PlayerChoice[0] == "LOOK":
        Look(PlayerChoice)
    elif PlayerChoice[0] == "TAKE":
        Take(PlayerChoice)
    elif PlayerChoice[0] == "TOSS":
        Toss(PlayerChoice)
    elif PlayerChoice[0] == "USE":
        UsingItem(PlayerChoice)
    elif PlayerChoice[0] == "HELP":
        Help()
    else:
        print("Please enter a valid Command")
        
    if Player.CurrentLocation == Rooms["HighwayExit"]:
        print(Player.CurrentLocation.Desc.read())
        GameRunning == False
    


#--------------- Game Handler ----------------
GameRunning = True
while GameRunning == True:
    PlayerChoice = input("What would you like to do? ")
    PlayerChoice = PlayerChoice.upper()
    PlayerChoice = PlayerChoice.split(" ")
    print(PlayerChoice)
    ProcessInput(PlayerChoice)

    

                                   
                    
