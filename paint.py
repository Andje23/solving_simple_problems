from tkinter import Tk, Button


class Paint:
    pen_size: float = 5.0
    color: str = 'black'

    def __init__(self):
        self.root: Tk = Tk()

        self.pen_button: Button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button: Button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button: Button = Button(self.root, text='brush', command=self.choose_color)
        self.color_button.grid(row=0, column=2)


