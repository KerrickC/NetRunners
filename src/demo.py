import tkinter as tk
import threading
from pynput.mouse import Listener
import pyautogui
import time


class GUI(object):
    def __init__(self):
        self.a = "Please focus on a text input..."
        self.w = tk.Label(root, text=self.a)
        self.w.pack()
        thread2 = threading.Thread(target=self.initMouseClickController)
        thread2.start()

    def update(self):
        self.w.config(text=self.a)

    def initMouseClickController(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def sendTextInput(text):
        time.sleep(1)
        pyautogui.typewrite(text)

    def on_click(self, x, y, button, pressed):
        # startKeyboardInput()
        self.w.config(text="Mouse Clicked!")
        self.sendTextInput("texttexttext")

# def main():
root = tk.Tk()
# title of window
root.title("DEMO")
# stick to top left
root.geometry("+0+0") 
# keep window on top
root.wm_attributes("-topmost", True)
# create new GUI instance
gui = GUI()

root.mainloop()




   