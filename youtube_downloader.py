from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry("500x300")
window.resizable(0,0)
window.title("MY youtube downloader")

Label(window,text = "YouTube Downloader", font = "arial 20 bold").pack()

#placelink
link = StringVar()

Label(window, text = "Paste YouTube Link Here: ", font = "arial 15 bold").place(x=160,y=50)
lint_enter = Entry(window, width = 70,textvariable = link).place(x=32,y=90)

#download function to be used as command in button

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text = "Downloaded", font = "arial 15").place(x=180,y=210)

Button(window, text = "Download", font = "helvetica 15 bold",bg = "red", padx = 2, command = Downloader).place(x=180,y=150)

window.mainloop()
