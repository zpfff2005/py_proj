from pynput.keyboard import Key, Controller
import time
a, b = input().split(' ')
time.sleep(2)
keyboard = Controller()
if a == '0':
	while True:
		keyboard.type(b + '\n')
		time.sleep(0.1)
else:
	for i in range(int(a)):
		keyboard.type(b + '\n')
		time.sleep(0.1)
