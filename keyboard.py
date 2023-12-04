import RPi.GPIO as GPIO
import pygame
import time
import threading

PINS = {
    "c": 12,
    "c#": 7,
    "d": 9,
    "d#": 10,
    "e": 24,
    "f": 23,
    "f#": 22,
    "g": 27,
    "g#": 18,
    "a": 15,
    "a#": 14,
    "b": 4
}

SOUND_FILENAMES = {
    "c": "./piano_notes/c.wav",
    "c#": "./piano_notes/c#.wav",
    "d": "./piano_notes/d.wav",
    "d#": "./piano_notes/d#.wav",
    "e": "./piano_notes/e.wav",
    "f": "./piano_notes/f.wav",
    "f#": "./piano_notes/f#.wav",
    "g": "./piano_notes/g.wav",
    "g#": "./piano_notes/g#.wav",
    "a": "./piano_notes/a.wav",
    "a#": "./piano_notes/a#.wav",
    "b": "./piano_notes/b.wav"
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
        if GPIO.input(pin) == GPIO.LOW:
            print(note)
            play_note(file_name)
        time.sleep(0.1)


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in PINS.values():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    pygame.mixer.init()

    for note in PINS:
        thread = threading.Thread(target=wait_for_press, args=(note,))
        thread.start()
