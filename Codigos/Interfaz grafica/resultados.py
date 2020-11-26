import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
style = ttk.Style(root)
style.configure("LargeEntry.TEntry", font=("Segoe UI", 15))
font.nametofont("TkDefaultFont").configure(size=15)


root.title("Resultados")
ttk.Label(root, text="Resultados", padding=(30, 10)).pack()
boton_atras =ttk.Button(root, text="Atras", command=root.destroy).pack()

root.mainloop()