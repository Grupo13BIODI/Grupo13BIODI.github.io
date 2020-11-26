import tkinter as tk
from tkinter import ttk
import tkinter.font as font
root = tk.Tk()
N=1
P=2
root.title("Historial de probabilidades")
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)
ttk.Label(root, text="Historial de probabilidades", padding=(30, 10)).pack()
#probabilidades
probabilidades_frame=ttk.Frame(root, padding=(20,10,20,0))
probabilidades_frame.pack(fill="both")
ttk.Label(probabilidades_frame, text=f"Semana {N}").pack(side="left")
ttk.Label(probabilidades_frame, text=f"{P}%").pack(side="right")
#atras
boton_atras =ttk.Button(root, text="Atras", command=root.destroy).pack()
root.mainloop()
