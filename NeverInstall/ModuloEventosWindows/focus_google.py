import re, traceback
from unittest import result
import win32gui, win32con, win32com.client
from time import sleep
import pythoncom

class cWindow:
    def __init__(self):
        self._hwnd = None
        self.shell = win32com.client.Dispatch("WScript.Shell",pythoncom.CoInitialize())
    def BringToTop(self):
        win32gui.BringWindowToTop(self._hwnd)

    def SetAsForegroundWindow(self):
        
        self.shell.SendKeys('%')
        win32gui.SetForegroundWindow(self._hwnd)

    def Maximize(self):
        win32gui.ShowWindow(self._hwnd, win32con.SW_MAXIMIZE)

    def setActWin(self):
        win32gui.SetActiveWindow(self._hwnd)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._hwnd = hwnd
            

    def find_window_wildcard(self, wildcard):
        self._hwnd = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
    def kill_task_manager(self):
        wildcard = 'Gestionnaire des t.+ches de Windows'
        self.find_window_wildcard(wildcard)
        if self._hwnd:
            win32gui.PostMessage(self._hwnd, win32con.WM_CLOSE, 0, 0)
            sleep(0.5)

    def valorhwnd (self):
        valor= (self._hwnd)
        return valor

    def hacerfocusenlaventana(self, accname):
    
        try:
            self.Maximize()
            self.BringToTop()        
            self.SetAsForegroundWindow()
            return True
        
        except:
            traceback.format_exc()
            print(traceback.format_exc(),"Error al hacer focus en la ventana :","/n", accname)
            exit()


