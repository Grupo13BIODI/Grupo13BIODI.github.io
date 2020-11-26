import tkinter as tk
from tkinter import ttk
import tkinter.font as font




class Probabilidad(tk.Tk):
    def __init__(self):
        super().__init__()
        ppt=10

        style = ttk.Style(self)
        style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
        font.nametofont("TkDefaultFont").configure(size=15)

        ttk.Label(self, text="Probabilidad de parto prematuro", padding=(30, 10)).grid(column=0,row=0)
        ttk.Label(self, text="Usted presenta una probabilidad de: ", padding=(30, 10)).grid(column=0,row=1)
        ttk.Label(self, text=f"{ppt}%", padding=(30, 10)).grid(column=0,row=2)
        boton_historial =ttk.Button(self, text="Historial de probabilidades")
        boton_historial.grid(column=0,row=3)
        boton_atras =ttk.Button(self, text="Atras")
        boton_atras.grid(column=1,row=4)

main = Probabilidad()
main.columnconfigure(0,weight=1)
main.mainloop()