from tkinter import ttk
import tkinter.font as font


i=0
class Perfilmo(ttk.Frame):
    def __init__(self,parent,show_menu,show_preliminar):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        botones_container = ttk.Frame(
            self,
            padding="30 15 30 15"
        )
        botones_container.grid(row=0, column=0, sticky="EW", padx=100, pady=100)
        fuente = font.Font(family="Ms Sans Serif")


        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)

        titulo_etiqueta = ttk.Label(botones_container, text="Opciones de perfil medico",font= fuente)
        titulo_etiqueta.grid(row=0 , column=1,sticky="EW")

        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1, column=1, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="")
        Espacio2.grid(row=2, column=1, sticky="EW")

        Espacio3 = ttk.Button(botones_container, text="Datos preliminares", command= show_preliminar)
        Espacio3.grid(row=3, column=0,sticky="EW")

        Boton_resultados= ttk.Button(botones_container, text="Resultados")
        Boton_resultados.grid(column=2,row=3,sticky="EW")

        Boton_atras= ttk.Button(botones_container, text="Atras", command=show_menu)
        Boton_atras.grid(column=2,row=4,sticky="EW")