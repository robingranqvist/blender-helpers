# Blender helpers

A couple helpers for working with Python in Blender 3.5 or any Blender version that uses Python v.3.10+.

## Usage

Using external Python file is quite quirky in Blender for some reason. It should look something like this:

.
├── project
│ ├── modules
| ├── script.py
│ │ ├── **init**.py
│ │ ├── obj.py
| │ ├── scene.py
└── ...

### Script file

Create a Python file called whatever (script.py for example).

### Modules folder

Create a modules folder (containing an **init**.py file) and throw the obj.py & scene.py into it.

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

<insert more info here>

### Obj

<insert more info here>
