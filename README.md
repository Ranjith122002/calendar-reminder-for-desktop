# 📅 Calendar & Reminder App — Desktop Edition

> A beautiful, full-featured calendar and reminder desktop application built with **Python & Tkinter**. Stay organized, never miss a thing!

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-lightblue?style=flat-square&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 🌐 Web Version Available!

> Don't want to install? Use the web version — works on phone, tablet & laptop!

### 👉 [https://rcdwx5zu4scbvffx4.streamlit.app](https://rcdwx5zu4scbvffx4.streamlit.app)

---

## 📸 Preview

| Dark Mode | Light Mode |
|---|---|
| Deep dark theme with blue accents | Notion-style soft blue-grey |

---

## ✨ Features

### 📅 Calendar & Reminders
- Interactive monthly calendar view
- Click any date to view/add reminders
- Color-coded reminder highlights on calendar
- **Priority levels** — 🔴 High / 🟡 Medium / 🟢 Low
- Set reminder time (HH:MM) with sound alert
- Delete reminders with one click
- Monthly stats counter

### 😊 Mood Tracker
- Log your daily mood from 7 options
- 😄 Happy · 😊 Good · 😐 Neutral · 😔 Sad · 😤 Stressed · 😴 Tired · 🤩 Excited
- Personalized motivational messages per mood
- 📓 Journal notebook — write about your day
- Journal entries automatically linked to reminders

### 🎂 Birthday Manager
- Save birthdays for friends & family
- Upcoming birthday alerts (next 30 days)
- Age calculator
- Today's birthday popup notification 🎉

### 🔍 Search & Export
- Search across all reminders instantly
- Export all reminders to **CSV** file
- Quick Notes panel for fast note-taking

### 🎨 Themes
- 🌙 **Dark Mode** — deep charcoal with blue accents (default)
- ☀️ **Light Mode** — Notion-style soft grey-blue
- One-click theme toggle

### 🔔 Notifications
- Background thread checks reminders every minute
- Desktop popup notification at exact reminder time
- 🔊 Sound beep when reminder triggers

### ⚡ Other Features
- 💬 **Quote of the day** — random motivational quote on startup
- ⏳ **Countdown widget** — shows time until next reminder
- 🌤️ **Live weather** — current weather in footer (no API key needed!)
- 🕐 **Live clock** — real-time clock in footer
- 💡 **Splash screen** — animated loading screen on startup

---

## 🛠️ Built With

| Technology | Purpose |
|---|---|
| **Python 3.x** | Core language |
| **Tkinter** | Desktop GUI framework |
| **tkcalendar** | Calendar widget |
| **plyer** | Desktop notifications |
| **requests / urllib** | Live weather fetching |
| **JSON** | Local data storage |
| **winsound** | Sound notifications |
| **threading** | Background reminder checker |

---

## 🚀 Getting Started

### Prerequisites
- Windows 10 or 11
- Python 3.8 or higher

### Step 1 — Clone the repository
```bash
git clone https://github.com/Ranjith122002/calendar-reminder-for-desktop.git
cd calendar-reminder-for-desktop
```

### Step 2 — Install dependencies
```bash
pip install tkcalendar plyer requests
```

### Step 3 — Run the app
```bash
python main.py
```

---

## 📁 Project Structure
```
calendar-reminder-for-desktop/
│
├── main.py                 # Entry point + splash screen launcher
├── app.py                  # Main application window & themes
├── calendar_view.py        # Interactive calendar widget
├── reminder_manager.py     # Reminders panel with priorities
├── mood_tracker.py         # Mood tracker + journal
├── birthday.py             # Birthday manager
├── storage.py              # JSON data storage functions
├── notifier.py             # Background sound + desktop notifications
├── quotes.py               # Daily motivational quotes
├── countdown.py            # Countdown to next reminder widget
├── weather_widget.py       # Live weather display
├── splash.py               # Animated loading splash screen
│
├── reminders.json          # Auto-created — reminders data
├── moods.json              # Auto-created — mood entries
├── birthdays.json          # Auto-created — birthdays
└── mood_notes.json         # Auto-created — journal entries
```

---

## 💾 Data Storage

All data is stored **locally** on your machine as JSON files:

| File | Contents |
|---|---|
| `reminders.json` | All reminders organized by date |
| `moods.json` | Daily mood entries |
| `birthdays.json` | Saved birthdays |
| `mood_notes.json` | Journal entries |

> 🔒 Your data never leaves your computer — 100% private & offline!

---

## 🔗 Links

| | Link |
|---|---|
| 🌐 **Web Version** | [https://rcdwx5zu4scbvffx4.streamlit.app](https://rcdwx5zu4scbvffx4.streamlit.app) |
| 💻 **Web App GitHub** | [calendar-reminder-app](https://github.com/Ranjith122002/calendar-reminder-app) |
| 🖥️ **Desktop GitHub** | [calendar-reminder-for-desktop](https://github.com/Ranjith122002/calendar-reminder-for-desktop) |

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Ranjith122002**

Made with ❤️ using Python & Tkinter

---

⭐ **If you like this project, please give it a star on GitHub!** ⭐