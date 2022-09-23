import tkinter as tk
from tkinter import ttk


class BetterTk(tk.Tk):
    def __init__(
        self,
        title: str = "Untitled",
        geometry: tuple[int, int] = (640, 400),
        resizable: bool = True,
        default_pages: list[str] = ["Main"],
        *args, **kwargs
    ):
        super(Root, self).__init__()
        self.title(title)
        self.minsize(640, 400)

        self.pages = []

        self.tabControl = ttk.Notebook(self)

        self.mainloop()

    def addPage(self, name) -> None:
        self.pages[name] = ttk.Frame(self.tabControl)
        self.tabControl.add(self.pages[name], text=name)
        self.tabControl.pack(expand=1, fill="both")

    def removePage(self, name) -> None:
        self.tabControl.forget(self.pages[name])
        del self.pages[name]

