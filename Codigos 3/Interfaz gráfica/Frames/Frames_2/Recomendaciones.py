from tkinter import ttk
import tkinter.font as font

class recomendaciones(ttk.Frame):
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

        Recomendacion = ttk.Label(botones_container, text="En muchos de los casos las infecciones ocurren por una alteración hormonal.\nDurante el embarazo la vagina segrega fluidos,\n por ello debe haber un mayor cuidado en la higiene vaginal", font= fuente)
        Recomendacion.grid(row=0, column=0, sticky="EW")

        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1, column=1, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="")
        Espacio2.grid(row=2, column=1, sticky="EW")



        Atras = ttk.Button(botones_container, text="Atras", command=show_menu)
        Atras.grid(column=2,row=3,sticky="NSEW")