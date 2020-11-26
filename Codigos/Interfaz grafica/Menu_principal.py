import tkinter as tk
from tkinter import ttk

a=10

class Menu_principal(tk.Tk):
    def __init__(self):
        super().__init__()



        ttk.Label(self, text="Menu principal", padding=(30, 10)).grid(column=0,row=0)
        container = ttk.Frame(self, padding=(30,15))
        container.grid()
        container.columnconfigure(0,weight=1)


        boton_preguntas_diarias =ttk.Button(self, text="Preguntas diarias")
        boton_preguntas_diarias.grid(column=0, row=1, sticky="EW")
        boton_probabilidad_ppt =ttk.Button(self, text="Probabilidad de parto prematuro")
        boton_probabilidad_ppt.grid(column=0, row=2, sticky="EW")
        boton_perfil_medico =ttk.Button(self, text="Perfil medico")
        boton_perfil_medico.grid(column=0, row=3, sticky="EW")
        boton_consejos =ttk.Button(self, text="Consejos")
        boton_consejos.grid(column=0, row=4, sticky="EW")
        boton_configuraciones =ttk.Button(self, text="Configuración")
        boton_configuraciones.grid(column=0, row=5, sticky="EW")







main = Menu_principal()
main.columnconfigure(0,weight=1)
main.mainloop()