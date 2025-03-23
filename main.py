from tkinter import *
from playsound import playsound
import time


#To create interface
root=Tk()
root.title("ContdownTimer")
root.geometry("400x600")
root.config(bg="white")
root.resizable(False,False)


#to create heading Label-CountDown,timer
Heading1=Label(root,text="COUNTDOWN",bg="white",fg="black",font="arial 32 bold")
Heading1.pack(pady=5)
Heading2=Label(root,text="TIMER",bg="white",fg="black",font="arial 30 bold")
Heading2.pack(pady=5)

#to create label as current time
Label(root,text="CurrentTime:",bg="papayawhip",font="arial 15 bold").place(x=70,y=150)

#clock time interface (eg=20:37:20PM) with suitable location
def clock():
    clock_time=time.strftime('%H:%M:%S %p')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)

 
current_time=Label(root,text="",font="arial 15 bold",bg="white",fg="black")
current_time.place(x=200,y=150)
clock()

#timer
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 50",bd=0).place(x=30,y=200)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 50",bd=0).place(x=150,y=200)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec,width=2,font="arial 50",bd=0).place(x=270,y=200)
sec.set("00")

#to ceate label hours,mins,secs
Label(root,text="hours",fg="black",bg="white",font="arial 12 bold").place(x=102,y=223)

Label(root,text="mins",fg="black",bg="white",font="arial 12 bold").place(x=225,y=223)

Label(root,text="secs",fg="black",bg="white",font="arial 12 bold").place(x=345,y=223)

def Timer():
    times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())

    while times > -1:
        minute,second=(times//60,times%60)

        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        root.update()
        time.sleep(1)

        if times==0:
            playsound("alert.mp3")
            sec.set("00")
            mins.set("00")
            hrs.set("00")
        times -= 1    
            
    

#to create a start Button
button=Button(root,text="Start",height=1,fg="black",bg="red",font="arial 15 bold",command=Timer)
button.pack(padx=5,pady=40,side=BOTTOM)

def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")


def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

    
 
Image1=PhotoImage(file="brush.png")
button1=Button(root,image=Image1,bg="white",bd=0,command=brush)
button1.place(x=7,y=300)


Image2=PhotoImage(file="eggs.png")
button2=Button(root,image=Image2,bg="white",bd=0,command=eggs)
button2.place(x=137,y=300)

Image3=PhotoImage(file="face.png")
button3=Button(root,image=Image3,bg="white",bd=0,command=face)
button3.place(x=267,y=300)


root.mainloop()

