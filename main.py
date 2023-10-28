class Tank_t72:
    armor = 170
    speed = 85
    smoothbore_gun = 125

class Bnp_2m(Tank_t72):
    smoothbore_gun = 30

class Btr(Bnp_2m):
    armor = 30
    def __init__(self):
        print(self.armor)
        print(self.speed)
        print(self.smoothbore_gun)

Btr_2 = Btr()
