
import pygetwindow as gw

class cWindow:
    def __init__(self,accname):
        self.url = str.lower(accname)+'.com'
        self.cW=None

    def find_window(self ):
        self.cW= gw.getWindowsWithTitle(self.url)[0]


    def setActWin(self):
        self.cW.activate()


