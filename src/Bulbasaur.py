import random

class Bulbasaur:
    def __init__(self):
        self.name = "Bulbasaur"
        self.id = 1
        self.type = ["Grass", "Poison"]
        self.gender = "Male"
        gender_chance = random.randint(0, 1)
        if gender_chance == 0:
            self.gender = "Female"
        self.stats = {"HP" : 45,
                      "Attack" : 49,
                      "Defense" : 49,
                      "Sp. Attack" : 65,
                      "Sp. Defense": 65,
                      "Speed" : 45}
        self.moveset = [{"Name" : "Growl",          # MOVE 1
                         "PP" : 40,
                         "Accuracy" : 100,
                         "Type" : "Normal",
                         "Power" : 0,
                         "Category" : "Status", 
                         "Stages" : 1},
                        {"Name" : "Tackle",         # MOVE 2
                         "PP" : 35,
                         "Accuracy" : 100,
                         "Type" : "Normal",
                         "Power" : 40,
                         "Category" : "Physical", 
                         "Stages" : 0}, 
                         {"Name" : "--",            # MOVE 3
                         "PP" : None,
                         "Accuracy" : None,
                         "Type" : None,
                         "Power" : None,
                         "Category" : None, 
                         "Stages" : None}, 
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

instance = Bulbasaur()
instance.__init__()
instance.buildTest()
            