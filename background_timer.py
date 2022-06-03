import time
import keyboard

KEY = "p"
start = False
start_time = 0
end_time = 0

while(True):
    keyboard.wait(KEY)
    start = not start
    if start:
        start_time = time.time()
    else:
        end_time = time.time()
        print(end_time - start_time)
