import math

from tkinter import ttk

class Tab(ttk.Frame):
    def __init__(self, parent, name, *args, **kwargs):
        super(Tab, self).__init__(parent, *args, **kwargs)
        self.name = name
        self.parent = parent
        self.inputs = {}

    def create_input(
        self,
        id,
        text: str = "Button",
        default_text: str = "",
        type: str ="text",
        on_click=None,
        x: any = 0, y: any = 0, w: any = 100, h: any = 20,
        **kwargs
    ) -> ttk.Button:
        x, y, w, h = self._convert_to_pixels(x, y, w, h)
        if type == "text":
            self.inputs[id] = ttk.Entry(self, textvariable=text, width=w, **kwargs)
            self.inputs[id].grid(column=x, row=y, padx=10, pady=10)
        elif type == "button":
            self.inputs[id] = ttk.Button(self, text=text, command=on_click, **kwargs)
            self.inputs[id].grid(column=x, row=y, padx=10, pady=10)
        elif type == "check":
            self.inputs[id] = ttk.Checkbutton(self, text=text, **kwargs)
            self.inputs[id].grid(column=x, row=y, padx=10, pady=10)
        return self.inputs[id]

    def _convert_to_pixels(self, x, y, w, h):
        # Allows users to enter an int amount of pixels, or a percentage of the window size
        def toFormat(n) -> (int, int, int, int):
            if isinstance(n, float):
                return int(math.floor(n))
            elif type(n) == str and n.endswith("%"):
                return int(self.parent.winfo_width() * (int(n[:-1]) / 100))
            elif type(n) == str and n.endswith("px"):
                return int(n[:-2])
            else:
                return n
        return toFormat(x), toFormat(y), toFormat(w), toFormat(h)

