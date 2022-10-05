from tkinter import Frame, Entry, Tk, Button, TOP, Scrollbar, RIGHT, Y, Text, WORD, END, INSERT

import wikipedia
from wikipedia import PageError


def get_data() -> None:
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except PageError:
        answer.insert(INSERT, "ERROR! Invalid input or poor internet connection!")


windows = Tk()
windows.title("Wikipedia Search")
top_frame = Frame(windows)
entry = Entry(top_frame)
entry.pack()
button = Button(top_frame, text="SEARCH", command=get_data)
button.pack()
top_frame.pack(side=TOP)

bottom_frame = Frame(windows)
scroll = Scrollbar(bottom_frame)
scroll.pack(side=RIGHT, fill=Y)
answer = Text(bottom_frame, width=50, height=20,
              yscrollcommand=scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottom_frame.pack()

windows.mainloop()
