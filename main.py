import tkinter as tk
import datetime

font_color_01 = "white"
font_color_02 = "black"

class CountdownApp:
    def __init__(self, root, target_time):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.attributes("-fullscreen", True)

        self.label = tk.Label(root, font=("Helvetica", 300), bg="black", fg=font_color_01)
        self.label.pack(expand=True, fill="both")

        self.target_time = target_time
        self.update()

        self.root.bind("<Escape>", self.exit_timer)  # Bind the Esc key to the exit_timer function

    def update(self):
        current_time = datetime.datetime.now()
        remaining_time = self.target_time - current_time

        hours, remainder = divmod(int(remaining_time.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)

        if hours == 0:
            time_text = f"{minutes:02d}:{seconds:02d}"
        else:
            time_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        if remaining_time <= datetime.timedelta(minutes=2):
            if int(remaining_time.total_seconds()) % 2 == 0:
                self.label.configure(bg="red", fg=font_color_01)
            else:
                self.label.configure(bg="yellow", fg=font_color_02)
            self.label.after(1000, self.update)  # Update every 1 second
        elif remaining_time <= datetime.timedelta(minutes=5):
            self.label.configure(bg="red", fg=font_color_01)
            self.label.after(1000, self.update)  # Update every 1 minute
        elif remaining_time <= datetime.timedelta(minutes=15):
            self.label.configure(bg="yellow", fg=font_color_02)
            self.label.after(1000, self.update)  # Update every 1 minute
        else:
            self.label.configure(bg="black", fg=font_color_01)
            self.label.after(1000, self.update)  # Update every 1 second

        self.label.config(text=str(remaining_time).split(".")[0])
        
        if remaining_time.total_seconds() <= 0:
            self.label.configure(bg="red", fg=font_color_01)
            self.label.config(text="OVER")
            return
        else:
            self.label.config(text=time_text)
        
    def exit_timer(self, event):
        self.root.destroy()

if __name__ == "__main__":
    while True:
        time_input = input("Unesi vreme u formatu HHMM (0000-2359): ")
        if len(time_input) == 4 and time_input.isdigit():
            target_hour = int(time_input[:2])
            target_minute = int(time_input[2:])
            if 0 <= target_hour <= 23 and 0 <= target_minute <= 59:
                break
            else:
                print("Unesi validno vreme između 0000 i 2359.")
        else:
            print("Unesi vreme u formatu HHMM.")

    target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, target_hour, target_minute)
    root = tk.Tk()
    app = CountdownApp(root, target_time)
    root.mainloop()
