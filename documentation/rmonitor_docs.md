# Outline
- imports
- variables
- initialization of Tkinter window
- hw component functions
- ttk widgets
- main function
- prevent execution if imported as module
***
## Imports
```python
from tkinter import ttk
import tkinter as tk
import sv_ttk
import psutil
```

Imports all the needed libraries / modules such as:
- `tkinter` the GUI library
- `ttk` from `tkinter` the themed newer widgets
- `sv_ttk` the Sun-Valley-ttk Theme
- `psutil` is needed to obtain hw component info
***
## Variables & Window init
```python
nfont = ("CaskaydiaMono Nerd Font", 14)
root = tk.Tk()
style = ttk.Style()
root.geometry("1000x600")
root.tk.call("tk", "scaling", 1.0)
root.title("rmonitor")
```
- setting the font
- simplifying `tk.Tk()` to `root` which serves as container of widgets
- size of the window
- setting the scaling to 1 (normal)
- window title
***
## Functions and Widgets
So from here on the code looks the same, its just different positions and modules but the pattern is visible, for documentation I will take the BAT function and widget since its the most complex.
### Bat Widgets
```python
bat_label = ttk.Label(root, text="Battery: ", font=nfont)
bat_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
```
Ttk Label widget at the start of the row, left aligned.
```python
bat_pct_bar = ttk.Progressbar(root, length=200, maximum=100)
bat_pct_bar.grid(row=3, column=1, padx=10, pady=10)
```
Ttk Progressbar that displays the battery percentage as a bar.
```python
bat_pct = ttk.Label(root, text="", font=nfont)
bat_pct.grid(row=3, column=2, padx=10, pady=10, sticky="e")
```
Ttk Label that holds the percentage of the battery
```python
bat_state = ttk.Label(root, text="", font=nfont)
bat_state.grid(row=3, column=3, padx=10, pady=10)
```
Ttk Label that displays charging or 
### Bat Functions
```python
def bat_funcs():
  bat_s = psutil.sensors_battery().power_plugged 
  bat = psutil.sensors_battery().percent 
```
- returns True if the battery is charging and assigns to `bat_s`.
- returns the battery percentage into `bat`
```python
  bat_pct_bar["value"] = bat
  bat_pct.config(text=f"{bat}%")
```
- passes `bat` (defined above) into dictionary or bar
- sets the percent label to text `bat`
```python
  if bat_s:
    bat_state.config(text=f"Charging")
  else:
    bat_state.config(text=f"Discharging")
```
- if charging label says charging if not label says discharging.
```python
  root.after(500, bat_funcs)
```
- after 500ms root runs the function again.
## main function and module function
```python
def main():
  cpu_funcs()
  ram_funcs()
  disk_funcs()
  bat_funcs()
  sv_ttk.set_theme("dark")
  root.mainloop()

if __name__ == "__main__":
  main()
```
- contains all functions
- only executes main if the script is run as not a module