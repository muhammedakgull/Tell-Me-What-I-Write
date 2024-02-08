import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root=Tk()
root.title("Tell Me What I Write")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#5270ff")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    
    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()   
            
    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()
            
def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    
    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, "text.mp3")
            engine.runAndWait()   
            
    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()




image_icon=PhotoImage(file="1391034.png")
root.iconphoto(False,image_icon)


Top_Frame=Frame(root,bg="#aaffff",width=900,height=100)
Top_Frame.place(x=0,y=0)

Logo=PhotoImage(file="mikrafon.png")
Label(Top_Frame,image=Logo,bg="#aaffff").place(x=-20,y=-50)

Label(Top_Frame,text="TELL ME WHAT I WRITE",font="arial 25 bold",bg="#aaffff",fg="black").place(x=135,y=30)

#####

text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#5270ff",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#5270ff",fg="white").place(x=755,y=160)

gender_combobox=Combobox(root,values=['Female','Male'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')
speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')


image_icon=PhotoImage(file="image (1).png")
btn=Button(root,text=" Speak",compound=LEFT,image=image_icon,width=130,bg="#Fffd7d",font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)

image_icon2=PhotoImage(file="speak2.png")
save=Button(root,text=" Save",compound=LEFT,image=image_icon2,width=130,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=730,y=280)


root.mainloop()