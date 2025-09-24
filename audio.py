import pygame
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AudioManager():
    audio_file: Path

    def play_audio(self):
        pygame.init()
        pygame.mixer.music.load(self.audio_file)
        pygame.mixer.music.play()
        # Keep the terminal open until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.stop()