# import RPi.GPIO as GPIO
from playsound import playsound
import time
import keyboard
import threading

A_PIN = None
A_SHARP_PIN = None
B_PIN = None
C_PIN = None
C_SHARP_PIN = None
D_PIN = None
D_SHARP_PIN = None
E_PIN = None
F_PIN = None
F_SHARP_PIN = None
G_PIN = None
G_SHARP_PIN = None


def get_pin(note):
    match note:
        case "a":
            return A_PIN
        case "a#":
            return A_SHARP_PIN
        case "b":
            return B_PIN
        case "c":
            return C_PIN
        case "c#":
            return C_SHARP_PIN
        case "d":
            return D_PIN
        case "d#":
            return D_SHARP_PIN
        case "e":
            return E_PIN
        case "f":
            return F_PIN
        case "f#":
            return F_SHARP_PIN
        case "g":
            return G_PIN
        case "g#":
            return G_SHARP_PIN


def get_sound(note):
    match note:
        case "a":
            return "./sounds/a.wav"
        case "a#":
            return "./sounds/a#.wav"
        case "b":
            return "./sounds/b.wav"
        case "c":
            return "./sounds/c.wav"
        case "c#":
            return "./sounds/c#.wav"
        case "d":
            return "./sounds/d.wav"
        case "d#":
            return "./sounds/d#.wav"
        case "e":
            return "./sounds/e.wav"
        case "f":
            return "./sounds/f.wav"
        case "f#":
            return "./sounds/f#.wav"
        case "g":
            return "./sounds/g.wav"
        case "g#":
            return "./sounds/g#.wav"


def play_note(note, interval):
    thread = threading.Thread(target=playsound, args=(get_sound(note),))
    thread.start()
    thread.join()
#     pin = get_pin(note)
#     GPIO.output(pin, GPIO.HIGH)
#     time.sleep(interval)
#     GPIO.output(pin, GPIO.LOW)

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
