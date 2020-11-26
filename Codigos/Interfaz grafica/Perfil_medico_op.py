import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
root.title("Perfil medico opciones")
ttk.Label(root, text="Perfil medico opciones", padding=(30, 10)).pack(side="top")
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)
#opciones
opciones_frame=ttk.Frame(root, padding=(20,10,20,0))
opciones_frame.pack(fill="both")
boton_informacion =ttk.Button(opciones_frame, text="Información preliminar").pack(side="left")
boton_resultados =ttk.Button(opciones_frame, text="Resultados").pack(side="right")
boton_atras =ttk.Button(root, text="Atras", command=root.destroy).pack(side="right")

root.mainloop()