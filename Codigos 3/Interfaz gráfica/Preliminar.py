import tkinter as tk
from tkinter import ttk


class Preliminar_f(ttk.Frame):
    def __init__(self,parent,show_menu):
        super().__init__(parent)


        def Comprobar():
            N = Nombre.get()
            E = int(Edad.get())
            P = float(Peso.get())
            T = float(Talla.get())
            S = int(Semana.get())
            ENC = Enc.get()
            EC = Enfermedad.get()

            if((E>=14 and E<=55)and (T>=1.3 and T<=2.10)) and ((P >= (((T*100)-100)-20) and P <= (((T*100)-100)+20)) and (S>=0 and S<=40)) and (N and ENC and EC):
             Boton_siguiente= ttk.Button(Boton_container, text="Siguiente", command=show_menu, cursor="hand2")
             Boton_siguiente.grid(column=0, row=0)

            else:
             Salida = ttk.Label(self, text="Datos incorrectos \nSi no presenta enfermedades coloque ninguna")
             Salida.grid(row=6, column=0,sticky="W")




        #Nombre

        Nombre_container = ttk.Frame(self)
        Nombre_container.grid(sticky="W")
        Nombre_container.columnconfigure(0,weight =1)

        Nombre_etiqueta = ttk.Label(Nombre_container, text="Coloque su nombre")
        Nombre_etiqueta.grid(row=0 , column=0,sticky="W")
        Nombre = tk.StringVar()
        Nombre_entrada = tk.Entry(Nombre_container,width=20, textvariable= Nombre)
        Nombre_entrada.grid(row=0, column=1,sticky="W")

        #Edad

        Datos_container = ttk.Frame(self)
        Datos_container.grid(sticky="EW")
        Datos_container.columnconfigure(0,weight =1)

        Edad_etiqueta = ttk.Label(Datos_container, text="Coloque su edad:")
        Edad_etiqueta.grid(row=0, column=0,sticky="W")
        Edad = tk.IntVar()
        Edad_entrada = tk.Entry(Datos_container,width=5, textvariable=Edad)
        Edad_entrada.grid(row=0, column=1,sticky="W")

        #Peso

        Peso_etiqueta = ttk.Label(Datos_container, text="Coloque su peso")
        Peso_etiqueta.grid(row=0 , column=2,sticky="W")
        Peso= tk.DoubleVar()
        Peso_entrada = tk.Entry(Datos_container,width=5, textvariable= Peso)
        Peso_entrada.grid(row=0, column=3,sticky="W")

        #Talla

        Talla_etiqueta = ttk.Label(Datos_container, text="Coloque su talla")
        Talla_etiqueta.grid(row=0 , column=4,sticky="W")
        Talla= tk.DoubleVar()
        Talla_entrada = tk.Entry(Datos_container,width=5, textvariable=Talla)
        Talla_entrada.grid(row=0, column=5,sticky="W")

        #Semana de gestación

        Semana_container = ttk.Frame(self)
        Semana_container.grid(sticky="W")
        Semana_container.columnconfigure(0,weight =1)

        Semana_etiqueta = ttk.Label(Semana_container, text="Coloque su semana de gestación")
        Semana_etiqueta.grid(row=0, column=0,sticky="W")
        Semana= tk.IntVar()
        Semana_entrada = tk.Entry(Semana_container,width=10, textvariable=Semana)
        Semana_entrada.grid(row=0, column=1,sticky="W")

        #Enfermedad no considerable

        Enc_container = ttk.Frame(self)
        Enc_container.grid(sticky="W")
        Enc_container.columnconfigure(0,weight =1)

        Enc_etiqueta = ttk.Label(Enc_container, text="Si padece de alguna enfermedad coloquela: ")
        Enc_etiqueta.grid(row=3 , column=0, sticky="W")
        Enc= tk.StringVar()
        Enc_entrada = tk.Entry(Enc_container,width=20, textvariable=Enc)
        Enc_entrada.grid(row=3, column=1,sticky="W")

        #Enfermedad considerable
        lista_frame= ttk.Frame(self)
        lista_frame.grid(sticky="W")
        lista_frame.columnconfigure(0, weight=1)

        Enfermedad_seleccionada = tk.StringVar()
        Enfermedad_etiqueta= ttk.Label(lista_frame, text = "Seleccione una enfermedad:")
        Enfermedad_etiqueta.grid(column= 0, row=0)
        Enfermedad = ttk.Combobox(lista_frame, textvariable=Enfermedad_seleccionada)
        Enfermedad["values"] = ("Diabetes","Asma","Anomalías utero-cervicales","Cardiopatías","Anemia", "Ninguna")
        Enfermedad.grid(column= 1 , row=0)

        Boton_container = ttk.Frame(self)
        Boton_container.grid(sticky="W")
        Boton_container.columnconfigure(0,weight =1)

        Boton_comprobar= ttk.Button(Boton_container, text="Comprobar", command=Comprobar, cursor="hand2")
        Boton_comprobar.grid(column=3, row=0)







