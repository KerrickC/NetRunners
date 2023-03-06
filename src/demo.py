from tkinter import *
import webview
import threading
#from pynput.mouse import Listener

from pynput import mouse

import pyautogui
import time

import webbrowser

# class GUI(object):
#     def __init__(self):
#         self.a = "Please focus on a text input..."
#         self.w = tk.Label(root, text=self.a)
#         self.w.pack()
#         thread2 = threading.Thread(target=self.initMouseClickController)
#         thread2.start()

#     def update(self):
#         self.w.config(text=self.a)

#     def initMouseClickController(self):
#         with Listener(on_click=self.on_click) as listener:
#             listener.join()

#     def sendTextInput(self, text):
#         time.sleep(1)
#         pyautogui.typewrite(text)

#     def on_click(self, x, y, button, pressed):
#         # startKeyboardInput()
#         self.w.config(text="Mouse Clicked!")
#         self.sendTextInput("texttexttext")

# def main():
#root = Tk()
# title of window
#root.title("DEMO")
# stick to top left
# root.geometry("+0+0") 
# keep window on top
# root.wm_attributes("-topmost", True)
# create new GUI instance
# gui = GUI()

# root.mainloop()
  
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

# TODO: FIX INPUT ISSUE
# ISSUE: text seems to only be inputted if input field is selected
# before listener is started and then clicked again

class GUI(QMainWindow):
    lines = ""
    def __init__(self):
        super(GUI, self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.Browser)
        self.showMaximized()
        
        NavBar = QToolBar()
        self.addToolBar(NavBar)

        pixmapi = QStyle.StandardPixmap.SP_FileDialogStart
        icon = self.style().standardIcon(pixmapi)
        SelectFile = QAction(QIcon(icon), 'Select File', self)
        SelectFile.triggered.connect(self.FileSelector)
        NavBar.addAction(SelectFile)

        pixmapi = QStyle.StandardPixmap.SP_MediaPlay
        icon = self.style().standardIcon(pixmapi)
        StartMonitoring = QAction(QIcon(icon),'Start Monitoring', self)
        StartMonitoring.triggered.connect(self.StartMonitor)
        NavBar.addAction(StartMonitoring)

        pixmapi = QStyle.StandardPixmap.SP_ArrowBack
        icon = self.style().standardIcon(pixmapi)
        BackButton = QAction(QIcon(icon), 'Back', self)
        BackButton.triggered.connect(self.Browser.back)
        NavBar.addAction(BackButton)

        pixmapi = QStyle.StandardPixmap.SP_ArrowForward
        icon = self.style().standardIcon(pixmapi)
        ForwardButton = QAction(QIcon(icon), 'Forward', self)
        ForwardButton.triggered.connect(self.Browser.forward)
        NavBar.addAction(ForwardButton)

        pixmapi = QStyle.StandardPixmap.SP_BrowserReload
        icon = self.style().standardIcon(pixmapi)
        ReloadButton = QAction(QIcon(icon), 'Reload', self)
        ReloadButton.triggered.connect(self.Browser.reload)
        NavBar.addAction(ReloadButton)

        HomeButton = QAction('Home', self)
        HomeButton.triggered.connect(self.NavigateHome)
        NavBar.addAction(HomeButton)

        self.UrlBar = QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavigateToUrl)

        NavBar.addWidget(self.UrlBar)
        self.Browser.urlChanged.connect(self.UpdateUrl)

    def FileSelector(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        # Text files only (TODO: add functionality for other files)
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","Text Files (*.txt)", options=options)
        if file:
            print(file)
            self.ReadFile(file)

    def ReadFile(self, file):
        with open(file) as f:
            self.lines = f.read()
            print(self.lines)
            
    def NavigateHome(self):
        self.Browser.setUrl("http://google.com")

    def NavigateToUrl(self):
        Url = self.UrlBar.text()
        self.Browser.setUrl(QUrl('https://google.com'))

    def UpdateUrl(self, p):
        self.UrlBar.setText(str(p))
    
    def on_click(self, x, y, button, pressed):
        mouse.Listener.stop
        if pressed:
            print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

            # Maybe add another mouse click here to ensure the text box is actually being clicked
                # Seems to be windows issue
            
            #print (pyautogui.position().x)

            # Additional mouse click
            pyautogui.click(x, y)

            pyautogui.write(self.lines)
            # Stop listener           
            return False
            
    def StartMonitor(self):
        self.setStyleSheet("background-color:red")
        print(self)

        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

app = QApplication(sys.argv)
QApplication.setApplicationName('NetRunners')
window = GUI()
app.exec()