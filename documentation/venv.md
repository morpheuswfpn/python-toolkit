# Venv
venv is a builtin python module that helps isolate dependencies for python projects so that for example when using `pip install` inside of a virtual environment this will only be available there but not on your whole system.
# Get Started
What I am referring to as dir is in fact usually called `venv` or `.venv`.
## Create
`python -m venv <dir>`
This will create the `<dir>` dir inside your current one.
## Activate
### Linux * & Mac
`chmod +x <dir>/bin/activate`
`source <dir>/bin/activate`
### Windows
`<dir>/bin/activate`
## deactivate
`deactivate`
# IDE
At the bottom right in most IDE's you need to change the python interpreter to something that says *venv*. Else the by `pip` installed packages will not be available.