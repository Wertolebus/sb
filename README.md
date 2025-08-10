# SimpleBuilder
Simple builder is simple python library which I made for myself to provide simple building operations *(and not use .sh/.bat files)*.

# Quickstart
```py
from simple_builder import *

Builder().AddTask(Task("python").AddArg("main.py").AddFlag("-v")).CmdSync()
```

# Documentation

## class `Task(cmd)`
- param `cmd` - command to run (e.g. "python", "gcc", etc.)
- param `com` - print comment instead of standard log

func `AddFlag(flag)` - add flag to task (e.g. `.AddFlag("-v")`). This is a fluent method that returns the instance itself for chaining.

func `AddArg(arg, flag)` - add arg to task (e.g. `.AddArg("main.c")`, `.AddArg`). This is a fluent method that returns the instance itself for chaining.


func `GetFullTask()` - return task as list (e.g. `.GetFullTask()` will return `['gcc', 'main.c', '-o', './app']`)


## class `Builder()`
func `AddTask(task)` - add task to builder. This is a fluent method that returns the instance itself for chaining.


func `CmdSync()` - run tasks synchronously. This is a fluent method that returns the instance itself for chaining.


func `CmdAsync()` - run tasks asynchronously. This is a fluent method that returns the instance itself for chaining.
# Quickstart
```py
from simple_builder import *

platform = GetPlatform()
cmd = ""

# defining command for specific OS
if platform == Platform.WIN32:
    cmd = "python"
else:
    cmd = "python3"

b = Builder()
t = Task(cmd)
t.AddFlag("-v")
t.AddArg("main.py")
b.AddTask(t)
b.CmdSync()
```
## Functions
func `GetPlatform()` - get system platform

| System                         | Value             |
|--------------------------------|-------------------|
| Linux                          | Platform.LINUX    |
| Windows                        | Platform.WIN32    |
| Windows/Cygwin                 | Platform.CYGWIN   |
| Windows/MSYS2<br>Windows/MinGW | Platform.MSYS     |
| Mac OS X                       | Platform.MACOSX   |
| OS/2                           | Platform.OS2      |
| OS/2 EMX                       | Platform.OS2EMX   |
| RiscOS                         | Platform.RISCOS   |
| AtheOS                         | Platform.ATHEOS   |
| FreeBSD 6                      | Platform.FREEBSD6 |
| FreeBSD 7                      | Platform.FREEBSD7 |
| FreeBSD 8                      | Platform.FREEBSD8 |
| FreeBSD N                      | Platform.FREEBSDN |

