import shared._MapperTools as corefunc
from Tkinter import (Tk)
import source.Mapper as Mapper


def set_geometry(raiz):
    tskbar_width, tskbar_height = corefunc.get_taskbar_hw()
    y = 420 - tskbar_height
    geometry_str = '{width}x{height}+{x}+{y}'.format(width='255', height='420', x=tskbar_width, y=y)
    raiz.geometry(geometry_str)


# Tk padrao
raiz = Tk()
raiz.resizable(width=False, height=False)
raiz.title("Mapper")
set_geometry(raiz)
disp = Mapper.App(raiz)
raiz.mainloop()