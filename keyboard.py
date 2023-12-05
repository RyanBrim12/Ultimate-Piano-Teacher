import RPi.GPIO as GPIO
import pygame
import time
import threading

PINS = {
    "c": 12,
    "c_sharp": 7,
    "d": 9,
    "d_sharp": 10,
    "e": 24,
    "f": 23,
    "f_sharp": 22,
    "g": 27,
    "g_sharp": 18,
    "a": 15,
    "a_sharp": 14,
    "b": 4
}

SOUND_FILENAMES = {
    "c": "./piano_notes/c.wav",
    "c_sharp": "./piano_notes/c_sharp.wav",
    "d": "./piano_notes/d.wav",
    "d_sharp": "./piano_notes/d_sharp.wav",
    "e": "./piano_notes/e.wav",
    "f": "./piano_notes/f.wav",
    "f_sharp": "./piano_notes/f_sharp.wav",
    "g": "./piano_notes/g.wav",
    "g_sharp": "./piano_notes/g_sharp.wav",
    "a": "./piano_notes/a.wav",
    "a_sharp": "./piano_notes/a_sharp.wav",
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
