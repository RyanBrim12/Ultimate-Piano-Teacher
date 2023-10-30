import pygame

SOUND_FILENAMES = {
    "a": "./sounds/a.wav",
    "a#": "./sounds/a#.wav",
    "b": "./sounds/b.wav",
    "c": "./sounds/c.wav",
    "c#": "./sounds/c#.wav",
    "d":  "./sounds/d.wav",
    "d#": "./sounds/d#.wav",
    "e": "./sounds/e.wav",
    "f": "./sounds/f.wav",
    "f#": "./sounds/f#.wav",
    "g": "./sounds/g.wav",
    "g#": "./sounds/g#.wav"
}

if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND_FILENAMES["a"])
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
