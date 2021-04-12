import random

class Bulbasaur:
    def __init__(self):
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
        self.move1 = {"Name" : "Growl",
                      "PP" : 40,
                      "Accuracy" : 100,
                      "Move_Type" : "Normal",
                      "Power" : 0,
                      "Stat_Effect" : "Attack", 
                      "Stat_Change" : -1}
        self.move2 = {"Name" : "Tackle",
                      "PP" : 35,
                      "Accuracy" : 100,
                      "Move_Type" : "Normal",
                      "Power" : 40,
                      "Stat_Effect" : None, 
                      "Stat_Change" : None}
        self.move3 = {"Name" : "--",
                      "PP" : None,
                      "Accuracy" : None,
                      "Move_Type" : None,
                      "Power" : None,
                      "Stat_Effect" : None, 
                      "Stat_Change" : None}
        self.move4 = {"Name" : "--",
                      "PP" : None,
                      "Accuracy" : None,
                      "Move_Type" : None,
                      "Power" : None,
                      "Stat_Effect" : None, 
                      "Stat_Change" : None}
    def buildTest(self):
        print(self.id)
        print(self.gender)
        print(self.type)
        print(self.stats)
        print(self.move1)
        print(self.move2)
        print(self.move3)
        print(self.move4)
        print("Successful Build!")

instance = Bulbasaur()
instance.__init__()
instance.buildTest()
            