import tkinter as tk
import datetime

font_color_01 = "white"
font_color_02 = "black"

class CountdownApp:
    def __init__(self, root, target_time):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.attributes("-fullscreen", True)

        self.label = tk.Label(root, font=("Helvetica", 200), bg="black", fg=font_color_01)
        self.label.pack(expand=True, fill="both")

        self.target_time = target_time
        self.update()

        self.root.bind("<Escape>", self.exit_timer)  # Bind the Esc key to the exit_timer function

    def update(self):
        current_time = datetime.datetime.now()
        remaining_time = self.target_time - current_time

        if remaining_time <= datetime.timedelta(minutes=0):
            self.label.configure(bg="red", fg=font_color_01)
            self.label.config(text="OVER")
            break
        elif remaining_time <= datetime.timedelta(minutes=2):
            if int(remaining_time.total_seconds()) % 2 == 0:
                self.label.configure(bg="red", fg=font_color_01)
            else:
                self.label.configure(bg="yellow", fg=font_color_02)
            self.label.after(1000, self.update)  # Update every 1 second
        elif remaining_time <= datetime.timedelta(minutes=5):
            self.label.configure(bg="red", fg=font_color_01)
            self.label.after(60000, self.update)  # Update every 1 minute
        elif remaining_time <= datetime.timedelta(minutes=15):
            self.label.configure(bg="yellow", fg=font_color_02)
            self.label.after(60000, self.update)  # Update every 1 minute
        else:
            self.label.configure(bg="black", fg=font_color_01)
            self.label.after(1000, self.update)  # Update every 1 second

        self.label.config(text=str(remaining_time).split(".")[0])
        
    def exit_timer(self, event):
        self.root.destroy()

if __name__ == "__main__":
    target_hour = 20
    target_minute = 18
    target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, target_hour, target_minute)
    root = tk.Tk()
    app = CountdownApp(root, target_time)
    root.mainloop()
