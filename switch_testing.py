import RPi.GPIO as GPIO
import threading
import pygame

PINS = {
    "c": 2,
    "c#": 3,
    "d": 4,
    "d#": 14,
    "e": 15,
    "f": 18,
    "f#": 27,
    "g": 22,
    "g#": 23,
    "a": 24,
    "a#": 210,
    "b": 9
}
SOUND_FILENAMES = {
    "a": "./sounds/a.wav",
    "a#": "./sounds/a#.wav",
    "b": "./sounds/b.wav",
    "c": "./sounds/c.wav",
    "c#": "./sounds/c#.wav",
    "d": "./sounds/d.wav",
    "d#": "./sounds/d#.wav",
    "e": "./sounds/e.wav",
    "f": "./sounds/f.wav",
    "f#": "./sounds/f#.wav",
    "g": "./sounds/g.wav",
    "g#": "./sounds/g#.wav"
}


def play_note(file_name):
   pygame.mixer.music.load(file_name)
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
       continue


def wait_for_press(note):
    pin = PINS[note]
    file_name = SOUND_FILENAMES[note]
    while True:
        if GPIO.input(pin) == GPIO.HIGH:
            print(note)
            play_note(file_name)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in PINS.values():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    pygame.mixer.init()

    for note in PINS:
        thread = threading.Thread(target=wait_for_press, args=(note,))
        thread.start()

