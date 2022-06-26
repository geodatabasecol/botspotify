import time
import win32gui
 
def loadwindowslist(hwnd, topwindows):
	topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))

def showwindowslist():
	topwindows = []
	win32gui.EnumWindows(loadwindowslist, topwindows)
	for hwin in topwindows:	
		sappname=str(hwin[1])
		nhwnd=hwin[0]
		print(str(nhwnd) + ": " + sappname)


def ventana(swinname):
	topwindows = []
	win32gui.EnumWindows(loadwindowslist, topwindows)
	for hwin in topwindows:	
		sappname=str(hwin[1])
		if swinname in sappname.lower():	
			nhwnd=hwin[0]
			return nhwnd

def abrirventana(idventana):
	win32gui.ShowWindow(idventana,5)
	win32gui.SetForegroundWindow(idventana)

valor=(ventana("facebook"))

time.sleep(10)
for i in range (0,20):
	if (ventana("facebook")):
		valor = (ventana("facebook"))
		print ("facebook",valor)
		abrirventana(valor)
	elif (ventana("rt")):
		valor = (ventana("rt"))
		print ("rt",valor)
		#abrirventana(valor)
	else :
		pass
	time.sleep(4)
	