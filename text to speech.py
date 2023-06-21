import tkinter as tk
from tkinter import *
import pyttsx

engine=pyttsx3.init()
def speaknow():
     engine.say(textv.get())
     engine.runAendWait()
     engine.stop()
rot=Tk()
textv=StringVar()

obj=LabelFramw(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="Yes",padx=10,pady=10)

lbl=Label(obj,text="text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="speak",fot=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

root.title("Text to speech")
root.geometry("400*200")
root.resizable(False,False)
root.mainloop()