from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

blue = LED(2)
green = LED(3)
red = LED(4)

win = Tk()
win.title("LED GUI Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")


def ledToggleBlue():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "Turn Blue LED on"
    else:
        blue.on()
        blueButton["text"] = "Turn Blue LED off"

def ledToggleRed():
    if red.is_lit:
        red.off()
        redButton["text"] = "Turn Red LED on"
    else:
        red.on()
        redButton["text"] = "Turn Red LED off"
        
def ledToggleGreen():
    if green.is_lit:
        green.off()
        greenButton["text"] = "Turn Green LED on"
    else:
        green.on()
        greenButton["text"] = "Turn Green LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()


blueButton = Button(win, text = 'Turn Blue LED on', font = myFont, command = ledToggleBlue, bg = 'blue', height = 1, width = 24)
blueButton.grid(row=0,column=1)

redButton = Button(win, text = 'Turn Red LED on', font = myFont, command = ledToggleRed, bg = 'red', height = 1, width = 24)
redButton.grid(row=1,column=1)

greenButton = Button(win, text = 'Turn Green LED on', font = myFont, command = ledToggleGreen, bg = 'green', height = 1, width = 24)
greenButton.grid(row=2,column=1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red2', height = 1, width = 6)
exitButton.grid(row=3,column=1)
