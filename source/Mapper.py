from Tkinter import (Tk, Frame, StringVar, Label, Listbox, Scrollbar,
                     Entry, Checkbutton, END, EXTENDED, Button, HORIZONTAL, BROWSE, Toplevel)


class App(Frame):
    def __init__(self, raiz=None):
        self.gui_mapper(raiz)

    def gui_mapper(self, raiz):
        self.raiz = raiz
        self.label_aba_conectar = Label(raiz, text='conectar', bg='#EEEEEE')
        self.label_aba_conectar.place(x=10, y=10)

