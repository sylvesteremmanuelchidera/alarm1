import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import time

class DesktopApp:
    def __init__(self, root):
dsc

def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label['text'] = current_time
        self.root.after(1000, self.update_time)

    def update_stopwatch(self):
        if self.running:
            elapsed_time = datetime.now() - self.start_time
            stopwatch_time = str(elapsed_time).split(".")[0]
            self.stopwatch_label['text'] = stopwatch_time
        self.root.after(100, self.update_stopwatch)

    def toggle_stopwatch(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            if self.start_time is None:
                self.start_time = datetime.now()
            else:
                self.start_time += (datetime.now() - self.pause_time)

   def toggle_stopwatch(self):
        if self.running:
            self.running = False
        else:
            self.running = True
            if self.start_time is None:
                self.start_time = datetime.now()
            else:
                self.start_time += (datetime.now() - self.pause_time)

    def reset_stopwatch(self):
        self.start_time = None
        self.running = False
        self.stopwatch_label['text'] = "00:00:00"

    def set_alarm(self):
        alarm_time_str = self.alarm_entry.get()
        try:
            alarm_time = datetime.strptime(alarm_time_str, '%H:%M:%S')
            self.alarm_active = True
            self.check_alarm()
        except ValueError:
            print("Invalid time format. Please use HH:MM:SS")

