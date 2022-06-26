import re, traceback
import win32gui, win32con, win32com.client
from time import sleep
import pythoncom

class cWindow:
    def __init__(self):
        pythoncom.CoInitialize()
        self.hwnd = None
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def BringToTop(self):
        win32gui.BringWindowToTop(self.hwnd)

    def SetAsForegroundWindow(self):
        self.shell.SendKeys('%')
        win32gui.SetForegroundWindow(self.hwnd)

    def Maximize(self):
        win32gui.ShowWindow(self.hwnd,win32con.SW_MAXIMIZE)

    def setActWin(self):
        win32gui.SetActiveWindow(self.hwnd)

    def window_enum_callback(self, hwnd, wildcard):
        '''Pass to win32gui.EnumWindows() to check all the opened windows'''
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self.hwnd = hwnd
                     

    def find_window_wildcard(self, wildcard):
        self.hwnd = None
        win32gui.EnumWindows(self.window_enum_callback, wildcard)
         
        return self.hwnd
    def kill_task_manager(self):
        wildcard = 'Gestionnaire des t.+ches de Windows'
        self.find_window_wildcard(wildcard)
        if self.hwnd:
            win32gui.PostMessage(self.hwnd, win32con.WM_CLOSE, 0, 0)
            sleep(0.5)
    def valor (self):
        valor= (self.hwnd)
        return valor
def main1(nombreventa):
    sleep(1)
    try:
        wildcard = nombreventa
        cW = cWindow()

        #cW.kill_task_manager()
        cW.find_window_wildcard(wildcard)
        cW.Maximize()        
        #cW.BringToTop()
        
        cW.SetAsForegroundWindow()

    except:
        f = open("log.txt", "w")
        f.write(traceback.format_exc())
        print(traceback.format_exc())

def main2(nombreventana):
    
    try:
        wildcard = nombreventana
        cW = cWindow()
        #cW.kill_task_manager()
        cW.find_window_wildcard(wildcard)
        
        #cW.Maximize()
        cW.SetAsForegroundWindow()
        return cW
        
    except:
        f = open("log.txt", "w")
        f.write(traceback.format_exc())
        print(traceback.format_exc())
        return "texttoo"


def main3(cW):
    sleep(5)
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