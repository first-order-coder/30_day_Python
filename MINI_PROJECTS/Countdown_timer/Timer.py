import time
from tkinter import *
from tkinter import messagebox

### Create Interface 

clockWindow = Tk()
clockWindow.geometry("500x500")
clockWindow.configure(background='green')
clockWindow.title(" COUNTDOWN TIMER")

hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

hourString.set("00")
minuteString.set("00")
secondString.set("00")

''' using Entry() will give you chance to insert values in to text boxes and using textvariable will take the input to the assigned 
    string value '''

hourTextbox = Entry(clockWindow, width=3, font=('Calibri', 20, ''), textvariable=hourString)
minuteTextbox = Entry(clockWindow, width=3, font=('Calibri', 20, ''), textvariable=minuteString)
secondTextbox = Entry(clockWindow, width=3, font=('Calibri', 20, ''), textvariable=secondString)

'center textboxes'
hourTextbox.place( x=170, y=180 )
secondTextbox.place( x=220, y=180 )
minuteTextbox.place( x=270, y=180 )

def rumTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())

    except:
        print('Invalid Input') 

    while(clockTime > -1):
        
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if( totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)
        
        hourString.set("{0:2d}" .format(totalHours))
        minuteString.set("{0:2d}" .format(totalMinutes))
        secondString.set("{0:2d}" .format(totalSeconds))
    
    ### Update the interface

    clockWindow.update()
    time.sleep(1)

    if (clockTime == 0):
        messagebox.showinfo("", ' Time Expiered ')

    clockTime =-1

setTimeButton = Button(clockWindow, text='Set Time', bd= '5', command=rumTimer)
setTimeButton.place(relx = 0.5, rely= 0.5, anchor= CENTER)

clockWindow.mainloop()

