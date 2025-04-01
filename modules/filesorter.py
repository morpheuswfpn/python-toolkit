import tkinter as tk
from tkinter import ttk 
import sv_ttk
import os
from shutil import move

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

def does_dir_exist(dir):
	return os.path.isdir(dir)

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

if __name__ == "__main__":
	main()

