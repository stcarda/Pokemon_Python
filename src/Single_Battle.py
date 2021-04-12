from Pokemon_Entity import Pokemon_Entity
from Bulbasaur import Bulbasaur

def createTeam():
    print("\n*** Welcome to Single Battles! ***")
    print("----------------------------------\n")
    print("How many Pokemon would you like in your team?")
    team_size = input(": ")
    print("Would like like randomized Pokemon?")
    randomized = input(": ")

def choosePokemon():
    print("Temp")

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