from typing import Any

class TaskQueue:
    def push(self, *args, **kwargs) -> Any: ...
    def peek(self, *args, **kwargs) -> Any: ...
    def remove(self, *args, **kwargs) -> Any: ...
    def pop(self, *args, **kwargs) -> Any: ...
    def __init__(self, *argv, **kwargs) -> None: ...

class Task:
    def __init__(self, *argv, **kwargs) -> None: ...
