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

