from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:$S")
        date = current_time.strftime("%D/%M/%Y")
        #print("The Set Date is:",date)
        #print(now)
        if now == set_alarm_timer:
            print("Time to wake up")
            winsound.PlaySound("wake.mp3",windsound,SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}::{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock= Tk()
clock.title("Tobi's Alarm")
clock.iconbitmap(r"iretomiwa.jpg")
clock.geometry("400x200")
time_format= Label(clock, text= "Enter time in 24hours format!", fg= "red", bg = "black", font="arial").place(x=6,y=120)
addTime = Label(clock, text = "Hour Min Sec", font = 60).place(x=110)
setYourAlarm = Label(clock, text = "When to wake up", fg = "blue", relief = "solid", font = ("Arial",10,"bold")).place(x=0,y=29)

# The Variables needs initialization
hour = StringVar()
min = StringVar()
sec = StringVar()

#time required to set the alarm clock
hourTime = Entry(clock, textvariable = hour, bg = "red", width = 15).place(x=110,y=30)
minTime = Entry(clock, textvariable = min, bg = "red", width = 15).place(x=150,y=30)
secTime = Entry(clock, textvariable = sec, bg = "red", width = 15).place(x= 190,y=30)

submit = Button(clock, text = "Set Alarm", fg = "brown", width = 10, command = actual_time).place(x=110,y=70)
clock.mainloop()
