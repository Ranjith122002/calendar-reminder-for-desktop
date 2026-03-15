import tkinter as tk
from datetime import datetime
from storage import load_reminders


class CountdownWidget(tk.Frame):
    def __init__(self, parent, theme):
        super().__init__(parent, bg=theme["header_bg"])
        self.theme = theme

        self.title_lbl = tk.Label(
            self,
            text="⏳ Next:",
            font=("Helvetica", 8),
            bg=theme["header_bg"],
            fg=theme["footer_fg"]
        )
        self.title_lbl.pack(side="left")

        self.countdown_lbl = tk.Label(
            self,
            text="—",
            font=("Helvetica", 8, "bold"),
            bg=theme["header_bg"],
            fg=theme["accent"]
        )
        self.countdown_lbl.pack(side="left", padx=3)

        self._update()

    def _update(self):
        next_reminder = self._get_next_reminder()
        if next_reminder:
            self.countdown_lbl.config(text=next_reminder)
        else:
            self.countdown_lbl.config(text="No upcoming")
        self.after(60000, self._update)

    def _get_next_reminder(self):
        data = load_reminders()
        now = datetime.now()
        today = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M")

        upcoming = []
        for date_str, reminders in sorted(data.items()):
            if date_str >= today:
                for r in reminders:
                    parts = r.split("|")
                    if len(parts) >= 3 and parts[0].strip():
                        time_part = parts[0].strip()
                        if date_str > today or time_part > current_time:
                            upcoming.append((date_str, time_part, r))

        if upcoming:
            upcoming.sort()
            date_str, time_part, reminder = upcoming[0]
            if date_str == today:
                return f"Today {time_part}"
            else:
                return f"{date_str} {time_part}"
        return None
