import RPi.GPIO as GPIO
import time

def setup():
	global pwm
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)

	pwm = GPIO.PWM(11, 10)

def cycle():
	pwm.start(50)

	time.sleep(3)

	pwm.ChangeFrequency(200)

	print("5%")
	pwm.ChangeDutyCycle(5)   # Duty cycle is now 5%
	time.sleep(2)          # 0.5 seconds till the next change

	print("10%")
	pwm.ChangeDutyCycle(10)  # Duty cycle is now 10%
	time.sleep(2)          # 0.5 seconds till the next change

	print("15%")
	pwm.ChangeDutyCycle(15)  # Duty cycle is now 15%
	time.sleep(2)          # 0.5 seconds till the next change

	print("20%")
	pwm.ChangeDutyCycle(20)  # Duty cycle is now 20%
	time.sleep(2)          # 0.5 seconds till the next change

	print("30%")
	pwm.ChangeDutyCycle(30)  # Duty cycle is now 30%
	time.sleep(2)          # 0.5 seconds till the next change

	print("50%")
	pwm.ChangeDutyCycle(50)  # Duty cycle is now 50%
	time.sleep(2)          # 0.5 seconds till the next change

	print("80%")
	pwm.ChangeDutyCycle(80)  # Duty cycle is now 80%
	time.sleep(2)          # 0.5 seconds till the next change

	print("100%")
	pwm.ChangeDutyCycle(100) # Duty cycle is now 100%
	time.sleep(2)          # 0.5 seconds till the next change

	print("50 at 5.5Hz for 3 seconds")
	pwm.ChangeFrequency(2000) # Frequency is now 5.5 Hz
	pwm.ChangeDutyCycle(50)  # Duty cycle is now 50%
	time.sleep(3)            # Three seconds till the next change

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def off():
	GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.HIGH)
        GPIO.output(13, GPIO.HIGH)


def loop():
	while True:
		time.sleep(1)

def destroy():
	pwm.stop()
	off()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		cycle()
		loop()
	except KeyboardInterrupt:
		destroy()

