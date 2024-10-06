import tkinter as tk
from tkinter import *
from tkinter import font
import random 
from random import choice,choices 

colour1 = "#020f12" 
colour2 = "#05d7ff"
colour3 = "#65e7ff"
colour4 = "BLACK"
missionCounter = 0
conquestCounter = 0

listMission = ["Claim all 6 squares around the starting hexagon +3 -2"
              , "Claim Ceres +2 -1","Claim Ceres +2 -1"
              , "Claim Eres +2 -1", "Claim Eres +2 -1"
              ,"Have an adjacent hexagon to your opponents starting hexagon +5 -2"
              ,"Become neighbors with your teammate +3 -3","Claim minimum 4 hexagons around Sirius +3 -2"
              ,"Claim Ceres and all surrounding hexagons +5 -3"
              ,"Claim Eres and all surrounding hexagons +5 -3"]
takenMissionA = []
takenMissionB = []

def randomMissionSelection():
    if not listMission:
        return "There is no mission left"
    
    takenMission = random.choice(listMission)
    listMission.remove(takenMission)

    return f"mission: {takenMission}"

def randomConquestSelection():
    listAward = ["Claim 1 hexagons"
                 ,"Claim 2 hexagons"
                 ,"Claim 3 hexagons"
                 ,"Claim 4 hexagons"
                 ,"Claim 5 hexagons"
                 ,"Claim 6 hexagons"
                 ,"Claim 7 hexagons"
                 ,"Your opponent has to give up control over 1 hexagon"
                 ,"Your opponent has to give up control over 2 hexagons"
                 ,"Your opponent has to give up control over 3 hexagons"
                 ,"Your opponent has to give up control over 1 hexagon and You can claim 1 hexagon"
                 ,"Your opponent has to give up control over 2 hexagons and You can claim 2 hexagons"
                 ,"Your team can sacrifice his control over maximum 3 hexagons giving you right to claim as much hexagons as the deleted hexagons "]
    listPunishment = ["Wait 1 Turn"
                 ,"No Penalty"
                 ,"Give up your control over 1 hexagon"
                 ,"Give up your control over 2 hexagons"
                 ,"Give up your control over 3 hexagons"
                 ,"Give up your control over 4 hexagons"
                 ,"Give up your control over 2 hexagons and Your Opponents can claim 2 hexagons"
                 ,"Your teammate has to give up control over 1 hexagon"
                 ,"Your teammate has to give up control over 3 hexagon"]
   
    x = f"1: {random.choices(listAward,weights=[10,10,9,9,6,4,2,10,7,4,5,3,3],k=1)} {random.choices(listPunishment,weights=[6,3,10,9,7,5,6,8,6],k=1)}"
    y = f"2: {random.choices(listAward,weights=[10,10,9,9,6,4,2,10,7,4,5,3,3],k=1)} {random.choices(listPunishment,weights=[6,3,10,9,7,5,6,8,6],k=1)}"
    z = f"3: {random.choices(listAward,weights=[10,10,9,9,6,4,2,10,7,4,5,3,3],k=1)} {random.choices(listPunishment,weights=[6,3,10,9,7,5,6,8,6],k=1)}"
    k = f"4: {random.choices(listAward,weights=[10,10,9,9,6,4,2,10,7,4,5,3,3],k=1)} {random.choices(listPunishment,weights=[6,3,10,9,7,5,6,8,6],k=1)}"
    l = f"5: {random.choices(listAward,weights=[10,10,9,9,6,4,2,10,7,4,5,3,3],k=1)} {random.choices(listPunishment,weights=[6,3,10,9,7,5,6,8,6],k=1)}"
    
    return f"{x}\n{y}\n{z}\n{k}\n{l}"

def resetConquest():
    newText = randomConquestSelection()
    lb3.config(text=newText)
    page4.tkraise()

def resetMission():
    newText2 = randomMissionSelection()
    lb2.config(text=newText2)
    updateMissionLog(newText2)
    page2.tkraise()

def addMission():
    global missionCounter
    missionCounter += 1
    resetMission()

def addConquest():
    global conquestCounter
    conquestCounter += 1
    page3.tkraise()

