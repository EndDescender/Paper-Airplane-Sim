#!/usr/bin/python3

import sys
import socket
import math
from tkinter import *

#-------------------------------------------
# Getting the port number of the local server, connects variables to sim 

if ( len(sys.argv) == 2) :
    trick_varserver_port = int(sys.argv[1])
else:
    print("usage: vsclient <port_number>")
    sys.exit()


#-----------------------------------
# Dimensions to variables in the graphics window

HEIGHT, WIDTH = 600,900
MARGIN = 20
SCALE = 15
ovalRadius = 20 #originally planned on a polygon, was scrapped later as tkinter 
                #did not like polygons moving

#-----------------------------------
# Values for when the sim is in either run or freeze mode.

MODE_FREEZE = 1
MODE_RUN = 5

#-----------------------------------
# Sets launch to false, freezing the simulation at first.

launchCommand = False
def planeLaunch():
    global launchCommand
    launchCommand = True
    
#-----------------------------------
# making the display

tk = Tk()
canvas = Canvas(tk, width = WIDTH, height = HEIGHT, bg="light blue")
tk.title("Paper Plane Display")
canvas.pack()


buttonFrame = Frame()
buttonFrame.pack(side=BOTTOM)
launchButton = Button(buttonFrame,text="THROW",command=planeLaunch)
launchButton.pack(side=LEFT)

# The scales
speedScale = Scale(buttonFrame, from_=5, to=100, label="Initial Speed", orient=HORIZONTAL, activebackground= "yellow")
speedScale.pack(side=LEFT)
speedScale.set(20)

angleScale = Scale(buttonFrame, from_=0, to=46, label="Initial Angle", orient=HORIZONTAL, activebackground= "green")
angleScale.pack(side = RIGHT)
angleScale.set(0)

# Made the mass scale more precise and longer for more comfort and more realistic values.
massScale = Scale(buttonFrame, from_=.05, to=5, label = "Mass", orient = HORIZONTAL, digits=3, length= 120, 
resolution = .05, activebackground= "orange")
massScale.pack(side = RIGHT)

# The x and y axis lines
xAxis = canvas.create_line(MARGIN,HEIGHT-MARGIN,WIDTH,HEIGHT-MARGIN)
yAxis = canvas.create_line(MARGIN, HEIGHT-MARGIN, MARGIN, 0)

# The "Paper Airplane" represented by the super accurate oval 
paperPlane = canvas.create_oval(580,580, ovalRadius + 100, ovalRadius, fill = "red")

modeText = canvas.create_text(WIDTH/2, 20, text="--unknown-mode--")

# Text that shows the impact results
impactTimeText = canvas.create_text(WIDTH/2, 40, text = "")
impactPosText =  canvas.create_text(WIDTH/2, 60, text="")

#---------------------------------------------------------
# Connecting to the clinet server 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", trick_varserver_port))
insock = client_socket.makefile("r")

# Retreiveing variables, important to note that send argument needs .encode at the end
# in order to work with Python 3 as it now neeeds bytes, not strings.
client_socket.send( "trick.var_set_client_tag(\"myvsclient\") \n".encode("utf-8")) #the utf-8 is not necessary for it to work
client_socket.send( "trick.var_debug(3)\n".encode("utf-8") )
client_socket.send( "trick.var_pause()\n".encode("utf-8") )
client_socket.send( "trick.var_ascii()\n".encode("utf-8") )
client_socket.send( ("trick.var_add(\"dyn.paperPlane.pos[0]\") \n" +
                    "trick.var_add(\"dyn.paperPlane.pos[1]\") \n" +
                    "trick.var_add(\"trick_sys.sched.mode\")\n" +
                    "trick.var_add(\"dyn.paperPlane.impact\") \n" +
                    "trick.var_add(\"dyn.paperPlane.impactTime\") \n").encode("utf-8"))
client_socket.send( "trick.var_unpause()\n".encode("utf-8") )


# Implementing gathered values into updating the simulation. 
# Will continue untill the simulation ends
while(True):

    line = insock.readline()
    if line == "":
        break

    field = line.split("\t")

    x,y = float(field[1]), float(field[2])
    cx,cy = (x*SCALE+MARGIN), (HEIGHT-y*SCALE-MARGIN) 
    canvas.coords(paperPlane, cx - ovalRadius, cy - ovalRadius, cx + ovalRadius, cy + ovalRadius) 

#--------------------------------------
# Tells simulation what to do in freeze or run mode, also adds to the display details of which mode it is in.
# This process involves updating information from the user input in the display to the respective modules that take the data. 

    simMode = int(field[3])
    if simMode == MODE_FREEZE:
        canvas.itemconfigure(modeText, fill="blue", text="FREEZE")
    elif simMode == MODE_RUN:
        canvas.itemconfigure(modeText, fill="red", text="RUN")
    else:
        canvas.itemconfigure(modeText, text="--unknown-mode--")

    impact = int(field[4])
    if simMode == MODE_RUN:
        if impact:
        
            canvas.itemconfigure(impactTimeText, text="Impact time = " + field[5])
            canvas.itemconfigure(impactPosText, text="Impact pos  = (" + field[1] + "," + field[2] + ")")
            client_socket.send( "trick.exec_freeze()\n".encode("utf-8"))
            client_socket.send(("dyn.paperPlane.pos[1] = " + str(0) + " \n").encode()) 

    if simMode == MODE_FREEZE:
        if launchCommand:
            launchCommand = False
            launchButton.config(state=DISABLED)
            
            client_socket.send( ("dyn.paperPlane.init_speed = " + str(speedScale.get()) + " \n").encode("utf-8"))                
            client_socket.send( ("dyn.paperPlane.angleDeg = " + str(angleScale.get()) + " \n").encode("utf-8"))
            client_socket.send( ("dyn.paperPlane.mass = " + str(massScale.get())+ " \n").encode())
            
            client_socket.send( "dyn.paperPlane.default_data()\n".encode()) #This line is dependent on how you have the default
            #or initial data set up. Ours was a module so we referenced it the same as the others.
            
            #runs the simulation
            client_socket.send( "trick.exec_run()\n".encode())

    tk.update()

tk.mainloop()
