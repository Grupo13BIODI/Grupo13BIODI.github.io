import tkinter as tk
from tkinter import ttk

class Preliminar_f(ttk.Frame):
    def __init__(self,parent,show_menu):
        super().__init__(parent)


        def Comprobar():
            e = int(Edad.get())
            if e>=1:
             Boton_siguiente= ttk.Button(Boton_container, text="Siguiente", command=show_menu, cursor="hand2")
             Boton_siguiente.grid(column=3, row=0)



        #Nombre

        Nombre_container = ttk.Frame(self)
        Nombre_container.grid(sticky="W")
        Nombre_container.columnconfigure(0,weight =1)

        Nombre_etiqueta = ttk.Label(Nombre_container, text="Coloque su nombre")
        Nombre_etiqueta.grid(row=0 , column=0,sticky="W")
        Nombre= tk.StringVar(Nombre_container)
        Nombre_entrada = tk.Entry(Nombre_container,width=20, textvariable= Nombre)
        Nombre_entrada.grid(row=0, column=1,sticky="W")

        #Edad

        Datos_container = ttk.Frame(self)
        Datos_container.grid(sticky="EW")
        Datos_container.columnconfigure(0,weight =1)

        Edad_etiqueta = ttk.Label(Datos_container, text="Coloque su edad:")
        Edad_etiqueta.grid(row=0, column=0,sticky="W")
        Edad = tk.IntVar(Datos_container)
        Edad_entrada = tk.Entry(Datos_container,width=2, textvariable=Edad)
        Edad_entrada.grid(row=0, column=1,sticky="W")

        #Peso

        Peso_etiqueta = ttk.Label(Datos_container, text="Coloque su peso")
        Peso_etiqueta.grid(row=0 , column=2,sticky="W")
        Peso= tk.StringVar(Datos_container)
        Peso_entrada = tk.Entry(Datos_container,width=2, textvariable= Peso)
        Peso_entrada.grid(row=0, column=3,sticky="W")

        #Talla

        Talla_etiqueta = ttk.Label(Datos_container, text="Coloque su talla")
        Talla_etiqueta.grid(row=0 , column=4,sticky="W")
        Talla= tk.StringVar(Datos_container)
        Talla_entrada = tk.Entry(Datos_container,width=2, textvariable=Talla)
        Talla_entrada.grid(row=0, column=5,sticky="W")

        #Mes de gestación

        Mes_container = ttk.Frame(self)
        Mes_container.grid(sticky="W")
        Mes_container.columnconfigure(0,weight =1)

        Mes_etiqueta = ttk.Label(Mes_container, text="Coloque su mes de gestación")
        Mes_etiqueta.grid(row=0, column=0,sticky="W")
        Mes= tk.StringVar(Mes_container)
        Mes_entrada = tk.Entry(Mes_container,width=10, textvariable=Mes)
        Mes_entrada.grid(row=0, column=1,sticky="W")

        #Enfermedad no considerable

        Enc_container = ttk.Frame(self)
        Enc_container.grid(sticky="W")
        Enc_container.columnconfigure(0,weight =1)

        Enc_etiqueta = ttk.Label(Enc_container, text="Si padece de alguna enfermedad coloquela: ")
        Enc_etiqueta.grid(row=3 , column=0, sticky="W")
        Enc= tk.StringVar(Enc_container)
        Enc_entrada = tk.Entry(Enc_container,width=20, textvariable=Enc)
        Enc_entrada.grid(row=3, column=1,sticky="W")

        Boton_container = ttk.Frame(self)
        Boton_container.grid(sticky="W")
        Boton_container.columnconfigure(0,weight =1)

        Boton_siguiente= ttk.Button(Boton_container, text="Comprobar", command=Comprobar, cursor="hand2")
        Boton_siguiente.grid(column=3, row=0)







