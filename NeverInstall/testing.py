from importlib.machinery import EXTENSION_SUFFIXES
import time
import pygetwindow as gw

#print(gw.getAllTitles())
#print(gw.getWindowsAt(10, 10))


notepadWindow = gw.getWindowsWithTitle('2.com')[0]
notepadWindow.activate()

time.sleep(1)
notepadWindow = gw.getWindowsWithTitle('3.com')[0]
notepadWindow.activate()

time.sleep(1)
notepadWindow = gw.getWindowsWithTitle('4.com')[0]
notepadWindow.activate()

time.sleep(1)
notepadWindow = gw.getWindowsWithTitle('5.com')[0]
notepadWindow.activate()

time.sleep(1)
notepadWindow = gw.getWindowsWithTitle('6.com')[0]
notepadWindow.activate()
time.sleep(1)
notepadWindow = gw.getWindowsWithTitle('2.com')[0]
notepadWindow.activate()