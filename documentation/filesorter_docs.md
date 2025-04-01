# Outline
- imports
- variables
- GUI function
- small function
- main function
- essential if statement
***
## Imports
```python
import tkinter as tk
from tkinter import ttk, messagebox
import sv_ttk
import os
from shutil import move
```
Importing modules that are built into python, `shutil` for moving files and `os` for getting extensions, path joining etc.
## Variables
```python
programming = [
  "py", "c", "pyc", "lua", "java", "asm", "go", "zig", 
  "js", "html", "htmx", "xml", "css", "nix", "toml", 
  "rb", "php", "swift", "rs", "pl", "sh", "sql", "dart", 
  "scala", "clj", "kt", "v", "pas", "ml", "r", "groovy"
]

text = [
  "txt", "md", "csv", "log", "json", "xml", "yaml", 
  "ini", "properties", "rtf", "doc", "docx", "odt", 
  "wps", "tex", "ppt", "pptx", "epub", "xhtml"
]

pictures = [
  "tiff", "png", "jpeg", "jpg", "gif", "bmp", "webp", 
  "svg", "heif", "raw", "ico", "jfif", "exif", "cr2", 
  "nef", "orf", "dng", "indd", "ai", "eps"
]

videos = [
  "mp4", "mov", "avi", "mkv", "wmv", "flv", "webm", 
  "mpeg", "mpg", "3gp", "m4v", "f4v", "vob", "ts", 
  "rm", "rmvb", "asf", "divx", "h264", "h265"
]

file_types = {
  "Programming": programming,
  "Text": text,
  "Pictures": pictures,
  "Videos": videos,
}
```
Pretty self explanatory, lists that contain file extensions that are later iterated through in order to sort the files into the corresponding directories.

```python
def GUI():
	root = tk.Tk()
	root.geometry("600x300")

	source = tk.StringVar()
	destination = tk.StringVar()

	source_label = ttk.Label(root, text="Absolute Source Path")
	source_label.pack()

	source_entry = ttk.Entry(root, textvariable=source)
	source_entry.pack()

	destination_label = ttk.Label(root, text="Absolute Destination Path")
	destination_label.pack()

	destination_entry = ttk.Entry(root, textvariable=destination)
	destination_entry.pack()
	
		def on_submit():
		root.quit()

	submit_button = ttk.Button(root, text="Submit", command=on_submit)
	submit_button.pack()

	sv_ttk.set_theme("dark")
	root.mainloop()

	return source.get(), destination.get()
```
- Initialization of the main window
- Initialization of Stringvars for storing userinput
- Labels and Entries
- Function that closes window on button submit press
- Actual submit button
- Theme setting
- returning path using `.get()` which is available because of StringVar

```python
def does_dir_exist(dir):
	return os.path.isdir(dir)
```
- Little function that returns true or false which is used to check if a directory exists
```python
def main():
	moved_count = 0
	hidden_count = 0

	src, dest = GUI()

	if not does_dir_exist(src):
		exit()
	else:
		os.chdir(src)

	if not does_dir_exist(dest):
		os.makedirs(dest, exist_ok=True)

	for file in os.listdir():
		ext = os.path.splitext(file)[-1][1:]

		if ext == "":
			hidden_count += 1

		for file_class, extensions in file_types.items():
			if ext in extensions:
				file_class_dir = os.path.join(dest, file_class)
				os.makedirs(file_class_dir, exist_ok=True)

				move(file, os.path.join(file_class_dir, file))
				moved_count += 1
	exit()
```
- Main function
- Two variables that count how many files were moved and how many were hidden
- Some if statements to make sure the source and destination directory exists, if source does not exist the program closes, if destination does not exist the directory gets created.
- Then the main for loop, grabs files and their extensions, if a file does not have an extension its likely to be a dotfile so they do not get moved.
- Then the code is iterating through the dictionary defined way above and grabs both the name (key) and the value (content of list) using the `.items()` method.
- Variable that is a full path and consist of destination directory and class name which is the key value of dictionary.
- using move from `shutil` the files get moved using the previously defined full path with class name

```python
if __name__ == "__main__":
	main()
```
- Essential statement to check if file is run directly or as a module.