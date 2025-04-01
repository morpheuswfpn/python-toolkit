from tkinter import ttk
import tkinter as tk
import sv_ttk
import psutil

def megamain():
  nfont = ("CaskaydiaMono Nerd Font", 14)

  root = tk.Tk()
  style = ttk.Style()
  root.geometry("1000x600")
  root.tk.call("tk", "scaling", 1.0)
  root.title("rmonitor")

  #       ██████╗██████╗ ██╗   ██╗
  #      ██╔════╝██╔══██╗██║   ██║
  #      ██║     ██████╔╝██║   ██║
  #      ██║     ██╔═══╝ ██║   ██║
  #      ╚██████╗██║     ╚██████╔╝
  #       ╚═════╝╚═╝      ╚═════╝ 

  def cpu_funcs():  # function for CPU-related monitoring
    load = psutil.cpu_percent()  # gets CPU load

    cpu_load_progress["value"] = load  # passes load into progress bar as the value
    cpu_load_actual.config(text=f"{load}%")  # label with load

    root.after(500, cpu_funcs)  # exec func every half a sec

  cpu_label = ttk.Label(root, text="CPU Load:", font=nfont)
  cpu_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

  cpu_load_progress = ttk.Progressbar(root, length=200, maximum=100)
  cpu_load_progress.grid(row=0, column=1, padx=10, pady=10)

  cpu_load_actual = ttk.Label(root, text="", font=nfont)
  cpu_load_actual.grid(row=0, column=2, padx=10, pady=10, sticky="e")

  #      ██████╗  █████╗ ███╗   ███╗
  #      ██╔══██╗██╔══██╗████╗ ████║
  #      ██████╔╝███████║██╔████╔██║
  #      ██╔══██╗██╔══██║██║╚██╔╝██║
  #      ██║  ██║██║  ██║██║ ╚═╝ ██║
  #      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

  def ram_funcs():
    ram = psutil.virtual_memory().percent
    ram_usage["value"] = ram # pass ram percent into bar
    ram_actual.config(text=f"{ram}%")  # label with RAM usage
    root.after(500, ram_funcs)

  ram_label = ttk.Label(root, text="RAM Usage:", font=nfont)
  ram_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")  

  ram_usage = ttk.Progressbar(root, length=200, maximum=100)
  ram_usage.grid(row=1, column=1, padx=10, pady=10)

  ram_actual = ttk.Label(root, text="", font=nfont)
  ram_actual.grid(row=1, column=2, padx=10, pady=10, sticky="e")

  #      ██████╗ ██╗███████╗██╗  ██╗
  #      ██╔══██╗██║██╔════╝██║ ██╔╝
  #      ██║  ██║██║███████╗█████╔╝ 
  #      ██║  ██║██║╚════██║██╔═██╗ 
  #      ██████╔╝██║███████║██║  ██╗

  def disk_funcs(): # disk related functions
    disk_pct_used = psutil.disk_usage("/").percent

    disk_pct_bar["value"] = disk_pct_used
    disk_pct.config(text=f"{disk_pct_used}%")

    root.after(500, disk_funcs)

  disk_label = ttk.Label(root, text="Disk Usage percent: ", font=nfont)
  disk_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

  disk_pct_bar = ttk.Progressbar(root, length=200, maximum=100)
  disk_pct_bar.grid(row=2, column=1, padx=10, pady=10)

  disk_pct = ttk.Label(root, text="", font=nfont)
  disk_pct.grid(row=2, column=2, padx=10, pady=10, sticky="e")

  #      ██████╗  █████╗ ████████╗
  #      ██╔══██╗██╔══██╗╚══██╔══╝
  #      ██████╔╝███████║   ██║   
  #      ██╔══██╗██╔══██║   ██║   
  #      ██████╔╝██║  ██║   ██║   
  #      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   

  def bat_funcs():
    bat_s = psutil.sensors_battery().power_plugged # charging returns BOOL
    bat = psutil.sensors_battery().percent # percent

    bat_pct_bar["value"] = bat
    bat_pct.config(text=f"{bat}%")

    if bat_s:
      bat_state.config(text=f"Charging")
    else:
      bat_state.config(text=f"Discharging")

    root.after(500, bat_funcs)

  bat_label = ttk.Label(root, text="Battery: ", font=nfont)
  bat_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

  bat_pct_bar = ttk.Progressbar(root, length=200, maximum=100)
  bat_pct_bar.grid(row=3, column=1, padx=10, pady=10)

  bat_pct = ttk.Label(root, text="", font=nfont)
  bat_pct.grid(row=3, column=2, padx=10, pady=10, sticky="e")

  bat_state = ttk.Label(root, text="", font=nfont)
  bat_state.grid(row=3, column=3, padx=10, pady=10)

  cpu_funcs()
  ram_funcs()
  disk_funcs()
  bat_funcs()
  sv_ttk.set_theme("dark")
  root.mainloop()

if __name__ == "__main__":
  megamain()