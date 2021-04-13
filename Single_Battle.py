import pokemon_database

def __init__(self):
    self.playerTeam = 0
    self.enemyTeam = 0
    self.playerItems = 0


def createTeam():
    print("\n*** Welcome to Single Battles! ***")
    print("----------------------------------\n")
    print("How many Pokemon would you like in your team?")
    team_size = int(input(": "))
    while team_size != 1:
        if team_size == 0:
            print("\nSorry, but you cannot have a team of zero!\n")
        else:
            print("\nSorry, teams other than one are unsupported right now. Please choose a ")
            print("smaller team size.\n")
        print("How many Pokemon would you like in your team?")
        team_size = int(input(": "))
    print("\nWould like like randomized Pokemon? (y/n)")
    randomized = input(": ").lower()
    if randomized == "n":
        assignRandomPokemon()

    print(randomized)

def choosePokemon():
    print("Temp")

def assignRandomPokemon():
    

def showPokemonList():
    print("Temp")

def decideAction(target):
    print("What should " + target.name +  " do?")
    print("Attack\t Bag\n") 
    print("Pokemon\t Run")
    return input(": ")


def showMoves(target):
    for move in move_list:
        print(move)

createTeam()