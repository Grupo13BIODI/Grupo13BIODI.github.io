from tkinter import ttk
i=0
class historial(ttk.Frame):
    def __init__(self,parent, show_probabilidad):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        botones_container = ttk.Frame(
            self,
            padding="30 15 30 15"
        )
        botones_container.grid(row=0, column=0, sticky="EW", padx=100, pady=100)

        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)

        Nombre_etiqueta = ttk.Label(botones_container, text="Historial de probabilidades: ")
        Nombre_etiqueta.grid(row=0 , column=1,sticky="EW")

        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1, column=1, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="Semana 1:")
        Espacio2.grid(row=2, column=0, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="3 %")
        Espacio2.grid(row=2, column=2, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="Semana 2:")
        Espacio2.grid(row=3, column=0, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="4 %")
        Espacio2.grid(row=3, column=2, sticky="EW")

        Boton_si= ttk.Button(botones_container, text="Atras", command=show_probabilidad)
        Boton_si.grid(column=2,row=4,sticky="EW")