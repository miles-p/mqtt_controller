### YOU NEED TO CONFIGURE THIS STUFF ###

button_1_path = "The topic to publish Button 1's commands to"
button_2_path = "The topic to publish Button 2's commands to"
button_3_path = "The topic to publish Button 3's commands to"
button_4_path = "The topic to publish Button 4's commands to"



### SPECIAL SHIT ###
import paho.mqtt.client as mqtt
from tkinter import *

### INSTANCES AND DECLARATIONS AND OTHER THINGS ###
root = Tk()
client =mqtt.Client("")
#client.connect('YasawaPi')
host = StringVar()

### FUNCTIONS ###
def ON1():
    client.publish(button_1_path,"ON")
    print("SENT ON")
def OFF1():
    client.publish(button_1_path,"OFF")
    print("SENT OFF")
def ON2():
    client.publish(button_2_path,"ON")
    print("SENT ON")
def OFF2():
    client.publish(button_2_path,"OFF")
    print("SENT OFF")
def ON3():
    client.publish(button_3_path,"ON")
    print("SENT ON")
def OFF3():
    client.publish(button_3_path,"OFF")
    print("SENT OFF")
def ON4():
    client.publish(button_4_path,"ON")
    print("SENT ON")
def OFF4():
    client.publish(button_4_path,"OFF")
    print("SENT OFF")
def RECONNECT():
    client.connect(host.get())

### TKINTER TEXT & ENTRY DECLARATIONS ###
hostEntry = Entry(width=20, textvariable=host)
hostEntry.grid(row=0,column=0, columnspan=3)

### SPECIAL TKINTER BUTTON DECLARATIONS ###
# CONNECT BUTTON
connectButton = Button(root, text="CONNECT", width='7',command=RECONNECT)
connectButton.grid(row=0,column=3)
# STBD/1
r1ON = Button(root, text="1 ON", command=ON1, width='7')
r1ON.grid(row=2,column=0)
r1OFF = Button(root, text="1 OFF", command=OFF1, width='7')
r1OFF.grid(row=3,column=0)
# STBD/2
r2ON = Button(root, text="2 ON", command=ON2, width='7')
r2ON.grid(row=2,column=1)
r2OFF = Button(root, text="2 OFF", command=OFF2, width='7')
r2OFF.grid(row=3,column=1)
# STBD/3
r3ON = Button(root, text="3 ON", command=ON3, width='7')
r3ON.grid(row=2,column=2)
r3OFF = Button(root, text="3 OFF", command=OFF3, width='7')
r3OFF.grid(row=3,column=2)
# STBD/4
r4ON = Button(root, text="4 ON", command=ON4, width='7')
r4ON.grid(row=2,column=3)
r4OFF = Button(root, text="4 OFF", command=OFF4, width='7')
r4OFF.grid(row=3,column=3)
