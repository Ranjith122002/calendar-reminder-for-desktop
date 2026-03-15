import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime, date

BIRTHDAY_FILE = "birthdays.json"


def load_birthdays():
    if not os.path.exists(BIRTHDAY_FILE):
        return {}
    with open(BIRTHDAY_FILE, "r") as f:
        return json.load(f)


def save_birthdays(data):
    with open(BIRTHDAY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_upcoming_birthdays(days=30):
    data = load_birthdays()
    today = datetime.today()
    upcoming = []
    for name, date_str in data.items():
        try:
            bday = datetime.strptime(date_str, "%Y-%m-%d")
            this_year = bday.replace(year=today.year)
            if this_year < today:
                this_year = this_year.replace(year=today.year + 1)
            diff = (this_year - today).days
            age = today.year - bday.year
            if diff <= days:
                upcoming.append((name, date_str, diff, age + 1))
        except:
            pass
    return sorted(upcoming, key=lambda x: x[2])


class BirthdayManager(tk.Toplevel):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.title("🎂 Birthday Manager")
        self.geometry("480x560")
        self.resizable(False, False)
        self.configure(bg=theme["bg"])
        self.theme = theme
        self._build_ui()

    def _build_ui(self):
        th = self.theme

        tk.Label(
            self,
            text="🎂 Birthday Manager",
            font=("Helvetica", 14, "bold"),
            bg=th["bg"], fg=th["fg"]
        ).pack(pady=(15, 10))

        # Upcoming section
        tk.Label(
            self,
            text="🔔 Upcoming Birthdays (next 30 days)",
            font=("Helvetica", 10, "bold"),
            bg=th["bg"], fg=th["accent"]
        ).pack(anchor="w", padx=20)

        upcoming_frame = tk.Frame(self, bg=th["stats_bg"])
        upcoming_frame.pack(fill="x", padx=20, pady=5)

        upcoming = get_upcoming_birthdays(30)
        if upcoming:
            for name, date_str, days_left, age in upcoming:
                if days_left == 0:
                    text = f"🎉 TODAY — {name} turns {age}!"
                    fg = "#1dd1a1"
                else:
                    text = f"🎂 {name} — {date_str} | In {days_left} days | Turns {age}"
                    fg = th["fg"]
                tk.Label(
                    upcoming_frame,
                    text=text,
                    font=("Helvetica", 9),
                    bg=th["stats_bg"], fg=fg,
                    anchor="w"
                ).pack(fill="x", padx=10, pady=2)
        else:
            tk.Label(
                upcoming_frame,
                text="No upcoming birthdays in next 30 days",
                font=("Helvetica", 9, "italic"),
                bg=th["stats_bg"], fg=th["subfg"]
            ).pack(padx=10, pady=5)

        tk.Frame(self, bg=th["divider"], height=1).pack(fill="x", padx=20, pady=10)

        # Add birthday
        tk.Label(
            self,
            text="➕ Add Birthday",
            font=("Helvetica", 10, "bold"),
            bg=th["bg"], fg=th["fg"]
        ).pack(anchor="w", padx=20)

        add_frame = tk.Frame(self, bg=th["bg"])
        add_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(add_frame, text="👤 Name:", font=("Helvetica", 9),
                 bg=th["bg"], fg=th["fg"]).grid(row=0, column=0, sticky="w", pady=3)
        self.name_entry = tk.Entry(
            add_frame, font=("Helvetica", 10),
            bg=th["entry_bg"], fg=th["fg"],
            insertbackground=th["fg"],
            relief="flat", bd=2, width=20
        )
        self.name_entry.grid(row=0, column=1, padx=10, pady=3, ipady=3)

        tk.Label(add_frame, text="📅 Date (YYYY-MM-DD):", font=("Helvetica", 9),
                 bg=th["bg"], fg=th["fg"]).grid(row=1, column=0, sticky="w", pady=3)
        self.date_entry = tk.Entry(
            add_frame, font=("Helvetica", 10),
            bg=th["entry_bg"], fg=th["fg"],
            insertbackground=th["fg"],
            relief="flat", bd=2, width=20
        )
        self.date_entry.grid(row=1, column=1, padx=10, pady=3, ipady=3)
        self.date_entry.insert(0, "1990-01-01")

        tk.Button(
            self,
            text="🎂 Save Birthday",
            command=self.save_birthday,
            bg=th["accent"], fg="white",
            font=("Helvetica", 10, "bold"),
            relief="flat", padx=12, pady=5,
            cursor="hand2"
        ).pack(pady=5)

        tk.Frame(self, bg=th["divider"], height=1).pack(fill="x", padx=20, pady=8)

        # All birthdays list
        tk.Label(
            self,
            text="📋 All Birthdays",
            font=("Helvetica", 10, "bold"),
            bg=th["bg"], fg=th["fg"]
        ).pack(anchor="w", padx=20)

        self.listbox = tk.Listbox(
            self,
            font=("Helvetica", 10),
            bg=th["listbox_bg"], fg=th["listbox_fg"],
            selectbackground=th["accent"],
            relief="flat",
            height=6
        )
        self.listbox.pack(fill="both", expand=True, padx=20, pady=5)
        self._refresh_list()

        tk.Button(
            self,
            text="🗑 Delete Selected",
            command=self.delete_birthday,
            bg="#ff6b6b", fg="white",
            font=("Helvetica", 9, "bold"),
            relief="flat", padx=8, pady=4,
            cursor="hand2"
        ).pack(pady=5)

    def _refresh_list(self):
        self.listbox.delete(0, "end")
        data = load_birthdays()
        for name, date_str in data.items():
            self.listbox.insert("end", f"🎂 {name} — {date_str}")

    def save_birthday(self):
        name = self.name_entry.get().strip()
        date_str = self.date_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a name!")
            return
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except:
            messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD")
            return
        data = load_birthdays()
        data[name] = date_str
        save_birthdays(data)
        self.name_entry.delete(0, "end")
        self._refresh_list()
        messagebox.showinfo("✅ Saved!", f"{name}'s birthday saved!")

    def delete_birthday(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        item = self.listbox.get(sel[0])
        name = item.replace("🎂 ", "").split(" — ")[0]
        data = load_birthdays()
        if name in data:
            del data[name]
            save_birthdays(data)
            self._refresh_list()
