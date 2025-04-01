import tkinter as tk
from tkinter import ttk
import sv_ttk
import subprocess
from tkinter.font import nametofont

TOOLKITVERSION = "v.0.12"
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toolkit Lauchner "+TOOLKITVERSION)
        self.geometry("960x540") # 16:9@60
        self.resizable(False, False)
        

class moduleContainer(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        def start_rmonitor():
            subprocess.Popen(["python", "./modules/resourcemonitor.py"])
        
        def start_filesorter():
            subprocess.Popen(["python", "./modules/filesorter.py"])
        
        def start_calc():
            subprocess.Popen(["python", "./modules/calc.py"])
        
        # Title label, centered at the top
        self.title = ttk.Label(self, text="Dashboard", font=("Segoe UI", 40))
        self.title.pack(side="top", pady=10, anchor="n")

        # Frame to hold the buttons and distribute them horizontally
        button_frame = ttk.Frame(self)
        button_frame.pack(side="top", fill="x", pady=20)

        # Left button that expands
        self.button_rmonitor = ttk.Button(button_frame, text="Resource Monitor", command=start_rmonitor)
        self.button_rmonitor.pack(side="left", expand=True, padx=20)
        
        # Middle button that stays fixed in the center
        self.button_filesorter = ttk.Button(button_frame, text="Filesorter", command=start_filesorter)
        self.button_filesorter.pack(side="left", padx=20)
        
        # Right button that expands
        self.button_calc = ttk.Button(button_frame, text="Calculator", command=start_calc)
        self.button_calc.pack(side="left", expand=True, padx=20)

        # Make the entire frame expand to fill available space
        self.pack(fill="both", expand=True)

        # Center the middle button with "place" geometry manager
        button_frame.place(relx=0.5, rely=0.5, anchor="center")
if __name__ == "__main__":
    app = App()
    moduleContainer(app)
    sv_ttk.set_theme("dark")
    nametofont("SunValleyBodyFont").configure(size=15)
    app.mainloop()
