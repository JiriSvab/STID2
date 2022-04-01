import os
import pypandoc
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = tk.Tk()
root.title(".docx to .html converter")


def open_file():
    word_file = filedialog.askopenfilename(initialdir='C:\\Users\\jiri.svab\\Desktop\\Requests\\Byrne-Michelle')
    output = pypandoc.convert_file(word_file, 'html', outputfile='test2_html.html')


open_file_btn = Button(root, text="Open file", command=open_file, fg="white", bg="green")
open_file_btn.grid(row=0, column=1, sticky="WE", padx=100, pady=10, ipadx=70)


root.mainloop()
