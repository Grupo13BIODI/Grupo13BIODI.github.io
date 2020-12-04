import datetime
import math
#función que te dice qué día es
def fecha_actual():
    hoy = datetime.date.today()
    return hoy
#función que te dice cuantos días han transcurridos
#hoy-día inicial
#type datetime.timedelta
def díasTranscurridos(fecha_inicial):
    till_day=fecha_actual()-fecha_inicial
    return till_day
#esta variable debería ser traida desde la base de datos
#debería ser definida para
def till_day():
    fecha_inicial=datetime.date(2020,11,29)
    segundos_transcurridos=díasTranscurridos(fecha_inicial).total_seconds()
    M=segundos_transcurridos/86400
    M_decimal,M_entera =math.modf(M)
    print(type(M_entera))
    return M_entera + 1

print(till_day())

