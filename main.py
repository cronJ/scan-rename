#!/usr/bin/env python3

import os
from tkinter import *
from tkinter import filedialog


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.directory = ""
        self.list_of_files = []
        self.image = None

        self.directory_label = Label(frame, text="Directory")
        self.directory_label.grid(row=0, column=0)
        self.directory_entry = Entry(frame, width=90)
        self.directory_entry.grid(row=0, column=1)
        self.directory_btn = Button(frame,
                                    text="Load",
                                    command=self.load_directory)
        self.directory_btn.grid(row=0, column=2)

        self.name_label = Label(frame, text="Filename")
        self.name_label.grid(row=1, column=0)
        self.name_entry = Entry(frame, width=90)
        self.name_entry.grid(row=1, column=1)
        self.rename_btn = Button(frame,
                                 text="Rename",
                                 command=self.rename_file)
        self.rename_btn.grid(row=1, column=2)

        self.file_list = Listbox(frame,
                                 listvariable=self.list_of_files,
                                 selectmode=SINGLE,
                                 height=30,
                                 width=50)
        self.file_list.grid(row=3, column=0, columnspan=1)

        self.canvas = Canvas(frame,
                             bg='white',
                             height=100,
                             width=80)
        self.canvas.grid(row=3, column=1, columnspan=2)

    def load_directory(self):
        self.directory = filedialog.askdirectory()
        self.directory_entry.insert(0, self.directory)
        self.update_file_list()

    def rename_file(self):
        print("Rename file to: " + self.name_entry.get())

    def update_file_list(self):
        if self.directory != "":
            for _, _, self.file in os.walk(self.directory):
                for self.element in self.file:
                    self.file_list.insert(END, self.element)
                    self.list_of_files.append(self.element)

    def create_file_image(self):
        self.image = None

    def show_file_image(self):
        self.canvas.create_image(100, 80, anchow=NW, image=self.image)


root = Tk()
root.title("Scan rename")
root.minsize(width=800, height=640)
app = App(root)
root.mainloop()
