import tkinter as tk
import urllib.request
import json


def get_weather(city="Auto"):
    """Get weather using free wttr.in API — no API key needed!"""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            current = data["current_condition"][0]
            temp = current["temp_C"]
            desc = current["weatherDesc"][0]["value"]
            humidity = current["humidity"]
            city_name = data["nearest_area"][0]["areaName"][0]["value"]

            code = int(current["weatherCode"])
            if code == 113:
                emoji = "☀️"
            elif code in [116, 119]:
                emoji = "⛅"
            elif code in [122, 143]:
                emoji = "☁️"
            elif code in [200, 386, 389]:
                emoji = "⛈️"
            elif code in [227, 230]:
                emoji = "❄️"
            else:
                emoji = "🌦️"

            return {
                "city": city_name,
                "temp": temp,
                "desc": desc,
                "humidity": humidity,
                "emoji": emoji
            }
    except Exception:
        return None


class WeatherWidget(tk.Frame):
    def __init__(self, parent, theme):
        super().__init__(parent, bg=theme["header_bg"])
        self.theme = theme

        self.weather_lbl = tk.Label(
            self,
            text="🌤️ Loading weather...",
            font=("Helvetica", 9),
            bg=theme["header_bg"],
            fg=theme["footer_fg"]
        )
        self.weather_lbl.pack(side="left", padx=5)
        self.refresh()

    def refresh(self):
        """Refresh weather every 10 minutes."""
        data = get_weather()
        if data:
            self.weather_lbl.config(
                text=f"{data['emoji']} {data['city']}: {data['temp']}°C  {data['desc']}  💧{data['humidity']}%"
            )
        else:
            self.weather_lbl.config(text="🌤️ Weather unavailable")
        self.after(600000, self.refresh)
