from tkinter import ttk
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

        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)

        Nombre_etiqueta = ttk.Label(botones_container, text="Opciones de perfil medico")
        Nombre_etiqueta.grid(row=0 , column=1,sticky="EW")

        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1, column=1, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="")
        Espacio2.grid(row=2, column=1, sticky="EW")

        Espacio = ttk.Button(botones_container, text="Datos preliminares", command= show_preliminar)
        Espacio.grid(row=3, column=0,sticky="EW")

        Boton_si= ttk.Button(botones_container, text="Resultados")
        Boton_si.grid(column=2,row=3,sticky="EW")

        Boton_si= ttk.Button(botones_container, text="Atras", command=show_menu)
        Boton_si.grid(column=2,row=4,sticky="EW")