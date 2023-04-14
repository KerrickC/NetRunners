from pynput import mouse
import pyautogui
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *

# TODO: create shortcuts for start monitoring and upload file
    # [ ] - Decide on keyboard input
    # [ ] - Create functionality for start monitoring
    # [ ] - Create functionality for upload file

# TODO: change play button to pause button when selected and create stop listener functionality
    # [ ] - Implement icon change on mouse click
    # [ ] - If pause button is clicked, stop listener

# TODO: FIX INPUT ISSUE
# ISSUE: text seems to only be inputted if input field is selected before listener is started and then clicked again
# [X] - Added additional mouse click

# Quick meeting notes:
# - rc file, store previous window size, ...
# - create a file on the target VM (right click start monitor to bring up different options)
# - encoding
# - requirements.txt (>= versions)
# - download file with QR code generator (find python generator)
# - Use PyCharm for PEP style


class GUI(QMainWindow):
    lines = ""

    def __init__(self):
        super(GUI, self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.Browser)
        self.showNormal()

        NavBar = QToolBar()
        self.addToolBar(NavBar)

        # Select File
        pixmapi = QStyle.StandardPixmap.SP_FileDialogStart
        icon = self.style().standardIcon(pixmapi)
        SelectFile = QAction(QIcon(icon), 'Select File', self)
        SelectFile.triggered.connect(self.FileSelector)
        NavBar.addAction(SelectFile)

        # Start monitoring for next mouse click
        pixmapi = QStyle.StandardPixmap.SP_MediaPlay
        icon = self.style().standardIcon(pixmapi)
        StartMonitoring = QAction(QIcon(icon), 'Start Monitoring', self)
        StartMonitoring.triggered.connect(self.StartMonitor)
        NavBar.addAction(StartMonitoring)

        # Browser back button
        pixmapi = QStyle.StandardPixmap.SP_ArrowBack
        icon = self.style().standardIcon(pixmapi)
        BackButton = QAction(QIcon(icon), 'Back', self)
        BackButton.triggered.connect(self.Browser.back)
        NavBar.addAction(BackButton)

        # Browser forward button
        pixmapi = QStyle.StandardPixmap.SP_ArrowForward
        icon = self.style().standardIcon(pixmapi)
        ForwardButton = QAction(QIcon(icon), 'Forward', self)
        ForwardButton.triggered.connect(self.Browser.forward)
        NavBar.addAction(ForwardButton)

        # Browser reload button
        pixmapi = QStyle.StandardPixmap.SP_BrowserReload
        icon = self.style().standardIcon(pixmapi)
        ReloadButton = QAction(QIcon(icon), 'Reload', self)
        ReloadButton.triggered.connect(self.Browser.reload)
        NavBar.addAction(ReloadButton)

        self.UrlBar = QLineEdit()
        self.UrlBar.returnPressed.connect(self.NavigateToUrl)

        NavBar.addWidget(self.UrlBar)
        self.Browser.urlChanged.connect(self.UpdateUrl)

    def FileSelector(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Text Files (*.txt)", options=options)
        if file:
            print(file)
            self.ReadFile(file)

    def ReadFile(self, file):
        with open(file) as f:
            self.lines = f.read()
            print(self.lines)

    def NavigateToUrl(self):
        Url = self.UrlBar.text()
        self.Browser.setUrl(QUrl(Url))

    def UpdateUrl(self, p):
        p = str(p).removeprefix("PyQt5.QtCore.QUrl('")
        p = str(p).removesuffix("')")

        if p == "about:blank":
            p = "https://www.google.com/"
            self.UrlBar.setText(str(p))
            self.NavigateToUrl()
        else:
            self.UrlBar.setText(str(p))

    def on_click(self, x, y, button, pressed):
        mouse.Listener.stop
        if pressed:
            print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
            pyautogui.write(self.lines)

            # Stop listener
            return False

    def StartMonitor(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()


app = QApplication(sys.argv)
QApplication.setApplicationName('NetRunners')
window = GUI()
app.exec()
