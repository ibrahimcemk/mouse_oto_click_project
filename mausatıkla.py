import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="x")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.001)    
        
        
        
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking
        
        
clicking_thread = threading.Thread(target=clicker)
clicking_thread.start()



with Listener(on_press=toggle_event) as listener:
    listener.join()       
    
    input("break")    