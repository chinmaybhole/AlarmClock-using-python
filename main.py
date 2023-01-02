from tkinter import *
import datetime
import time
import winsound
from threading import *

# Create Object
alarm_clock = Tk()
alarm_clock.title('Beep beep wake up!')
icon1 = PhotoImage(file='media/alarm-clock.png')
bg1 = PhotoImage(file='media/tni8FoSvQOw.png')
label1 = Label(alarm_clock, image=bg1)
label1.place(x=0, y=0)
alarm_clock.iconphoto(False, icon1)

# Set geometry
alarm_clock.geometry("400x200")


# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()


def alarm():
    # Infintite Loop
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one seconds
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("media/blast.wav", winsound.SND_ASYNC)
            break


# Add Labels, Frame, Button, Option menus
Label(alarm_clock, text="Alarm Clock", font=("Helvetica 20 bold"),
      bg='light blue', fg="green").pack(pady=10)
Label(alarm_clock, text="Set Time", font=(
    "Helvetica 15 bold"), bg='light blue', fg="green").pack()

frame = Frame(alarm_clock)
frame.pack()

hour = StringVar(alarm_clock)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
         )
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(alarm_clock)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(alarm_clock)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(alarm_clock, text="Set Alarm", font=("Helvetica 15"), bg='light blue', fg="purple", command=Threading).pack(
    pady=20)

# Execute Tkinter
alarm_clock.mainloop()
