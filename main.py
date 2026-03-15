import tkinter as tk
from splash import SplashScreen

def main():
    splash = SplashScreen()
    splash.mainloop()
    from app import App
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
