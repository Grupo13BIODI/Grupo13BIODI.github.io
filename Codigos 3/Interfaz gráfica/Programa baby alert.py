import tkinter as tk
from tkinter import ttk
from Frames import Preliminar_f, menu
from Frames.Frames_2 import preguntas, Perfilmo, recomendaciones, probabilidad
from Frames.Frames_2.Frames_3 import historial, preliminar
from Frames.Frames_2.Frames_3.Frames_4 import Preliminar_E


class Principal(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.title("Programa Baby Alert")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        container= ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)


        self.frames = dict()

        Preliminar_frame = Preliminar_f(container, lambda: self.show_frame(menu))
        Preliminar_frame.grid(row=0, column=0)

        Menu_frame = menu(container, lambda: self.show_frame(preguntas), lambda: self.show_frame(Perfilmo), lambda: self.show_frame(recomendaciones), lambda: self.show_frame(probabilidad))
        Menu_frame.grid(row=0, column=0)

        Preguntas_frame= preguntas(container, lambda: self.show_frame(menu))
        Preguntas_frame.grid(row=0, column=0)

        Perfilo_frame= Perfilmo(container, lambda: self.show_frame(menu), lambda: self.show_frame(preliminar))
        Perfilo_frame.grid(row=0, column=0)

        Recomendaciones_frame = recomendaciones(container, lambda: self.show_frame(menu))
        Recomendaciones_frame.grid(row=0, column=0)

        Probabilidad_frame = probabilidad(container, lambda: self.show_frame(menu), lambda: self.show_frame(historial))
        Probabilidad_frame.grid(row=0, column=0)

        Historial_frame = historial(container, lambda: self.show_frame(probabilidad))
        Historial_frame.grid(row=0, column=0)

        Datos_frame = preliminar(container, lambda: self.show_frame(Perfilmo), lambda: self.show_frame(Preliminar_E))
        Datos_frame.grid(row=0, column=0)

        DatosE_frame = Preliminar_E(container, lambda: self.show_frame(preliminar))
        DatosE_frame.grid(row=0, column=0)



        self.frames[Preliminar_f] = Preliminar_frame
        self.frames[menu] = Menu_frame
        self.frames[preguntas] = Preguntas_frame
        self.frames[Perfilmo] = Perfilo_frame
        self.frames[recomendaciones] = Recomendaciones_frame
        self.frames[probabilidad] = Probabilidad_frame
        self.frames[historial] = Historial_frame
        self.frames[preliminar]= Datos_frame
        self.frames[Preliminar_E] = DatosE_frame


        i=1
        if i==1:
         self.show_frame(Preliminar_f)
        else:
         self.show_frame(menu)


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()




app = Principal()


style= ttk.Style(app)
print(style.theme_use("clam"))
app.mainloop()