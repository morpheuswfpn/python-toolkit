from tkinter import ttk
import tkinter as tk
import sv_ttk
import random
import platform
from tkinter.font import nametofont

root = tk.Tk()
root.geometry("980x280")
root.tk.call("tk", "scaling", 1.0)
root.title("Password Generator")
root.resizable(False,False)

if platform.system() == "Windows":
    import pywinstyles
    root.iconbitmap("./Assets/password.ico")
    pywinstyles.change_header_color(root,"#1c1c1c")

sv_ttk.set_theme("dark")
nametofont("SunValleyBodyFont").configure(size=30)
    
uselettersbool = tk.BooleanVar(value=False)
usenumbersbool = tk.BooleanVar(value=False)
usespecialcharbool = tk.BooleanVar(value=False)
usecapsbool = tk.BooleanVar(value=False)
passwordlength = tk.IntVar(value=8)
alphabet = list("abcdefghijklmnopqrstuvwxyz")
special_chars = list("!@#$%^&*()-_=+[]{};:'\",<>./?")
pwstrengths = ["Weak", "Medium", "Strong", "Very Strong", "Custom"]
stronk = tk.IntVar(value=len(pwstrengths)-1)
generated_password = ""
def rl():
    return random.choice(alphabet)

def rn09():
    return random.randint(0,9)

def rsc():
    return random.choice(special_chars)

def get_current_value():
    return '{: .0f}'.format(passwordlength.get())

def sliderchanged(event):
    passwordlengthlabel.configure(text=get_current_value())
    
def get_current_value2():
    return int(stronk.get())

    
def updatestrengthlabel(event):
    selected_strength = pwstrengths[get_current_value2()]
    pwstrengthlabel.config(text=f"{selected_strength}")
    
    if selected_strength == "Weak":
        if not (uselettersbool.get() == True and usenumbersbool.get() == False and usespecialcharbool.get() == False and usecapsbool.get() == False):
            selected_strength = "Custom"  
        uselettersbool.set(True)
        usenumbersbool.set(False)
        usespecialcharbool.set(False)
        usecapsbool.set(False)
        
    elif selected_strength == "Medium":
        if not (uselettersbool.get() == True and usenumbersbool.get() == True and usespecialcharbool.get() == False and usecapsbool.get() == False):
            selected_strength = "Custom"  
        uselettersbool.set(True)
        usenumbersbool.set(True)
        usespecialcharbool.set(False)
        usecapsbool.set(False)
        
    elif selected_strength == "Strong":
        if not (uselettersbool.get() == True and usenumbersbool.get() == True and usespecialcharbool.get() == False and usecapsbool.get() == True):
            selected_strength = "Custom"  
        uselettersbool.set(True)
        usenumbersbool.set(True)
        usespecialcharbool.set(False)
        usecapsbool.set(True)
        
    elif selected_strength == "Very Strong":
        if not (uselettersbool.get() == True and usenumbersbool.get() == True and usespecialcharbool.get() == True and usecapsbool.get() == True):
            selected_strength = "Custom"  
        uselettersbool.set(True)
        usenumbersbool.set(True)
        usespecialcharbool.set(True)
        usecapsbool.set(True)
    
    pwstrengthlabel.config(text=f"{selected_strength}")       
                        
generated_passwordlabel = ttk.Label(root,text="")
def generate():
    char_pool = []
    
    if uselettersbool.get():
        char_pool.extend(alphabet)
        
    if usecapsbool.get():
        char_pool.extend([char.upper() for char in alphabet])
        
    if usenumbersbool.get():
        char_pool.extend("0123456789")
        
    if usespecialcharbool.get():
        char_pool.extend(special_chars)
    
    if not char_pool:
        generated_passwordlabel.configure(text="Error: Select at least one option!")
        return

    length = passwordlength.get()
    password = "".join(random.choice(char_pool) for x in range(length))
    
    generated_passwordlabel.configure(text=password)
    
    
# config
useletterscheck = ttk.Checkbutton(root, text="Use Letters", variable=uselettersbool)
usenumberscheck = ttk.Checkbutton(root, text="Use Numbers", variable=usenumbersbool)
usespecialcharcheck = ttk.Checkbutton(root, text="Use Special Characters", variable=usespecialcharbool)
usecapscheck = ttk.Checkbutton(root, text="Use Capital Letters", variable=usecapsbool)

passwordlengthsliderlabel = ttk.Label(root, text="Length: ")
passwordlengthslider = ttk.Scale(root,from_=8,to=50, orient='horizontal', variable=passwordlength, command=sliderchanged, length=200)
passwordlengthlabel = ttk.Label(root, text=get_current_value())

pwstrengthsliderlabel = ttk.Label(root, text="Strength Preset: ")
pwstrengthslider = ttk.Scale(root, from_=0, to=len(pwstrengths)-1, variable=stronk, orient="horizontal", command=updatestrengthlabel, length=200)
pwstrengthlabel = ttk.Label(root, text="Custom")

submit = ttk.Button(root, text="Generate", command=lambda: generate())


useletterscheck.grid(row=0, column=0, ipadx=0, padx=10, ipady=0, pady=0, sticky="w")
usenumberscheck.grid(row=1, column=0, ipadx=0, padx=10, ipady=0, pady=0, sticky="w")
usecapscheck.grid(row=2, column=0, ipadx=0, padx=10, ipady=0, pady=0, sticky="w")
usespecialcharcheck.grid(row=3, column=0, ipadx=0, padx=10, ipady=0, pady=0, sticky="w")

passwordlengthsliderlabel.grid(row=0, column=1, ipadx=0, padx=10, ipady=0, pady=0, sticky="w")
passwordlengthslider.grid(row=0, column=2, ipadx=0, padx=0, ipady=0, pady=0, sticky="w")
passwordlengthlabel.grid(row=0, column=3, ipadx=0, padx=20, ipady=0, pady=0, sticky="w")

pwstrengthsliderlabel.grid(row=1, column=1, ipadx=0, padx=10, ipady=0, pady=0, sticky="w")
pwstrengthslider.grid(row=1, column=2, ipadx=0, padx=0, ipady=0, pady=0, sticky="w")
pwstrengthlabel.grid(row=1, column=3, ipadx=0, padx=20, ipady=0, pady=0, sticky="w")

submit.grid(row=3, column=2)

generated_passwordlabel.grid(row=4, column=0, columnspan=4, padx=10,ipadx=0, pady=20,ipady=0, sticky="w")

def main():
    root.mainloop()

if __name__ == "__main__":
  main()