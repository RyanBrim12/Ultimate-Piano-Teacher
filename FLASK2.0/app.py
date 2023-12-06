from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

PINS = {
    "c": 25,
    "c_sharp": 8,
    "d": 17,
    "d_sharp": 11,
    "e": 5,
    "f": 6,
    "f_sharp": 13,
    "g": 19,
    "g_sharp": 26,
    "a": 16,
    "a_sharp": 20,
    "b": 21
}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for pin in PINS.values():
    GPIO.setup(pin, GPIO.OUT)

app = Flask(__name__)


def light_led(pin, duration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin, GPIO.LOW)


@app.route("/play_jingle_bells", methods=["POST"])
def play_jingle_bells():
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 1)
    time.sleep(0.5)

    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 1)
    time.sleep(0.5)

    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["g"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 2)
    time.sleep(0.5)

    light_led(PINS["f"], 0.5)
    time.sleep(0.5)
    light_led(PINS["f"], 0.5)
    time.sleep(0.5)
    light_led(PINS["f"], 0.5)
    time.sleep(0.5)
    light_led(PINS["f"], 0.5)
    time.sleep(0.5)
    light_led(PINS["f"], 0.5)
    time.sleep(0.5)

    light_led(PINS["e"], 0.5) 
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)

    light_led(PINS["d"], 0.5) 
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)

    light_led(PINS["d"], 1)
    time.sleep(0.5)
    light_led(PINS["g"], 1)
    time.sleep(0.5)
    return "ok"


@app.route("/stop_jingle_bells", methods=["POST"])
def stop_jingle_bells():
    GPIO.output(PINS["c"], GPIO.LOW)
    return "ok"


@app.route("/play_happy_birthday", methods=["POST"])
def play_happy_birthday():
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["f"], 0.5)
    time.sleep(0.5)
    light_led(PINS["e"], 1)
    time.sleep(1)

    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["g"], 0.5)
    time.sleep(0.5)
    light_led(PINS["f"], 1)
    time.sleep(1)

    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["a"], 1)
    time.sleep(0.5)
    light_led(PINS["g"], 1)
    time.sleep(0.5)
    light_led(PINS["f"], 1)
    time.sleep(0.5)
    light_led(PINS["e"], 1)
    time.sleep(0.5)
    light_led(PINS["d"], 2)
    time.sleep(0.5)

    light_led(PINS["g_sharp"], 0.5)
    time.sleep(0.5)
    light_led(PINS["g_sharp"], 0.5)
    time.sleep(0.5)
    light_led(PINS["g"], 1)
    time.sleep(0.5)
    light_led(PINS["d_sharp"], 1)
    time.sleep(0.5)
    light_led(PINS["f"], 1)
    time.sleep(0.5)
    light_led(PINS["d_sharp"], 1)
    time.sleep(0.5)
    return "ok"


@app.route("/stop_happy_birthday", methods=["POST"])
def stop_happy_birthday():
    GPIO.output(PINS["c_sharp"], GPIO.LOW)
    return "ok"


@app.route("/play_hot_crossed_buns", methods=["POST"])
def play_hot_crossed_buns():
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 1)
    time.sleep(0.5)
    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 1)
    time.sleep(0.5)

    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 0.5)
    time.sleep(0.5)

    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)

    light_led(PINS["e"], 0.5)
    time.sleep(0.5)
    light_led(PINS["d"], 0.5)
    time.sleep(0.5)
    light_led(PINS["c"], 1)
    time.sleep(0.5)
    return "ok"


@app.route("/stop_hot_crossed_buns", methods=["POST"])
def stop_hot_crossed_buns():
    GPIO.output(PINS["c_sharp"], GPIO.LOW)
    return "ok"


@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Ashley Kulcsar")

