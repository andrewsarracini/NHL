import sys

if sys.platform == "win32":

    from . import win32

    class WinColor:
        BLACK: int = ...
        BLUE: int = ...
        GREEN: int = ...
        CYAN: int = ...
        RED: int = ...
        MAGENTA: int = ...
        YELLOW: int = ...
        GREY: int = ...

    class WinStyle:
        NORMAL: int = ...
        BRIGHT: int = ...
        BRIGHT_BACKGROUND: int = ...

    class WinTerm:
        def __init__(self) -> None: ...
        def get_attrs(self) -> int: ...
        def set_attrs(self, value: int) -> None: ...
        def reset_all(self, on_stderr: bool | None = ...) -> None: ...
        def fore(self, fore: int | None = ..., light: bool = ..., on_stderr: bool = ...) -> None: ...
        def back(self, back: int | None = ..., light: bool = ..., on_stderr: bool = ...) -> None: ...
        def style(self, style: int | None = ..., on_stderr: bool = ...) -> None: ...
        def set_console(self, attrs: int | None = ..., on_stderr: bool = ...) -> None: ...
        def get_position(self, handle: int) -> win32.COORD: ...
        def set_cursor_position(self, position: win32.COORD | None = ..., on_stderr: bool = ...) -> None: ...
        def cursor_adjust(self, x: int, y: int, on_stderr: bool = ...) -> None: ...
        def erase_screen(self, mode: int = ..., on_stderr: bool = ...) -> None: ...
        def erase_line(self, mode: int = ..., on_stderr: bool = ...) -> None: ...
        def set_title(self, title: str) -> None: ...

def enable_vt_processing(fd: int) -> bool: ...
