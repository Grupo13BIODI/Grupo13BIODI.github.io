
from tkinter import ttk

class menu(ttk.Frame):
    def __init__(self, parent, show_preguntas, show_Perfilmo, show_recomendaciones, show_probabilidad):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        botones_container = ttk.Frame(
            self,
            padding="30 15 30 15"
        )
        botones_container.grid(row=0, column=0, sticky="EW", padx=100, pady=100)

        botones_container.columnconfigure(0, weight=1)
        botones_container.rowconfigure(1, weight=1)


        Preguntas= ttk.Button(botones_container, text="Preguntas diarias",command= show_preguntas)
        Preguntas.grid(column=0,row=0,sticky="NSEW")
        Probabilidad= ttk.Button(botones_container, text="Probabilidad de ppt", command= show_probabilidad)
        Probabilidad.grid(column=0,row=1,sticky="NSEW")
        Perfil= ttk.Button(botones_container, text="Perfíl médico", command=show_Perfilmo)
        Perfil.grid(column=0,row=2,sticky="NSEW")
        Recomendaciones= ttk.Button(botones_container, text="Recomendaciones", command=show_recomendaciones)
        Recomendaciones.grid(column=0,row=3,sticky="NSEW")

