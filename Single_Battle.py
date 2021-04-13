import pokemon_database

def __init__(self):
    self.playerTeam = 0
    self.enemyTeam = 0
    self.playerItems = 0


def createTeam(self):
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
    self.playerTeam = [None] * team_size
    self.enemyTeam = [None] * team_size
    print("\nWould like like randomized Pokemon? (y/n)")
    randomized = input(": ").lower()
    if randomized == "n":
        assignRandomPokemon(playerTeam)
        assignRandomPokemon(enemyTeam)
    else:
        choosePokemon()
    print(randomized)

def choosePokemon():
    i = 1
    for pokemon in playerTeam:
        print("Please select Pokemon " + i + " ")
        name = input(": ")
        pokemon = eval(name)
        print("DEBUG " + pokemon.name)
        i += 1
        


# This method accepts no inputs and assigns random Pokemon for both teams. 
# This method needs heavy edits. I would like this method to assign random pokemon based on how 
# many Pokemon I have included in the pokemon_database folder.
def assignRandomPokemon(team):
    for pokemon in team:
        chance = random.randint(0, 1)
        if chance == 1:
            pokemon = Charmander()
        else:
            pokemon = Bulbasaur()

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

