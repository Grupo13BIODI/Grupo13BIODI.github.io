import tkinter.font as font
from tkinter import ttk

class preguntas(ttk.Frame):
    def __init__(self,parent,show_menu):
        super().__init__(parent)



        self.columnconfigure(0, weight=1)
        fuente = font.Font(family="Ms Sans Serif")



        botones_container = ttk.Frame(
            self,
            padding="30 15 30 15"
        )
        botones_container.grid(row=0, column=0, sticky="EW", padx=100, pady=100)

        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)
        Nombre_etiqueta = ttk.Label(botones_container, text="¿Ha sentido cólicos en el útero?", font= fuente)
        Nombre_etiqueta.grid(row=0 , column=1,sticky="EW")
        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1 , column=1,sticky="EW")
        Boton_si= ttk.Button(botones_container, text="Si")
        Boton_si.grid(column=0,row=2,sticky="NSEW")
        Boton_no= ttk.Button(botones_container, text="No")
        Boton_no.grid(column=2,row=2,sticky="NSEW")
        Espacio2 = ttk.Label(botones_container, text="")
        Espacio2.grid(row=3 , column=1,sticky="EW")
        Atras= ttk.Button(botones_container, text="Atras",command=show_menu)
        Atras.grid(column=2,row=4,sticky="NSEW")
