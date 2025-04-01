import tkinter as tk
from tkinter import ttk
import sv_ttk
import subprocess
from tkinter.font import nametofont


TOOLKITVERSION = "v.0.11"
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toolkit Lauchner "+TOOLKITVERSION)
        self.geometry("1120x630") # 16:9@70
        self.resizable(False, False)
        self.iconbitmap("./Assets/repair-toolkit.ico")
        
class moduleContainer(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.columnconfigure(2, weight=1)
        container.columnconfigure(3, weight=1)
        container.columnconfigure(4, weight=1)
        
        def start_rmonitor():
            subprocess.Popen(["python", "./modules/resourcemonitor.py"])
        
        def start_filesorter():
            subprocess.Popen(["python", "./modules/filesorter.py"])
        
        def start_calc():
            subprocess.Popen(["python", "./modules/calc.py"])
        
        self.title = ttk.Label(self, text="Dashboard", font=("Segoe UI", 40))
        self.title.grid(row=0, column=1, columnspan=3, pady=10, sticky="n")
        
        self.button_rmonitor = ttk.Button(self, text="Resource Monitor", command=start_rmonitor)
        self.button_rmonitor.grid(row=1, column=1, pady=10, padx=20, sticky="ew")
        
        self.button_filesorter = ttk.Button(self, text="Filesorter", command=start_filesorter)
        self.button_filesorter.grid(row=1, column=2, pady=10, padx=20, sticky="ew")
        
        self.button_calc = ttk.Button(self, text="Calculator", command=start_calc)
        self.button_calc.grid(row=1, column=3, pady=10, padx=20, sticky="ew")
        
        self.buttonplaceholder = ttk.Button(self, text="WIP....")
        self.buttonplaceholder.grid(row=2, column=2, pady=10, padx=20, sticky="ew")
        
        self.button_quit = ttk.Button(self, text="Quit", command=container.destroy)
        self.button_quit.grid(row=5, column=3, pady=10, padx=20, sticky="se")
        
        self.grid(padx=40, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = App()
    moduleContainer(app)
    sv_ttk.set_theme("dark")
    nametofont("SunValleyBodyFont").configure(size=15)
    app.mainloop()
