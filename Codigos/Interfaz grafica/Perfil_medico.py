import tkinter as tk
from tkinter import ttk
import tkinter.font as font


root = tk.Tk()
root.title("Perfil Medico")
ttk.Label(root, text="Perfíl medico", padding=(30, 10)).pack()
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)
Nombre="Harola Angeles "
Edad="19"
Peso="45"
Talla="1.5"
Mdg="2do mes"
Enfermedad_c="Diabetes"
Enfermedad_nc="Ninguna"


#nombre
Nombre_frame=ttk.Frame(root, padding=(20,10,20,0))
Nombre_frame.pack(fill="both")
ttk.Label(Nombre_frame, text=f"Nombre: {Nombre} ", padding=(30, 10)).pack(side="left")
#edad
Edad_frame=ttk.Frame(root, padding=(20,10,20,0))
Edad_frame.pack(fill="both")
ttk.Label(Edad_frame, text=f"Edad: {Edad} años", padding=(30, 10)).pack(side="left")
#peso
ttk.Label(Edad_frame, text=f"Peso: {Peso} kg", padding=(30, 10)).pack(side="left")
#Talla
ttk.Label(Edad_frame, text=f"Talla: {Talla} m", padding=(30, 10)).pack(side="left")
#Mes de gestacion
Mdg_frame=ttk.Frame(root, padding=(20,10,20,0))
Mdg_frame.pack(fill="both")
ttk.Label(Mdg_frame, text=f"Mes de gestación: {Mdg}", padding=(30, 10)).pack(side="left")
#Enfermedad adicional
EnfermedadA_frame=ttk.Frame(root, padding=(20,10,20,0))
EnfermedadA_frame.pack(fill="both")
ttk.Label(EnfermedadA_frame, text=f"Enfermedad considerable: {Enfermedad_c}", padding=(30, 10)).pack(side="left")
#Enfermedad no considerable
Enfermedadnc_frame=ttk.Frame(root, padding=(20,10,20,0))
Enfermedadnc_frame.pack(fill="both")
ttk.Label(Enfermedadnc_frame, text=f"Enfermedad no considerable: {Enfermedad_nc}", padding=(30, 10)).pack(side="left")
#Botones
botones_frame=ttk.Frame(root, padding=(20,10,20,0))
botones_frame.pack(fill="both")
boton_editar =ttk.Button(botones_frame, text="Editar").pack(side="left")
boton_atras =ttk.Button(botones_frame, text="Atras", command=root.destroy).pack(side="right")

root.mainloop()