from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM)


red_Led = LED(14)
yellow_Led = LED(15)
green_Led = LED(18)

win = Tk()
win.title("LED Control")
myFont = tkinter.font.Font(family = 'Helveticq', size = 12, weight = 'bold')

def RedLED():
    if red_Led.is_lit:
       red_Led.off()
       RedledButton["text"] = "Turn on red led"
    else:
        red_Led.on()
        RedledButton["text"] = "Turn off red led"
        yellow_Led.off()
        YellowledButton["text"] = "Turn on yellow led"
        green_Led.off()
        GreenledButton["text"] = "Turn on green led"

def YellowLED():
    if yellow_Led.is_lit:
        yellow_Led.off()
        YellowledButton["text"] = "Turn on yellow led"
    else:
        yellow_Led.on()
        YellowledButton["text"] = "Turn off yellow led"
        yellow_Led.off()
        RedledButton["text"] = "Turn on red led"
        green_Led.off()
        GreenledButton["text"] = "Turn on green led"

def GreenLED():
    if green_Led.is_lit:
       green_Led.off()
       GreenledButton["text"] = "Turn on green led"
    else:
        green_Led.on()
        GreenledButton["text"] = "Turn off green led"
        yellow_Led.off()
        YellowledButton["text"] = "Turn on yellow led"
        red_Led.off()
        RedledButton["text"] = "Turn on red led"


def close():

    RPi.GPIO.cleanup()
    win.destroy()



RedledButton = Button(win, text='Turn led on red led', font=myFont, command=RedLED, bg='bisque2', height=1, width=24)
RedledButton.grid(row=0, column=1)
YellowledButton = Button(win, text='Turn led on yellow led', font=myFont, command=YellowLED, bg='bisque2', height=1, width=24)
YellowledButton.grid(row=1, column=1)
GreenledButton = Button(win, text='Turn led on green led', font=myFont, command=GreenLED, bg='bisque2', height=1, width=24)
GreenledButton.grid(row=2, column=1)
ExistledButton = Button(win, text='EXIST', font=myFont, command=close, bg='red', height=1, width=6)
ExistledButton.grid(row=3, column=1)
win.mainloop()
