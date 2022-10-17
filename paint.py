from tkinter import Tk, Button


class Paint:
    pen_size: float = 5.0
    color: str = 'black'

    def __init__(self):
        self.root: Tk = Tk()

        self.pen_button: Button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)


