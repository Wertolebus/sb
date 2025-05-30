# Simple library to build stuff
# (c) zboxjpg

from datetime import datetime

class Task():
    """Task class, that contains task itself and args
    
    cmd -> command

    com -> comment (def. None)"""
    def __init__(self, cmd, com = None):
        self.args = []
        self.cmd = cmd
        self.com = com

    def AddFlag(self, flag = ""):
        """
        Add flag to task
        
        e.g. .AddArg("-v")
        """
        self.args.append(flag)

        return self
    
    def AddArg(self, arg = "", flag = ""):
        """
        Add argument to task

        e.g. .AddArg("main.cpp") OR .AddArg("app", "-o")
        """
        if flag: self.args.extend([flag, arg])
        else: self.args.append(arg)

        return self

    def GetFullTask(self):
        """
        Return task as list

        e.g. ['g++', 'main.cpp', '-o', 'app']
        """
        full_task = [self.cmd]
        full_task.extend(self.args)
        return full_task
    
class Builder():
    "Builder class that contains tasks and used to run tasks sync & async"
    def __init__(self):
        self.tasks : list[Task] = []

    def AddTask(self, task : Task):
        """
        Add task to builder

        e.g. .AddTask(Task("g++").AddArg("main.cpp").AddArg("app", "-o"))
        """
        self.tasks.append(task)
        return self

    def CmdSync(self):
        "Run tasks synchronously"
        import subprocess as sp
        for task in self.tasks:
            ft = task.GetFullTask()
            if task.com: print(task.com)
            else: print("[SB-Sync]", datetime.now().strftime("%H.%M.%S"), "RUNNING > ", " ".join(ft))
            proc = sp.run(ft)
            if proc.stdout: print("[SB-Sync]", datetime.now().strftime("%H.%M.%S"), "STDOUT > ", proc.stdout)
            elif proc.stderr: print("[SB-Sync]", datetime.now().strftime("%H.%M.%S"), "STDERR > ", proc.stderr)
            if proc.returncode: print("\n[SB-Sync]", datetime.now().strftime("%H.%M.%S"), "EXITCODE > ", proc.returncode)
        return self

    def CmdAsync(self):
        "Run tasks asynchronously"
        import subprocess as sp
        if not len(self.tasks): return
        for task in self.tasks:
            ft = task.GetFullTask()
            if task.com: print(task.com)
            else: print("[SB-Async]", datetime.now().strftime("%H.%M.%S"), "RUNNING > ", " ".join(ft))
            proc = sp.Popen(ft)
            if proc.stdout: print("[SB-Async]", datetime.now().strftime("%H.%M.%S"), "STDOUT >", proc.stdout)
            elif proc.stderr: print("[SB-Async]", datetime.now().strftime("%H.%M.%S"), "STDERR >", proc.stderr)
            if proc.returncode: print("\n[SB-Async]", datetime.now().strftime("%H.%M.%S"), "EXITCODE >", proc.returncode)
        return self
        