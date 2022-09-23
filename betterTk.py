import tkinter as tk
from tkinter import ttk
from BetterTk.tab import Tab


class BetterTk(tk.Tk):
    def __init__(
        self,
        title: str = "Untitled",
        geometry: tuple[int, int] = (640, 400),
        resizable: bool = True,
        default_tabs: list[str] = ["Main"],
        *args, **kwargs
    ):
        super(BetterTk, self).__init__(*args, **kwargs)
        self.winfo_toplevel().title(title)
        self.geometry(f"{int(geometry[0])}x{int(geometry[1])}")

        self.tabs = {}

        self.tabControl = ttk.Notebook(self)

        for page in default_tabs:
            self.add_tab(page)

    def add_tab(self, name) -> None:
        self.tabs[name] = Tab(self.tabControl, name)
        self.tabControl.add(self.tabs[name], text=name)
        self.tabControl.pack(expand=1, fill="both")

    def remove_tab(self, name) -> None:
        self.tabControl.forget(self.tabs[name])
        del self.tabs[name]

    def start(self):
        self.mainloop()

    def stop(self):
        self.destroy()
