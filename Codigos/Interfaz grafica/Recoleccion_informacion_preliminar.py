#importacion de tkinter

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

def comprobar():
     print(f"Nombre: {Nombre_usuario.get() or 'Faltan datos'}")
     print(f"Talla: {Talla_usuario.get() or 'Faltan datos'}")
     print(f"Nombre: {Nombre_usuario.get() or 'Faltan datos'}")
     print(f"Edad: {Edad_usuario.get() or 'Faltan datos'}")
     print(f"Enfermedad adicional: {Enfermedad_extra_usuario.get() or 'Faltan datos'}")
     print(f"Enfermedad adicional: {Enfermedad.get() or 'Faltan datos'}")


root = tk.Tk()
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)
root.title("Lectura de datos preliminares")
root.columnconfigure(0,weight=1)

input_frame= ttk.Frame(root, padding=(20,10,20,0))
input_frame.pack(fill="both")

#Lectura de nombre
#Nombre
nombre_frame= ttk.Frame(root, padding=(20,10,20,0))
nombre_frame.pack(fill="both")
Nombre_usuario = tk.StringVar()
nombre_etiqueta = ttk.Label(nombre_frame, text="Nombre: ").pack(side="left")
nombre_entrada = ttk.Entry(nombre_frame, width=20, textvariable=Nombre_usuario).pack(side="left")
#edad
edad_frame= ttk.Frame(root, padding=(20,10,20,0))
edad_frame.pack(fill="both")
Edad_usuario = tk.IntVar()
Edad_etiqueta = ttk.Label(edad_frame, text="Edad: ").pack(side="left")
Edad_entrada = ttk.Entry(edad_frame,width=3, textvariable=Edad_usuario).pack(side="left")
#altura
Talla_usuario = tk.StringVar()
Talla_etiqueta = ttk.Label(edad_frame, text="Talla: ").pack(side="left")
Talla_entrada = ttk.Entry(edad_frame,width=3, textvariable=Talla_usuario).pack(side="left")
#peso
Peso_usuario = tk.StringVar()
Peso_etiqueta = ttk.Label(edad_frame, text="Peso: ").pack(side="left")
Peso_entrada = ttk.Entry(edad_frame,width=3, textvariable=Peso_usuario).pack(side="left")
#Mes de gestacion
mes_frame= ttk.Frame(root, padding=(20,10,20,0))
mes_frame.pack(fill="both")
Mdg_usuario = tk.StringVar()
Mdg_etiqueta = ttk.Label(mes_frame, text="Mes de gestación: ").pack(side="left")
Mdg_entrada = ttk.Entry(mes_frame,width=3, textvariable=Mdg_usuario).pack(side="left")
#Enfermedad extra
enfermedad_frame= ttk.Frame(root, padding=(20,10,20,0))
enfermedad_frame.pack(fill="both")
Enfermedad_extra_usuario = tk.StringVar()
Enfermedad_extra_etiqueta = ttk.Label(enfermedad_frame, text="Enfermedad extra: ").pack(side="left")
Enfermedad_extra_entrada = ttk.Entry(enfermedad_frame,width=20, textvariable=Enfermedad_extra_usuario).pack(side="left")
#Lista de enfermedades
lista_frame= ttk.Frame(root, padding=(20,10,20,0))
lista_frame.pack(fill="both")
Enfermedad_seleccionada = tk.StringVar()
Enfermedad_etiqueta= ttk.Label(lista_frame, text = "Seleccione una enfermedad:").pack(side="left")
Enfermedad = ttk.Combobox(lista_frame, textvariable=Enfermedad_seleccionada)
Enfermedad["values"] = ("Diabetes","Asma","Anomalías utero-cervicales","Cardiopatías","Anemia")
Enfermedad.pack(side="left")


boton_comprobar =ttk.Button(root, text="Comprobar lectura", command = comprobar ).pack()
root.mainloop()