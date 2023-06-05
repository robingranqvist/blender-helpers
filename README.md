![Header](github__header.jpg)

# Blender helpers

Just a couple helpers for working with Python in Blender 3.5 (Python 3.10) for personal artsy projects.

## Usage

Using external Python scripts in Blender is quite quirky for some reason. The folder structure should however look something like this:

```
.
├── project
|   ├── script.py
│   └── modules
│       ├── __ init __.py
│       ├── obj.py
|       └── scene.py
└── ...
```

### Script file

Create a Python file called whatever (script.py for example).

### Modules folder

Create a modules folder (containing an init file) and throw the obj.py & scene.py into it.

### Import modules

In your script.py file, import the modules as follows

```python
from sys import path
from obj import Obj
from scene import Scene

path.append(r"C:\Path\To\Your\Python\Project\Folder")
```

### Open in Blender

Open the scripting tab, import script.py and run.

### Scene

-insert more info here-

### Obj

-insert more info here-
