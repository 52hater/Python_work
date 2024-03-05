from random import randint

class Die:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
    
result = []
cube_dice = Die()
for roll_num in range(10):
    result = cube_dice.roll_die
    result = list.append
