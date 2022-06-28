import re, traceback
import win32gui, win32con, win32com.client
from time import sleep
import pythoncom

class cWindow:
    def __init__(self):
        self._hwnd = None
        self.shell = None
        self._numeroventanascargadas=0

    def BringToTop(self):
        win32gui.BringWindowToTop(self._hwnd)

    def SetAsForegroundWindow(self):
        self.shell = win32com.client.Dispatch("WScript.Shell")
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

    def numeroventanascargadas(self):
        self._numeroventanascargadas+=1
        return self._numeroventanascargadas

def optenerdatosventana(ventana,accname):
    
    try:
        wildcard = ventana
        commandWindows = cWindow()
        #cW.kill_task_manager()
        commandWindows.find_window_wildcard(wildcard)
        #cW.Maximize()        
        #cW.BringToTop()
        #cW.SetAsForegroundWindow()
        return(commandWindows)
    except:
        traceback.format_exc()
        print(traceback.format_exc(),"/n", accname)


def hacerfocusenlaventana(cWindow,commandWindows, accname):
    
    try:
        commandWindows.Maximize()
        commandWindows.BringToTop()        
        commandWindows.SetAsForegroundWindow()
        return True
        
    except:
        traceback.format_exc()
        print("Error al hacer focus en la ventana :","/n", accname)
        exit()


def main3(cW):
    sleep(1)
    try:
        cW.setActWin()
        #cW.Maximize()
        cW.SetAsForegroundWindow()
        cW.valor()
        
        
    except:
        f = open("log.txt", "w")
        f.write(traceback.format_exc())
        print(traceback.format_exc())

#    a=main2()
#    print(a.valor())
#    main3(a)
#    main3(a)
#    main3(a)
#    main3(a)