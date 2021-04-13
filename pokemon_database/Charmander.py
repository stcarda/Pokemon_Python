import random

class Charmander:
    def __init__(self):
        self.id = 1
        self.type = ["Fire"]
        self.gender = "Male"
        gender_chance = random.randint(0, 1)
        if gender_chance == 0:
            self.gender = "Female"
        self.stats = {"HP" : 39,
                      "Attack" : 52,
                      "Defense" : 43,
                      "Sp. Attack" : 60,
                      "Sp. Defense": 50,
                      "Speed" : 65}
        self.moveset = [{"Name" : "Growl",          # MOVE 1
                         "PP" : 40,
                         "Accuracy" : 100,
                         "Type" : "Normal",
                         "Power" : 0,
                         "Category" : "Status", 
                         "Stages" : 1},
                        {"Name" : "Scratch",         # MOVE 2
                         "PP" : 35,
                         "Accuracy" : 100,
                         "Type" : "Normal",
                         "Power" : 40,
                         "Category" : "Physical", 
                         "Stages" : 0}, 
                         {"Name" : "Ember",            # MOVE 3
                         "PP" : 25,
                         "Accuracy" : 100,
                         "Type" : "Fire",
                         "Power" : 40,
                         "Category" : "Special", 
                         "Stages" : 0}, 
                         {"Name" : "--",            # MOVE 4
                         "PP" : None,
                         "Accuracy" : None,
                         "Type" : None,
                         "Power" : None,
                         "Category" : None, 
                         "Stages" : None}] 
    
    def buildTest(self):
        print(self.id)
        print(self.gender)
        print(self.type)
        print(self.stats)
        for move in self.moveset:
            print(move)
        print("Successful Build!")

instance = Charmander()
instance.__init__()
instance.buildTest()