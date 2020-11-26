import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
root.title("Recomendaciones")
consejo="'Deja de consumir tabaco definitivamente'"
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)

#recomendaciones
ttk.Label(root, text="Recomendaciones", padding=(30, 10)).pack()
Nombre_frame=ttk.Frame(root, padding=(20,10,20,0))
Nombre_frame.pack(fill="both")
boton_i =ttk.Button(Nombre_frame, text="<").pack(side="left")
ttk.Label(Nombre_frame, text=f"{consejo}", padding=(30, 10)).pack(side="left")
boto_d = ttk.Button(Nombre_frame, text=">").pack(side="left")
salida_frame=ttk.Frame(root, padding=(20,10,20,0))
salida_frame.pack(fill="both")
boton_atras =ttk.Button(salida_frame, text="Atras", command=root.destroy).pack(side="right")

root.mainloop()
