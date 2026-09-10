from time import sleep
import MTECH_GPIO as GPIO

'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class5
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

GPIO.setmode(GPIO.BCM)
outPin = 21
GPIO.setup(outPin, GPIO.OUT)


def main():
	repeat = True
	while(repeat):
		text = input("--Press 'y' to turn on the LED, 'n' to turn it off, or 'q' to quit.--")
		if text == 'y':
			GPIO.output( outPin,1)
		elif text == 'n':
			GPIO.output( outPin,0)
		elif text == 'q':
			text = False
			GPIO.cleanup()
		else:
			print("Input not recongnized. Try again")
if __name__ == "__main__":
	main()
