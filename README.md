     def check_alarm(self)
         if self.alarm_active:
            current_time = datetime.now().strftime( '%H:%M:%S' )
            alarm_time_str = sdelf.alarm_entry.get()
            if current_time == alarm_time_str:
               print("Alarm!")
               self.alarm_active = False
         self.root.after(1000, self.check_alarm)
         
if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopApp(root)
    app.update_time()
    root.mainloop()
