from tkinter import Tk, Button, HORIZONTAL, Canvas
from tkinter.colorchooser import askcolor


class Paint:
    pen_size: float = 5.0
    color: str = 'black'

    def __init__(self):
        self.root: Tk = Tk()

        self.pen_button: Button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button: Button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button: Button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button: Button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button: Button = Button(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self) -> None:
        self.old_x: int = None
        self.old_y: int = None
        self.line_width: int = self.choose_size_button.get()
        self.color: str = self.color
        self.eraser_on: bool = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion', self.print)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self) -> None:
        self.activate_button(self.pen_button)

    def use_brush(self) -> None:
        self.activate_button(self.brush_button)

    def choose_color(self) -> None:
        self.eraser_on: bool = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self) -> None:
        self.active_button(self.eraser_button, eraser_mode=True)


