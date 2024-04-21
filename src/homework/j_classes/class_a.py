#

import random  


class Die:
    
    def __init__(self):
        self.roll_value = 0  # Initially set roll_value to 0

    def roll(self):
        self.roll_value = random.randint(1, 6)  # Randomly assign value to roll_value

    def get_rolled_value(self):
        return self.roll_value  # Return the stored roll_value

    def __str__(self):
        return f"The rolled value is {self.roll_value}"  # Format the output message




