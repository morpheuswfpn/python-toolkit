# Outline
- Imports
- Variables and Creation of Objects
- actual calculating function
- clear function
- equals function
- All buttons
- Positioning of all buttons
- main function...
***
## Imports
```python
from tkinter import ttk
import tkinter as tk
import sv_ttk
import platform
from tkinter.font import nametofont
```
- Tkinter essentials
- Theme
- Windows detection
***
## Variables and Creation of Objects
```python
root = tk.Tk()
style = ttk.Style()
root.geometry("457x640")
root.tk.call("tk", "scaling", 1.0)
root.title("Calculator")
root.resizable(False,False)
sv_ttk.set_theme("dark")
```
- Window setup
- Style setup for later modifying font size
- theme setup
## Modifying Font Size
```python
nametofont("SunValleyBodyFont").configure(size=20)
```
- This is done to make the numbers on the calculator more readable
***
## Functions
```python
n = ""
def na(x):
    global n
    if x == "=":
        try:
            n = str(eval(n))  
        except:
            n = "Error"
    else:
        n += str(x)  
    title.config(text=n)
```
- This is the main calculating function
- n is a variable used for the output in calculator
- If user types `=` the things that are already inputted will be calculated
- If user types something else it will get displayed in the GUI
- text of main visual output field equals n

 ```python   
def claer():
    global n
    n = ""   
    title.config(text=n)   
```
- if the clear button is pressed it sets the text inside of n to an empty string

 ```python         
def eqauls():
    global n
    try:
        n = str(eval(n))
    except:
        n = "Error"
    title.config(text=n)
```
- the function that is called upon hitting the equal sign, tries to calculate but if it fails it will just print error to the user.
***
## Actual GUI
```python
title = ttk.Label(root, text=n, font=("JetBrains Nerd Font Mono", 25))
button0 = ttk.Button(root, text="0", command=lambda: na(0))
button1 = ttk.Button(root, text="1", command=lambda: na(1))
button2 = ttk.Button(root, text="2", command=lambda: na(2))
button3 = ttk.Button(root, text="3", command=lambda: na(3))
button4 = ttk.Button(root, text="4", command=lambda: na(4))
button5 = ttk.Button(root, text="5", command=lambda: na(5))
button6 = ttk.Button(root, text="6", command=lambda: na(6))
button7 = ttk.Button(root, text="7", command=lambda: na(7))
button8 = ttk.Button(root, text="8", command=lambda: na(8))
button9 = ttk.Button(root, text="9", command=lambda: na(9))
buttonm = ttk.Button(root, text="*", command=lambda: na("*"))
buttond = ttk.Button(root, text="/", command=lambda: na("/"))
buttonn = ttk.Button(root, text="-", command=lambda: na("-"))
buttonp = ttk.Button(root, text="+", command=lambda: na("+"))
buttone = ttk.Button(root, text="=", command=lambda:eqauls())
buttonc = ttk.Button(root, text="C", command=lambda:claer())
# Title

title.grid(row=0, column=0, columnspan=4, ipady=45)

# Row 1
button7.grid(row=1, column=0, ipadx=38,padx=1, ipady=45, pady=1)
button8.grid(row=1, column=1, ipadx=38,padx=1, ipady=45, pady=1)
button9.grid(row=1, column=2, ipadx=38,padx=1, ipady=45, pady=1)
buttond.grid(row=1, column=3, ipadx=38,padx=0, ipady=45, pady=1)
# Row 2
button4.grid(row=2, column=0, ipadx=38,padx=1, ipady=45, pady=1)
button5.grid(row=2, column=1, ipadx=38,padx=1, ipady=45, pady=1)
button6.grid(row=2, column=2, ipadx=38,padx=1, ipady=45, pady=1)
buttonm.grid(row=2, column=3, ipadx=38,padx=0, ipady=45, pady=1)
# Row 3
button1.grid(row=3, column=0, ipadx=38,padx=1, ipady=45, pady=1)
button2.grid(row=3, column=1, ipadx=38,padx=1, ipady=45, pady=1)
button3.grid(row=3, column=2, ipadx=38,padx=1, ipady=45, pady=1)
buttonn.grid(row=3, column=3, ipadx=38,padx=0, ipady=45, pady=1)
# Row 4
button0.grid(row=4, column=0, ipadx=38,padx=1, ipady=45) 
buttonc.grid(row=4, column=1, ipadx=38,padx=1, ipady=45)
buttone.grid(row=4, column=2, ipadx=38,padx=1, ipady=45)
buttonp.grid(row=4, column=3, ipadx=38,padx=1, ipady=45) 
```
There is not that much to say about this, its just GUI positioned with grid
