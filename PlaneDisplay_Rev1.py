#!/usr/bin/python3

import sys
import socket
import math
from tkinter import *

from signal import signal, SIGPIPE, SIG_DFL  
signal(SIGPIPE,SIG_DFL)

#-----------------------------------

if ( len(sys.argv) == 2) :
    trick_varserver_port = int(sys.argv[1])
else:
    print("usage: vsclient <port_number>")
    sys.exit()


#-----------------------------------

HEIGHT, WIDTH = 600,900
MARGIN = 20
SCALE = 3
ballRadius = 20

#-----------------------------------

MODE_FREEZE = 1
MODE_RUN = 5

#-----------------------------------

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
launchButton = Button(buttonFrame,text="launch",command=planeLaunch)
launchButton.pack(side=LEFT)

speedScale = Scale(buttonFrame, from_=5, to=100, label="Initial Speed", orient=HORIZONTAL)
speedScale.pack(side=LEFT)
speedScale.set(20)

angleScale = Scale(buttonFrame, from_=0, to=46, label="Initial Angle", orient=HORIZONTAL)
angleScale.pack(side = RIGHT)
angleScale.set(0)

xAxis = canvas.create_line(MARGIN,HEIGHT-MARGIN,WIDTH,HEIGHT-MARGIN)
yAxis = canvas.create_line(MARGIN, HEIGHT-MARGIN, MARGIN, 0)

paperPlane = canvas.create_oval(580,580, ballRadius, ballRadius, fill = "red")

modeText = canvas.create_text(WIDTH/2, 20, text="--unknown-mode--")

impactTimeText = canvas.create_text(WIDTH/2, 40, text = "")
impactPosText =  canvas.create_text(WIDTH/2, 60, text="")

#----------------------------------------------------------------
#connecting to the client variable server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", trick_varserver_port))
insock = client_socket.makefile("r")

client_socket.send( "trick.var_set_client_tag(\"myvsclient\") \n".encode("utf-8"))
client_socket.send( "trick.var_debug(3)\n".encode("utf-8") )
client_socket.send( "trick.var_pause()\n".encode("utf-8") )
client_socket.send( "trick.var_ascii()\n".encode("utf-8") )
client_socket.send( ("trick.var_add(\"dyn.paperPlane.pos[0]\") \n" +
                    "trick.var_add(\"dyn.paperPlane.pos[1]\") \n" +
                    "trick.var_add(\"trick_sys.sched.mode\")\n" +
                    "trick.var_add(\"dyn.paperPlane.impact\") \n" +
                    "trick.var_add(\"dyn.paperPlane.impactTime\") \n").encode("utf-8"))
client_socket.send( "trick.var_unpause()\n".encode("utf-8") )

while(True):

    line = insock.readline()
    field = line.split("\t")
    x,y = float(field[1]), float(field[2])
    cx,cy = (x*SCALE+MARGIN), (HEIGHT-y*SCALE-MARGIN) 
    canvas.coords(paperPlane, cx - ballRadius, cy - ballRadius, cx + ballRadius, cy + ballRadius) #this shi is broken, try the ball radius method

    # info on whether the sim is in freeze or run mode

    simMode = int(field[3])
    if simMode == MODE_FREEZE:
        canvas.itemconfigure(modeText, fill="blue", text="FREEZE")
    elif simMode == MODE_RUN:
        canvas.itemconfigure(modeText, fill="red", text="RUN")
    else:
        canvas.itemconfigure(modeText, text="--unknown-mode--")

    #suppose to inform on impact time and postion, doesn't work atm

    impact = int(field[4])
    if simMode == MODE_RUN:
        if impact:
        
            canvas.itemconfigure(impactTimeText, text="Impact time = " + field[5])
            canvas.itemconfigure(impactPosText, text="Impact pos  = (" + field[1] + "," + field[2] + ")")
            client_socket.send( "trick.exec_freeze()\n".encode("utf-8"))

    if simMode == MODE_FREEZE:
        if launchCommand:
            launchCommand = False
            launchButton.config(state=DISABLED)
            
            client_socket.send( "dyn.paperPlane.init_speed = " + str(speedScale.get()) + " \n".encode())                
            client_socket.send( "dyn.paperPlane.angleDeg = " + str(angleScale.get()*(math.pi/180.0)) + " \n".encode())
            
            client_socket.send( "trick.paperPlane_init( dyn.paperPlane )\n")
            
            client_socket.send( "trick.exec_run()\n")

    tk.update()

    tk.mainloop()