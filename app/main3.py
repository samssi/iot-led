import RPi.GPIO as GPIO
import time

def setup():
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

def off():
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
        off()
        GPIO.cleanup()

def run(r, g, b):
        start()
        redCycle(rgbToPwm(r))
        greenCycle(rgbToPwm(g))
        blueCycle(rgbToPwm(b))

if __name__ == "__main__":
        try:
                setup()
                run(254, 1, 255)
                loop()
        except KeyboardInterrupt:
                destroy()

