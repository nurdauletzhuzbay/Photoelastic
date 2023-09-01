from Tkinter import *
import subprocess
import os

def show_values(event):
    exposureValue = w1.get()
    focusVale = w2.get()
    saturationValue = w3.get()
    bashCommand = "v4l2-ctl -d /dev/video0 --set-ctrl=exposure_absolute=" + str(exposureValue) + ";" + "v4l2-ctl -d /dev/video0 --set-ctrl=focus_absolute=" + str(focusVale) + ";" + "v4l2-ctl -d /dev/video0 --set-ctrl=saturation=" +str(saturationValue)
    print(bashCommand)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()


bashCommandStart ="v4l2-ctl -d /dev/video0 --set-ctrl=focus_auto=0" + ";" + "v4l2-ctl -d /dev/video0 --set-ctrl=exposure_auto=1" + ";" + "v4l2-ctl -d /dev/video0 --set-ctrl=saturation=1"


process = subprocess.Popen(bashCommandStart.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

master = Tk()

w1 = Scale(master, from_=3, to=2047, length=800,tickinterval=100, orient=HORIZONTAL, command=show_values)
w1.pack()
w1.set(300)

w2 = Scale(master, from_=3, to=255, length=800,tickinterval=10, orient=HORIZONTAL, command=show_values)
w2.set(180)
w2.pack()

w3 = Scale(master, from_=3, to=255, length=800,tickinterval=10, orient=HORIZONTAL, command=show_values)
w3.set(255)
w3.pack()


mainloop()
