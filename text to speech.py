from tkinter import *
from gtts import gTTS
import os
from playsound import playsound

message = input("Enter the yext you want to change to audio: ")
audio = gTTS(text = msg, lang = "en", slow = False)
audio.save("example.mp3")
os.system("start example.mp3")

root = Tk()
root.geometry("400x400")
root.configure(bg = "ghost white")
root.title("Text To Speech")

Label(root, text = "Text To Speech", font = "arial 15 bold", bg = "white smoke").pack()
Label(text = "Hello There", font = "arial 15 bold", bg = "white smoke", width = "20").pack(side = BOTTOM)

Label(root, text = "Enter text: ", font = "arial 15 bold", bg = "White smoke").place(x=20, y=60)

Msg = StringVar()

entry_field = Entry(root, textvariable = Msg, width = "60")
entry_field.place(x=20, y=100)

def Text_to_speech():
    message = entry_field.get()#input("Enter the yext you want to change to audio: ")
    speech = gTTS(text = message)
    speech.save("example.mp3")
    playsount("start example.mp3")
def Exit():
    root.destroy()
def Reset():
    Msg.set("")
Button(root, text = "Play", font = "arial 15 bold", command = Text_to_speech, width = "4").place(x=25, y=140)
Button(root, text = "Exit", font = "arial 15 bold", command = Exit, width = "4").place(x=100, y=140)
Button(root, text = "Reset", font = "arial 15 bold", command = Reset, width = "4").place(x=175, y=140)
root.mainloop()


