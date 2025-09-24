from player import Player
import os
import pygame
from audio import AudioManager
from pathlib import Path
from horrorland import Horrorland
from PIL import Image


def main():
    # init player
    name = input("enter your name")
    age = input("enter your age")
    # name = 'gabe'
    # age = 32
    player_1 = Player(name, age)
    print(f"starting game as {player_1.name} whose age is {player_1.age}")

    def print_ascii_image(path, width=100):
        img = Image.open(path)
        img = img.convert("L")  # grayscale
        aspect_ratio = img.height / img.width
        height = int(aspect_ratio * width * 0.55)
        img = img.resize((width, height))

        pixels = img.getdata()
        chars = "@%#*+=-:. "
        new_pixels = [chars[pixel // 25] for pixel in pixels]
        ascii_str = "".join(new_pixels)

        for i in range(0, len(ascii_str), width):
            print(ascii_str[i : i + width])

    print_ascii_image(Path("./images/demon.PNG"))

    hl = Horrorland(player_1)
    hl.intro()
    hl.park_entrance()
    hl.park_map()


if __name__ == "__main__":
    main()
