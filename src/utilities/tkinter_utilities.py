import tkinter as tk
from tkinter import messagebox as mb, ttk
from tkinter.simpledialog import SimpleDialog as sd


# messagebox functions
def show_message(title, message):
    mb.showinfo(title, message)


def show_error(title, message):
    mb.showerror(title, message)


def show_warning(title, message):
    mb.showwarning(title, message)


def show_input_dialog(title, message):
    return sd.askstring(title, message)
