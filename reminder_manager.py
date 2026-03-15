import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
from storage import get_reminders, add_reminder, delete_reminder, load_reminders


class ReminderManager(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.current_date = datetime.today().strftime("%Y-%m-%d")
        self._build_ui()
        self.load_date(self.current_date)

    def _build_ui(self):
        # Title
        self.title_label = tk.Label(
            self,
            text="📝 Reminders",
            font=("Helvetica", 13, "bold")
        )
        self.title_label.pack(pady=(0, 2))

        # Date label
        self.date_label = tk.Label(
            self,
            text="",
            font=("Helvetica", 10, "bold")
        )
        self.date_label.pack()

        # Stats
        self.stats_label = tk.Label(
            self,
            text="",
            font=("Helvetica", 9),
            padx=10, pady=4
        )
        self.stats_label.pack(fill="x", padx=10, pady=4)

        # Listbox
        self.listbox = tk.Listbox(
            self,
            font=("Helvetica", 10),
            relief="flat",
            selectmode="single",
            height=8,
            activestyle="none"
        )
        self.listbox.pack(fill="both", expand=True, padx=10, pady=5)

        # Delete button
        tk.Button(
            self,
            text="🗑 Delete Selected",
            command=self.delete_selected,
            bg="#ff6b6b", fg="white",
            font=("Helvetica", 9, "bold"),
            relief="flat", padx=8, pady=4,
            cursor="hand2"
        ).pack(pady=3)

        # Priority
        priority_frame = tk.Frame(self)
        priority_frame.pack(fill="x", padx=10, pady=4)

        tk.Label(
            priority_frame,
            text="Priority:",
            font=("Helvetica", 9, "bold")
        ).pack(side="left")

        self.priority_var = tk.StringVar(value="🟡 Medium")
        for p in ["🔴 High", "🟡 Medium", "🟢 Low"]:
            tk.Radiobutton(
                priority_frame,
                text=p,
                variable=self.priority_var,
                value=p,
                font=("Helvetica", 9)
            ).pack(side="left", padx=5)

        # Time entry
        time_frame = tk.Frame(self)
        time_frame.pack(fill="x", padx=10, pady=2)

        tk.Label(
            time_frame,
            text="⏰ Time (HH:MM):",
            font=("Helvetica", 9)
        ).pack(side="left")

        self.time_entry = tk.Entry(
            time_frame,
            font=("Helvetica", 10),
            width=8,
            relief="flat", bd=2
        )
        self.time_entry.pack(side="left", padx=5, ipady=3)

        # Note entry
        note_frame = tk.Frame(self)
        note_frame.pack(fill="x", padx=10, pady=2)

        tk.Label(
            note_frame,
            text="📌 Note:",
            font=("Helvetica", 9)
        ).pack(side="left")

        self.note_entry = tk.Entry(
            note_frame,
            font=("Helvetica", 10),
            width=25,
            relief="flat", bd=2
        )
        self.note_entry.pack(side="left", padx=5, ipady=3)

        # Add button
        tk.Button(
            self,
            text="➕ Add Reminder",
            command=self.add_reminder,
            bg="#4a9eff", fg="white",
            font=("Helvetica", 10, "bold"),
            relief="flat", padx=12, pady=5,
            cursor="hand2"
        ).pack(pady=5)

        # Quick Notes
        tk.Label(
            self,
            text="🗒️ Quick Notes:",
            font=("Helvetica", 9, "bold"),
            anchor="w"
        ).pack(fill="x", padx=10)

        self.quick_notes = scrolledtext.ScrolledText(
            self,
            font=("Helvetica", 9),
            height=5,
            relief="flat",
            wrap="word"
        )
        self.quick_notes.pack(fill="both", padx=10, pady=4)

    def load_date(self, date_str):
        self.current_date = date_str
        self.date_label.config(text=f"📅 {date_str}")
        self.listbox.delete(0, "end")

        reminders = get_reminders(date_str)
        for r in reminders:
            self.listbox.insert("end", r)

        # Stats
        all_data = load_reminders()
        total = sum(len(v) for v in all_data.values())
        today = datetime.today().strftime("%Y-%m")
        month_count = sum(len(v) for k, v in all_data.items()
                          if k.startswith(today))
        self.stats_label.config(
            text=f"📊 Total: {total}  |  This month: {month_count}  |  Today: {len(reminders)}"
        )

    def add_reminder(self):
        time_val = self.time_entry.get().strip()
        note = self.note_entry.get().strip()
        priority = self.priority_var.get()

        if not note:
            return

        if time_val:
            reminder_text = f"{time_val} | {priority} | {note}"
        else:
            reminder_text = f"{priority} | {note}"

        add_reminder(self.current_date, reminder_text)
        self.time_entry.delete(0, "end")
        self.note_entry.delete(0, "end")
        self.load_date(self.current_date)

    def delete_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        reminder_text = self.listbox.get(sel[0])
        delete_reminder(self.current_date, reminder_text)
        self.load_date(self.current_date)
