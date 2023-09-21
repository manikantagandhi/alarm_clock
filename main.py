import tkinter as tk
from datetime import datetime
from datetime import timedelta
import time
import pygame

pygame.mixer.init()

def set_alarm():
    alarm_time_str = entry.get()
    try:
        alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").time()
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS.")
    current_time = datetime.now().time()
    time_diff = timedelta(hours=alarm_time.hour, minutes=alarm_time.minute, seconds=alarm_time.second) - \
                timedelta(hours=current_time.hour, minutes=current_time.minute, seconds=current_time.second)
    if time_diff.total_seconds() > 0:
        print(f"Time until the alarm: {time_diff}")
        time.sleep(time_diff.total_seconds())

        pygame.mixer.music.load("y2mate.com - JAILER  Hukum Lyric Video  Superstar Rajinikanth  Sun Pictures  Anirudh  Nelson.mp3")
        pygame.mixer.music.play()
        set_button.place_forget()

    else:
        print("Invalid alarm time. Please enter a future time.")

def stop_alarm():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("250x250")
root.resizable(0,0)

label = tk.Label(root, text="Enter alarm time (HH:MM:SS):", pady=20, padx=20)
label.pack()

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm, pady=10, padx=10)
set_button.pack()

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm, pady=10, padx=10)
stop_button.pack()

root.mainloop()
