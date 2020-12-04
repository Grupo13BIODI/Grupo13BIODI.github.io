import tkinter as tk
from tkinter import ttk

class preliminar(ttk.Frame):
    def __init__(self,parent,show_Perfilmo, show_Preliminar_f):
        super().__init__(parent)


        #Nombre

        Nombre_container = ttk.Frame(self)

        Nombre_container.grid(sticky="W")
        Nombre_container.columnconfigure(0,weight =1)

        Nombre_etiqueta = ttk.Label(Nombre_container, text="Nombre: ")
        Nombre_etiqueta.grid(row=0 , column=0,sticky="W")
        Nombre_salida = tk.Label(Nombre_container, text="Harola Angeles")
        Nombre_salida.grid(row=0, column=1,sticky="W")

        #Edad

        Datos_container = ttk.Frame(self)
        Datos_container.grid(sticky="EW")
        Datos_container.columnconfigure(0,weight =1)

        Edad_etiqueta = ttk.Label(Datos_container, text="Edad: ")
        Edad_etiqueta.grid(row=0, column=0,sticky="W")
        Edad_entrada = tk.Label(Datos_container, text="19")
        Edad_entrada.grid(row=0, column=1,sticky="W")

        #Peso

        Peso_etiqueta = ttk.Label(Datos_container, text="Peso: ")
        Peso_etiqueta.grid(row=0 , column=2,sticky="W")
        Peso_entrada = tk.Label(Datos_container, text="112")
        Peso_entrada.grid(row=0, column=3,sticky="W")

        #Talla

        Talla_etiqueta = ttk.Label(Datos_container, text="Talla: ")
        Talla_etiqueta.grid(row=0 , column=4,sticky="W")
        Talla_entrada = tk.Label(Datos_container, text="1.54")
        Talla_entrada.grid(row=0, column=5,sticky="W")

        #Mes de gestación

        Mes_container = ttk.Frame(self)
        Mes_container.grid(sticky="W")
        Mes_container.columnconfigure(0,weight =1)

        Mes_etiqueta = ttk.Label(Mes_container, text="Mes de gestación: ")
        Mes_etiqueta.grid(row=0, column=0,sticky="W")
        Mes_entrada = tk.Label(Mes_container, text="2do mes")
        Mes_entrada.grid(row=0, column=1,sticky="W")

        #Enfermedad no considerable

        Enc_container = ttk.Frame(self)
        Enc_container.grid(sticky="W")
        Enc_container.columnconfigure(0,weight =1)

        Enc_etiqueta = ttk.Label(Enc_container, text="Padece:  ")
        Enc_etiqueta.grid(row=3 , column=0, sticky="W")
        Enc_entrada = tk.Label(Enc_container,text= "Ninguna enfermedad")
        Enc_entrada.grid(row=3, column=1,sticky="W")

        Boton_container = ttk.Frame(self)
        Boton_container.grid(sticky="W")
        Boton_container.columnconfigure(0,weight =1)

        Boton_siguiente= ttk.Button(Boton_container, text="Atras", command=show_Perfilmo, cursor="hand2")
        Boton_siguiente.grid(column=3, row=0)

        Boton_editar = ttk.Button(Boton_container, text="Editar", command=show_Preliminar_f, cursor="hand2")
        Boton_editar.grid(column=0, row=0)