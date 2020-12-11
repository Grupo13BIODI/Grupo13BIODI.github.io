from tkinter import ttk
import tkinter.font as font

class probabilidad(ttk.Frame):
    def __init__(self, parent, show_menu, show_historial):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)

        i = 1

        botones_container = ttk.Frame(
            self,
            padding="30 15 30 15"
        )
        botones_container.grid(row=0, column=0, sticky="EW", padx=100, pady=100)
        fuente = font.Font(family="Ms Sans Serif")


        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)

        Titulo = ttk.Label(botones_container, text="Su probabilidad de parto prematuro es:        ",  font= fuente)
        Titulo.grid(row=0 , column=1,sticky="EW")

        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1, column=1, sticky="EW")

        proba = ttk.Label(botones_container, text=f"{i} %", font= fuente)
        proba.grid(row=2, column=1)

        historial_f = ttk.Label(botones_container, text="Historial de probabilidades ", font= fuente)
        historial_f.grid(row=3, column=1, sticky="W")

        historial = ttk.Button(botones_container, text="Ver historial",command= show_historial)
        historial.grid(row=3, column=1,sticky="E")

        Espacio1 = ttk.Label(botones_container, text="")
        Espacio1.grid(row=4, column=1, sticky="EW")


        Boton_atras = ttk.Button(botones_container, text="Atras", command=show_menu)
        Boton_atras.grid(column=2, row=5, sticky="EW")