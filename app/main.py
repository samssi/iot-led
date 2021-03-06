import RPi.GPIO as GPIO
import time
import signal
from flask import Flask, request
import json
import sys

app = Flask(__name__)


def setupBoard():
    global greenPwm
    global bluePwm
    global redPwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)

    redPwm = GPIO.PWM(11, 2000)
    greenPwm = GPIO.PWM(12, 2000)
    bluePwm = GPIO.PWM(13, 2000)

def start():
    redPwm.start(0)
    bluePwm.start(0)
    greenPwm.start(0)

def rgbToPwm(value):
    scaledDownVar = int(round((value / 2.55), 0))
    return abs(scaledDownVar - 100)

def redCycle(value):
    redPwm.ChangeDutyCycle(value)

def greenCycle(value):
    greenPwm.ChangeDutyCycle(value)

def blueCycle(value):
    bluePwm.ChangeDutyCycle(value)

def ledOff():
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(12, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)

def loop():
    while True:
        time.sleep(1)

def destroy():
    redPwm.stop()
    bluePwm.stop()
    greenPwm.stop()
    ledOff()
    GPIO.cleanup()

def ledOn(r, g, b):
    start()
    redCycle(rgbToPwm(r))
    greenCycle(rgbToPwm(g))
    blueCycle(rgbToPwm(b))

def exit(signum, stack):
	destroy()

def setup():
    setupBoard()
    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)

setup()
ledOn(222, 20, 255)


@app.route('/color', methods=['POST'])
def changeColor():
    request_json = request.get_json()
    r = request_json.get('r')
    g = request_json.get('g')
    b = request_json.get('b')
    ledOn(r, g, b)
    return "Hello World!"