def updateMissionLog(mission):
    global missionCounter, conquestCounter

    totalCounter = missionCounter + conquestCounter

    if totalCounter % 2 == 1:
        takenMissionA.append(mission)
        lbA_Mission.config(text="\n".join(takenMissionA), anchor="w") 
    else:
        takenMissionB.append(mission)
        lbB_mission.config(text="\n".join(takenMissionB), anchor="w")  

win = tk.Tk()

style1 = font.Font(size=25)
style2 = font.Font(size=20)
style3 = font.Font(size=15)

page1 = Frame(win, bg=colour4)
page2 = Frame(win, bg=colour4)
page3 = Frame(win, bg=colour4)
page4 = Frame(win, bg=colour4)
page5 = Frame(win, bg=colour4)

page1.grid(row=0, column=0, sticky="nsew")
page2.grid(row=0, column=0, sticky="nsew")
page3.grid(row=0, column=0, sticky="nsew")
page4.grid(row=0, column=0, sticky="nsew")
page5.grid(row=0, column=0, sticky="nsew")

lb1 = Label(page1, text="Menu",
            font=style1,
            background=colour2,
            foreground=colour4)
lb1.pack(padx=500,pady=20)

lb2 = Label(page2, text="",
            font=style1,
            bg=colour1,
            fg="white",
            anchor=N)
lb2.pack(pady=20)

lb3 = Label(page4, text=randomConquestSelection(),
            font=style3,
            bg=colour1,
            fg="white")
lb3.pack(pady=50)

lb5 = Label(page5, text="Mission Log",
            font=style1,
            bg=colour1,
            fg="white")
lb5.pack(pady=20)

lbA = Label(page5, text="Red Team\n",
            font=style1,
            bg=colour1,
            fg="white")
lbA.pack(side=LEFT, padx=20)

lbA_Mission = Label(page5,
                  text="",
                  font=style3,
                  anchor="nw",
                  bg=colour1,
                  fg="white")
lbA_Mission.pack(side=LEFT, padx=20, pady=10)

lbB = Label(page5, text="Blue Team",
            font=style1,
            bg=colour1,
            fg="white")
lbB.pack(side=RIGHT, padx=20)

lbB_mission = Label(page5, text="",
                  font=style3,
                  anchor="nw",
                  bg=colour1,
                  fg="white")
lbB_mission.pack(side=RIGHT, padx=20, pady=10)

btn1 = Button(page1, text="Mission",
              command=addMission,
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3,
              anchor=CENTER)
btn1.pack()

btn2 = Button(page1, text="Claim",
              command=addConquest,
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3,
              anchor=CENTER)
btn2.pack()

btn3 = Button(page2, text="Return",
              command=lambda: page1.tkraise(),
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3)
btn3.pack()

btn4 = Button(page3, text="Return",
              command=lambda: page1.tkraise(),
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3,
              width=6, height=2)
btn4.pack()

btn5 = Button(page4, text="Return",
              command=lambda: page1.tkraise(),
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3)
btn5.pack()

btn6 = Button(page1, text="Mission log",
              command=lambda: page5.tkraise(),
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3,
              anchor=CENTER)
btn6.pack()

btn7 = Button(page5, text="Return",
              command=lambda: page1.tkraise(),
              font=style2,
              background=colour2,
              foreground=colour4,
              activebackground=colour3)
btn7.pack()

b1 = Button(page3, text="1",
            command=resetConquest,
            font=style2,
            bg=colour2,
            fg=colour4,
            width=5, height=2)
b1.pack()

b2 = Button(page3, text="2",
            command=resetConquest,
            font=style2,
            bg=colour2,
            fg=colour4,
            width=5, height=2)
b2.pack()

b3 = Button(page3, text="3",
            command=resetConquest,
            font=style2,
            bg=colour2,
            fg=colour4,
            width=5, height=2)
b3.pack()

b4 = Button(page3, text="4",
            command=resetConquest,
            font=style2,
            bg=colour2,
            fg=colour4,
            width=5, height=2)
b4.pack()

b5 = Button(page3, text="5",
            command=resetConquest,
            font=style2,
            bg=colour2,
            fg=colour4,
            width=5, height=2)
b5.pack()

b0 = Button(page3, text="miss",
            command=lambda: page1.tkraise(),
            font=style2,
            bg=colour2,
            fg=colour4,
            width=5, height=2)
b0.pack()


page1.tkraise()
win.configure(bg='BLACK')
win.geometry("1750x650")
win.title("HexaPace")
win.resizable(True,True)
win.mainloop()