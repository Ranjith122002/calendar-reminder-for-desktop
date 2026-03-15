import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from storage import get_all_dates_with_reminders


class CalendarView(tk.Frame):
    def __init__(self, parent, on_date_select=None):
        super().__init__(parent)
        self.on_date_select = on_date_select

        self.title_lbl = tk.Label(
            self,
            text="📅 Calendar",
            font=("Helvetica", 13, "bold")
        )
        self.title_lbl.pack(pady=(0, 5))

        today = datetime.today()
        self.cal = Calendar(
            self,
            selectmode="day",
            year=today.year,
            month=today.month,
            day=today.day,
            font=("Helvetica", 10),
            showweeknumbers=False,
            firstweekday="monday"
        )
        self.cal.pack(padx=10, pady=5)
        self.cal.bind("<<CalendarSelected>>", self._on_select)

        self.today_btn = tk.Button(
            self,
            text="📅 Today",
            command=self._go_today,
            font=("Helvetica", 9, "bold"),
            relief="flat", padx=10, pady=4,
            cursor="hand2"
        )
        self.today_btn.pack(pady=5)

        self.refresh_highlights()

    def _on_select(self, event=None):
        date_str = self.cal.get_date()
        # Convert mm/dd/yy to yyyy-mm-dd
        parts = date_str.split("/")
        if len(parts) == 3:
            month, day, year = parts
            year = "20" + year if len(year) == 2 else year
            date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        if self.on_date_select:
            self.on_date_select(date_str)

    def _go_today(self):
        today = datetime.today()
        self.cal.selection_set(today)
        if self.on_date_select:
            self.on_date_select(today.strftime("%Y-%m-%d"))

    def refresh_highlights(self):
        self.cal.calevent_remove("all")
        dates = get_all_dates_with_reminders()
        for d in dates:
            try:
                dt = datetime.strptime(d, "%Y-%m-%d")
                self.cal.calevent_create(dt, "reminder", "reminder")
            except:
                pass
        self.cal.tag_config("reminder", background="#4a9eff", foreground="white")
