# SimpleBuilder
Simple builder is simple python library which I made for myself to provide simple building operations *(and not use .sh/.bat files)*.

# Quickstart
```py
from simple_builder import *

Builder().AddTask(Task("Python").AddArg("main.py").AddFlag("-v")).CmdSync()
```

# Documentation

