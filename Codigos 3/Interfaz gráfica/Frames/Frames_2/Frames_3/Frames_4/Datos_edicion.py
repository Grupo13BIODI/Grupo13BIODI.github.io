import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class Preliminar_E(ttk.Frame):
    def __init__(self,parent,show_preliminar):
        super().__init__(parent)


        def Guardar():
            N = Nombre.get()
            E = int(Edad.get())
            P = float(Peso.get())
            T = float(Talla.get())
            S = int(Semana.get())
            ENC = Enc.get()
            EC = Enfermedad.get()

            if((E>=14 and E<=55)and (T>=1.3 and T<=2.10)) and ((P >= (((T*100)-100)-20) and P <= (((T*100)-100)+20)) and (S>=0 and S<=40)) and (N and ENC and EC):
                Salida = ttk.Label(self, text="¡Datos guardados con exito!")
                Salida.grid(row=6, column=0,sticky="W")

            else:
                Salida = ttk.Label(self, text="Datos incorrectos \nSi no presenta enfermedades coloque ninguna")
                Salida.grid(row=6, column=0,sticky="W")




        fuente = font.Font(family="Ms Sans Serif")
        #Nombre

        Nombre_container = ttk.Frame(self,padding="100 4")
        Nombre_container.grid(sticky="W")
        Nombre_container.columnconfigure(0,weight =1)

        Nombre_etiqueta = ttk.Label(Nombre_container, text="Coloque su nombre",font= fuente)
        Nombre_etiqueta.grid(row=0 , column=0,sticky="W")
        Nombre = tk.StringVar()
        Nombre_entrada = tk.Entry(Nombre_container,width=20, textvariable= Nombre)
        Nombre_entrada.grid(row=0, column=1,sticky="W")

        #Edad

        Datos_container = ttk.Frame(self,padding="100 4")
        Datos_container.grid(sticky="EW")
        Datos_container.columnconfigure(0,weight =1)

        Edad_etiqueta = ttk.Label(Datos_container, text="Coloque su edad:",font= fuente)
        Edad_etiqueta.grid(row=0, column=0,sticky="W")
        Edad = tk.IntVar()
        Edad_entrada = tk.Entry(Datos_container,width=5, textvariable=Edad)
        Edad_entrada.grid(row=0, column=1,sticky="W")

        #Peso

        Peso_etiqueta = ttk.Label(Datos_container, text="Coloque su peso",font= fuente)
        Peso_etiqueta.grid(row=0 , column=2,sticky="W")
        Peso= tk.DoubleVar()
        Peso_entrada = tk.Entry(Datos_container,width=5, textvariable= Peso)
        Peso_entrada.grid(row=0, column=3,sticky="W")

        #Talla

        Talla_etiqueta = ttk.Label(Datos_container, text="Coloque su talla",font= fuente)
        Talla_etiqueta.grid(row=0 , column=4,sticky="W")
        Talla= tk.DoubleVar()
        Talla_entrada = tk.Entry(Datos_container,width=5, textvariable=Talla)
        Talla_entrada.grid(row=0, column=5,sticky="W")

        #Semana de gestación

        Semana_container = ttk.Frame(self,padding="100 4")
        Semana_container.grid(sticky="W")
        Semana_container.columnconfigure(0,weight =1)

        Semana_etiqueta = ttk.Label(Semana_container, text="Coloque su semana de gestación",font= fuente)
        Semana_etiqueta.grid(row=0, column=0,sticky="W")
        Semana= tk.IntVar()
        Semana_entrada = tk.Entry(Semana_container,width=10, textvariable=Semana)
        Semana_entrada.grid(row=0, column=1,sticky="W")

        #Enfermedad no considerable

        Enc_container = ttk.Frame(self,padding="100 4")
        Enc_container.grid(sticky="W")
        Enc_container.columnconfigure(0,weight =1)

        Enc_etiqueta = ttk.Label(Enc_container, text="Si padece de alguna enfermedad coloquela: ",font= fuente)
        Enc_etiqueta.grid(row=3 , column=0, sticky="W")
        Enc= tk.StringVar()
        Enc_entrada = tk.Entry(Enc_container,width=20, textvariable=Enc)
        Enc_entrada.grid(row=3, column=1,sticky="W")

        #Enfermedad considerable
        lista_frame= ttk.Frame(self,padding="100 4")
        lista_frame.grid(sticky="W")
        lista_frame.columnconfigure(0, weight=1)

        Enfermedad_seleccionada = tk.StringVar()
        Enfermedad_etiqueta= ttk.Label(lista_frame, text = "Seleccione una enfermedad:",font= fuente)
        Enfermedad_etiqueta.grid(column= 0, row=0)
        Enfermedad = ttk.Combobox(lista_frame, textvariable=Enfermedad_seleccionada)
        Enfermedad["values"] = ("Diabetes","Asma","Anomalías utero-cervicales","Cardiopatías","Anemia", "Ninguna")
        Enfermedad.grid(column= 1 , row=0)

        Boton_container = ttk.Frame(self,padding="100 4")
        Boton_container.grid(sticky="W")
        Boton_container.columnconfigure(0,weight =1)

        Boton_comprobar= ttk.Button(Boton_container, text="Guardar", command=Guardar, cursor="hand2")
        Boton_comprobar.grid(column=0, row=0)

        Boton_regresar= ttk.Button(Boton_container, text="Regresar", command=show_preliminar, cursor="hand2")
        Boton_regresar.grid(column=1, row=0)