from tkinter import ttk

class recomendaciones(ttk.Frame):
    def __init__(self,parent,show_menu):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)


        botones_container = ttk.Frame(
            self,
            padding="30 15 30 15"
        )
        botones_container.grid(row=0, column=0, sticky="EW", padx=100, pady=100)

        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)

        Recomendacion = ttk.Label(botones_container, text="'Aqui va el texto de las recomendaciones'")
        Recomendacion.grid(row=0, column=0, sticky="EW")

        Espacio = ttk.Label(botones_container, text="")
        Espacio.grid(row=1, column=1, sticky="EW")

        Espacio2 = ttk.Label(botones_container, text="")
        Espacio2.grid(row=2, column=1, sticky="EW")



        Atras = ttk.Button(botones_container, text="Atras", command=show_menu)
        Atras.grid(column=2,row=3,sticky="NSEW")