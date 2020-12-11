import tkinter.font as font
from tkinter import ttk


class preliminar(ttk.Frame):
    def __init__(self,parent,show_Perfilmo, show_Preliminar_E):
        super().__init__(parent)







        fuente = font.Font(family="Ms Sans Serif")
        #Nombre

        Nombre_container = ttk.Frame(self,padding="200 200 200 5 ")


        Nombre_container.grid(sticky="W")
        Nombre_container.columnconfigure(0,weight =1)

        Nombre_etiqueta = ttk.Label(Nombre_container, text="Nombre: ",font= fuente)
        Nombre_etiqueta.grid(row=0 , column=0,sticky="W")
        Nombre_salida = ttk.Label(Nombre_container, text="Harola Angeles",font= fuente)
        Nombre_salida.grid(row=0, column=1,sticky="W")

        #Edad

        Datos_container = ttk.Frame(self,padding="200 4")
        Datos_container.grid(sticky="EW")
        Datos_container.columnconfigure(0,weight =1)

        Edad_etiqueta = ttk.Label(Datos_container, text="Edad: ",font= fuente)
        Edad_etiqueta.grid(row=0, column=0,sticky="W")
        Edad_entrada = ttk.Label(Datos_container, text="19",font= fuente)
        Edad_entrada.grid(row=0, column=1,sticky="W")

        #Peso

        Peso_etiqueta = ttk.Label(Datos_container, text="Peso: ",font= fuente)
        Peso_etiqueta.grid(row=0 , column=2,sticky="W")
        Peso_entrada = ttk.Label(Datos_container, text="45",font= fuente)
        Peso_entrada.grid(row=0, column=3,sticky="W")

        #Talla

        Talla_etiqueta = ttk.Label(Datos_container, text="Talla: ",font= fuente)
        Talla_etiqueta.grid(row=0 , column=4,sticky="W")
        Talla_entrada = ttk.Label(Datos_container, text="1.54",font= fuente)
        Talla_entrada.grid(row=0, column=5,sticky="W")

        #Mes de gestación

        Mes_container = ttk.Frame(self,padding="200 5")
        Mes_container.grid(sticky="W")
        Mes_container.columnconfigure(0,weight =1)

        Mes_etiqueta = ttk.Label(Mes_container, text="semana de gestación: ",font= fuente)
        Mes_etiqueta.grid(row=0, column=0,sticky="W")
        Mes_entrada = ttk.Label(Mes_container, text="10",font= fuente)
        Mes_entrada.grid(row=0, column=1,sticky="W")

        #Enfermedad no considerable

        Enc_container = ttk.Frame(self,padding="200 5")
        Enc_container.grid(sticky="W")
        Enc_container.columnconfigure(0,weight =1)

        Enc_etiqueta = ttk.Label(Enc_container, text="Padece:  ",font= fuente)
        Enc_etiqueta.grid(row=3 , column=0, sticky="W")
        Enc_entrada = ttk.Label(Enc_container,text= "Ninguna enfermedad",font= fuente)
        Enc_entrada.grid(row=3, column=1,sticky="W")

        Boton_container = ttk.Frame(self,padding="200 5 200 200")
        Boton_container.grid(sticky="W")
        Boton_container.columnconfigure(0,weight =1)

        Boton_siguiente= ttk.Button(Boton_container, text="Atras", command=show_Perfilmo, cursor="hand2")
        Boton_siguiente.grid(column=3, row=0)

        Boton_editar = ttk.Button(Boton_container, text="Editar", command=show_Preliminar_E, cursor="hand2")
        Boton_editar.grid(column=0, row=0)