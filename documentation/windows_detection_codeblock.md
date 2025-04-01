```python
	if platform.system() == "Windows":
		import pywinstyles
		root.iconbitmap("./Assets/file.ico")
		pywinstyles.change_header_color(root, "#1c1c1c")
```

This codeblock is used in every single module and main, what It does it it themes the toolbar in and sets an Icon.