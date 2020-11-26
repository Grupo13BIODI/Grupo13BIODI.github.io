import tkinter as tk
from tkinter import ttk
import tkinter.font as font
#Por completaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar


root = tk.Tk()
root.title("Preguntas diarias")
font.nametofont("TkDefaultFont").configure(size=15)
root.title("Lectura de datos preliminares")
i=1
#Titulo
ttk.Label(root, text="Preguntas diarias", padding=(30, 10)).pack()
#Conteador
numero_frame=ttk.Frame(root, padding=(20,10,20,0))
numero_frame.pack(fill="both")
numero = ttk.Label(numero_frame, text=f"{i}/10").pack(side="right")
#Texto de pregunta
preguntas_frame=ttk.Frame(root, padding=(20,10,20,0))
preguntas_frame.pack(fill="both")
Pregunta= tk.StringVar()
Enfermedad_extra_etiqueta = ttk.Label(preguntas_frame, text="¿Siente dificultades para respirar?").pack()
#botones
botones_frame=ttk.Frame(root, padding=(20,10,20,0))
botones_frame.pack(fill="both")
boton_si =ttk.Button(botones_frame, text="Si", command=1+i).pack(side="left")
boton_no =ttk.Button(botones_frame, text="No", command=i+1).pack(side="right")
#saluda
atras_frame=ttk.Frame(root, padding=(20,10,20,0))
atras_frame.pack(fill="both")
boton_atras =ttk.Button(atras_frame, text="Atras", command=root.destroy).pack(side="right")





root.columnconfigure(0,weight=1)
root.mainloop()
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)