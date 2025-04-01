import tkinter as tk
from tkinter import ttk
import sv_ttk
import subprocess
import platform
from tkinter.font import nametofont

TOOLKITVERSION = "v.0.13"
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Toolkit Lauchner "+TOOLKITVERSION)
        self.geometry("960x540") # 16:9@60
        self.resizable(False, False)

        if platform.system() == "Windows":
            import pywinstyles
            self.iconbitmap("./Assets/repair-toolkit.ico")
            pywinstyles.change_header_color(self,"#1c1c1c")
        

class moduleContainer(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        def start_rmonitor():
            subprocess.Popen(["python", "./modules/resourcemonitor.py"])
        
        def start_filesorter():
            subprocess.Popen(["python", "./modules/filesorter.py"])
        
        def start_calc():
            subprocess.Popen(["python", "./modules/calc.py"])
        
        def start_pgen():
            subprocess.Popen(["python", "./modules/pgen.py"])
        
        # Title label, centered at the top
        self.title = ttk.Label(self, text="Dashboard", font=("Segoe UI", 40))
        self.title.pack(side="top", pady=10, anchor="n")

        # Frame to hold the buttons and distribute them horizontally
        button_frame = ttk.Frame(self)
        button_frame.pack(side="top", pady=20)

        # Left button that expands
        self.button_rmonitor = ttk.Button(button_frame, text="Resource Monitor", command=start_rmonitor)
        self.button_rmonitor.pack(side="left", expand=True, padx=10)
        
        # Middle button that stays fixed in the center
        self.button_filesorter = ttk.Button(button_frame, text="Filesorter", command=start_filesorter)
        self.button_filesorter.pack(side="left",expand=True, padx=10)
        
        # Right button that expands
        self.button_calc = ttk.Button(button_frame, text="Calculator", command=start_calc)
        self.button_calc.pack(side="left", expand=True, padx=10)

        self.button_pgen = ttk.Button(button_frame, text="Password Gen", command=start_pgen)
        self.button_pgen.pack(side="left", expand=True, padx = 10)
        
        # Make the entire frame expand to fill available space
        self.pack(fill="both", expand=True)

        # Center the middle button with "place" geometry manager
        button_frame.place(relx=0.45, rely=0.3, anchor="n")
        
if __name__ == "__main__":
    app = App()
    moduleContainer(app)
    sv_ttk.set_theme("dark")
    nametofont("SunValleyBodyFont").configure(size=15)
    app.mainloop()
