from player import Player

import pygame
from audio import AudioManager
from pathlib import Path
from horrorland import HorrorlandHelp


def play_audio(file_path):
    pygame.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    # Keep the terminal open until the music finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()


def main():
    name= input('enter your name')
    age = input('enter your age')
    player_1 = Player(name, age)

    print(player_1.age)
    print(player_1.name)

    #play_audio("audio\Goosebumps_theme.mp3")
    song_1 = Path("audio\Goosebumps_theme.mp3")
    audio_1 =AudioManager(song_1)
    audio_1.play_audio()


    hlh = HorrorlandHelp()
    hlh.intro()

    player_1.take_damage(100)



if __name__ == '__main__':
    main()