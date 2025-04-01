import tkinter as tk
from tkinter import ttk
import sv_ttk
import subprocess

TOOLKITVERSION = "v.0.9"
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toolkit Lauchner "+TOOLKITVERSION)
        self.geometry("1280x720")
        self.resizable(False, False)
        
class moduleContainer(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
    
        def start_rmonitor():
            subprocess.Popen(["python", "./modules/resourcemonitor.py"])
        self.button = ttk.Button(self, text="Resource Monitor", command=start_rmonitor)
        self.button.pack()

        def start_filesorter():
            subprocess.Popen(["python", "./modules/filesorter.py"])
        self.button = ttk.Button(self, text="Filesorter", command=start_filesorter)
        self.button.pack()

        def start_calc():
            subprocess.Popen(["python", ".modules/calc.py"])
        self.button = ttk.Button(self, text="Calculator", command=start_calc)
        self.button.pack
        
        self.title = ttk.Label(self, text="Dashboard", font=("Segoe UI",40))
        self.title.pack()  
        self.button = ttk.Button(self, text="Quit", command=container.destroy)
        self.button.pack()
        self.pack()

if __name__ == "__main__":
    app = App()
    moduleContainer(app)
    sv_ttk.set_theme("dark")
    app.mainloop()