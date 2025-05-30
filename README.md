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
