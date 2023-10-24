# import RPi.GPIO as GPIO
from playsound import playsound
import time
import keyboard
import threading

PINS = {
    "a": 2,
    "a#": 3,
    "b": 4,
    "c": 17,
    "c#": 27,
    "D": 22,
    "d#": 10,
    "e": 9,
    "f": 11,
    "f#": 5,
    "g": 6,
    "g#": 13
}

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


def play_note(note, interval):
    thread = threading.Thread(target=playsound, args=(SOUND_FILENAMES[note],))
    thread.start()
    thread.join()
    pin = PINS[note]
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(pin, GPIO.LOW)

if __name__ == "__main__":
    keyboard.add_hotkey("1", lambda: play_note("a", 0))
    keyboard.add_hotkey("2", lambda: playsound(get_sound("a#")))
    keyboard.add_hotkey("3", lambda: playsound(get_sound("b")))
    keyboard.add_hotkey("4", lambda: playsound(get_sound("c")))
    keyboard.add_hotkey("5", lambda: playsound(get_sound("c#")))
    keyboard.add_hotkey("6", lambda: playsound(get_sound("d")))
    keyboard.add_hotkey("7", lambda: playsound(get_sound("d#")))
    keyboard.add_hotkey("8", lambda: playsound(get_sound("e")))
    keyboard.add_hotkey("9", lambda: playsound(get_sound("f")))
    keyboard.add_hotkey("0", lambda: playsound(get_sound("f#")))
    keyboard.add_hotkey("-", lambda: playsound(get_sound("g")))
    keyboard.add_hotkey("=", lambda: playsound(get_sound("g#")))

    keyboard.wait()
    # playsound("./sounds/c.wav")
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(PIN, GPIO.OUT)
