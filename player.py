import time
import sys
import os
from PIL import Image


class Player:

    def __init__(self, name:str, age:str, health=100):
        self.name = name
        self.age = age
        self.health = health


    def take_damage(self, damage:int):
        self.health -= damage
        if self.health <=0:
            self.player_death()

    def player_death(self):
        print("So we finally meet. It's too bad you had to die for us to meet like this")
        time.sleep(5)
        # flush after every print because otherwise the terminal does not update real time
        sys.stdout.flush()
        # open image signifiying the player died
        img = Image.open(r"images\headless.PNG")
        img.show()
        # exit the terminal because the game is over
        os._exit(0)

    