from tkinter import ttk
import tkinter as tk
import sv_ttk
import random
import platform

root = tk.Tk()
style = ttk.Style()
root.geometry("900x480")
root.tk.call("tk", "scaling", 1.0)
root.title("Password Generator")
root.resizable(False,False)
sv_ttk.set_theme("dark")

if platform.system() == "Windows":
    import pywinstyles
    root.iconbitmap("./Assets/password.ico")
    pywinstyles.change_header_color(root,"#1c1c1c")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 'z'
]
def rl():
    return random.choice(alphabet)

def rn09():
    return random.randint(0,9)

special_chars = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
    "'", '"', ',', '<', '.', '>', '/', '?'
]
def rsc():
    return random.choice(special_chars)

def main():
    sv_ttk.set_theme("dark")
    root.mainloop()

if __name__ == "__main__":
  main()