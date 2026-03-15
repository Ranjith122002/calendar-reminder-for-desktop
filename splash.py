import tkinter as tk
from datetime import datetime


class SplashScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("400x280")
        self.resizable(False, False)
        self.configure(bg="#1e1e1e")
        self.overrideredirect(True)

        # Center on screen
        self.update_idletasks()
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        x = (w // 2) - 200
        y = (h // 2) - 140
        self.geometry(f"400x280+{x}+{y}")

        tk.Label(
            self,
            text="📅",
            font=("Helvetica", 48),
            bg="#1e1e1e", fg="white"
        ).pack(pady=(30, 5))

        tk.Label(
            self,
            text="Calendar & Reminder App",
            font=("Helvetica", 16, "bold"),
            bg="#1e1e1e", fg="white"
        ).pack()

        tk.Label(
            self,
            text="Stay organized, never miss a thing!",
            font=("Helvetica", 9, "italic"),
            bg="#1e1e1e", fg="#888888"
        ).pack(pady=5)

        self.progress_lbl = tk.Label(
            self,
            text="Loading...",
            font=("Helvetica", 9),
            bg="#1e1e1e", fg="#4a9eff"
        )
        self.progress_lbl.pack(pady=20)

        tk.Label(
            self,
            text=f"v1.0  |  {datetime.now().strftime('%Y')}",
            font=("Helvetica", 8),
            bg="#1e1e1e", fg="#444444"
        ).pack(side="bottom", pady=10)

        self.steps = [
            "Loading calendar...",
            "Setting up reminders...",
            "Loading mood tracker...",
            "Checking birthdays...",
            "Starting app..."
        ]
        self.step_index = 0
        self._animate()

    def _animate(self):
        if self.step_index < len(self.steps):
            self.progress_lbl.config(text=self.steps[self.step_index])
            self.step_index += 1
            self.after(400, self._animate)
        else:
            self.after(300, self.destroy)
