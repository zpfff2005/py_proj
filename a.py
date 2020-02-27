from pynput.mouse import Button, Controller
import time
a = input()
time.sleep(4)
mouse = Controller()
if a == '0':
	while True:
		mouse.press(Button.left)
		mouse.release(Button.left)
		time.sleep(0.005)
else:
	for i in range(int(a)):
		mouse.press(Button.left)
		mouse.release(Button.left)
		time.sleep(0.005)