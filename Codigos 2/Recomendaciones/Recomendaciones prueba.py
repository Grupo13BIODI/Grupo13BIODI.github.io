días_transcurridos=int(input("Coloque los días trancurridos"))
print(f"{días_transcurridos}")
def R2(días_transcurridos):
    if días_transcurridos%7==0:
        if días_transcurridos==7:
            print(f"Recomendación semanal {días_transcurridos}")
            print (f"Peso alto: Realizar caminatas cortas y balancear la comida.Peso bajo:No olvides consumir proteínas y carbohidratos en tus horas de almuerzo, además de consumir un buen desayuno.")
        elif días_transcurridos==14:
            print(f"Recomendación semanal {días_transcurridos}")
            print (f"Se recomienda que durante el embarazo no se consuman drogas no médicas , porque estas pueden manifestar alguna deformación congénita en su bebé , como por ejemplo labio fisurado.")
        elif días_transcurridos==21:
            print(f"Recomendación semanal {días_transcurridos}")
            print (f"Recuerde que asistir a sus controles médicos establecidos son de suma importancia ya que puede resolver dudas de su embarazo y además porque se lleva un control del feto.")
        else:
            print(f"Recomendación semanal {días_transcurridos}")
            print (f"Muchas veces las contracciones llamadas “contracciones de Braxton Hicks” generan el endurecimiento del abdomen pero no es muy significativo. Si usted siente un malestar mayor puede consultar con un médico pero no es necesario alarmarse; su bebé está desarrollándose.")
    else:
       if días_transcurridos==1:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"En muchos de los casos las infecciones ocurren por una alteración hormonal.  Durante el embarazo la vagina segrega fluidos , por ello debe haber un mayor cuidado en la higiene vaginal. ")
       elif días_transcurridos==2:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"!Calma! Estos dolores son normales , pero lo recomendable es relajarse y estar en una posición que le transmita tranquilidad , así mismo se recomienda evitar alimentos que generan gases.")
       elif días_transcurridos==3:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Las ganas de orinar constantemente pueden ser comunes durante el embarazo. Sin embargo; si  usted expulsa pequeñas cantidades de orina puede ser  un signo de infección urinaria , por favor acérquese al establecimiento de salud más cercano.")
       elif días_transcurridos==4:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Es recomendable asistir a un doctor puesto que la hematuria puede representar tanto una infección urinaria como un desprendimiento de placenta. Este último podría afectar el desarrollo del feto.")
       elif días_transcurridos==5:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"!Es importante que durante su embarazo , tenga momentos de ocio , como dormir , ver la televisión , jugar cartas , actividades que la hagan sentir cómoda ! ")
       elif días_transcurridos==6:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"!Tranquilidad,  luego de la lluvia llega el arcoiris, todo lo malo pasa en algún momento , recuerda que tienes una vida adentro que espera ansiosamente en verte ! Ante cualquier problema siempre es bueno ser escuchado y más por personas que nos aman como nuestros familiares.")
       elif días_transcurridos==8:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Si sufre alguna caída no dude en asistir al médico puesto que puede suponer un riesgo no atender una contusión que afecte el desarrollo del feto. Entre el 10 y 30% de traumatismos puede generar fatalidad")
       elif días_transcurridos==9:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Si usted observa que su flujo vaginal tiene un color verdoso, amarillento ,  es espeso , con mal olor y ardor, es posible que usted tenga vaginitis , por lo que se le recomienda ir al establecimiento de salud ,más cercano ya que esto puede afectar a su embarazo")
       elif días_transcurridos==10:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"El olor de las segregaciones vaginales debe ser leve y sutil, si encuentra olores muy inusuales con mucha intensidad poco frecuente consuma menos azúcares y balancee la dieta que mantiene. Si persiste puede ser producto de una infección intravaginal. (Acudir al especialista)")
       elif días_transcurridos==11:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Si hasta el momento ha sentido contracciones que no son dolorosas pero sí muy frecuentes, más aún durante el sexto mes de embarazo no se alarme, es parte del flujo normal de un embarazo. Por otro lado, si siente contracciones que provocan mucho dolor, no dude en asistir al doctor porque este tipo de contracciones son conocidas como patológicas y pueden desencadenar un parto prematuro espontáneo.")
       elif días_transcurridos==12:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"El dolor en la parte inferior de la espalda es común durante el embarazo , pues esto se debe a que en este período se gana más peso progresivamente y tu columna debe soportar esto. Algunas recomendaciones para no sentir con tanta frecuencia e intensidad estos dolores son: no usar tacones para caminar, no levantar mucho peso, dormir en una posición cómoda y correcta , finalmente dormir en un colchón bueno también ayudará a disminuir esta molestia.")
       elif días_transcurridos==13:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Es muy común experimentar mareos si ha realizado alguna acción brusca. Asimismo recuerde que su tensión arterial muchas veces disminuirá, lo mejor que puede hacer es acostarse de costado izquierdo para regular el flujo sanguíneo y evitar consumir calmantes(drogas). No permanezca en lugares cerrados o con temperaturas altas.Si conoce que es deficiente en producción de hierro,consuma alimentos ricos en este como carnes rojas, hígado y frutos secos.")
       elif días_transcurridos==15:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Se le recomienda evitar realizar grandes esfuerzos, no acostarse boca abajo y tratar de reducir la ansiedad. Si aún siente dificultad para respirar debe sentarse y concentrarse en su propia respiración, tratando de calmarse lo máximo posible.")
       elif días_transcurridos==16:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Si ha notado esta pigmentación en su piel puede ser ocasionada por la llamada colestasis del embarazo que es producida en el hígado. Esto ocasiona que la circulación de la propia bilis entre en retraso, y esto a su vez puede afectar el desarrollo de su bebé. Dicha situación escapa de sus manos por lo que debe acudir inmediatamente al doctor")
       elif días_transcurridos==17:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Futura madre no te olvides del seguimiento que debes tener en este proceso tan bello de vida")
       elif días_transcurridos==18:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Recuerda acariciar tu vientre, los bebés siempre responden a los estímulos que se le generan. Tener una bonito con tu bebé es algo muy importante")
       elif días_transcurridos==19:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Recuerda estar alerta ante cualquier síntoma inusual en tu cuerpo, ya sea visible o sensible.")
       elif días_transcurridos==20:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Recuerde que en el estado de gestación uno es más propenso a contraer infecciones, enfermedades crónicas. Recuerde asimismo utilizar mascarilla es estos tiempó de COVID-19")
       elif días_transcurridos==22:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"La mayoría de las personas saben que fumar causa cáncer y otros problemas de salud graves. Y fumar durante el embarazo también puede causar serios problemas. Su bebé podría nacer mucho antes de lo debido, tener un defecto de nacimiento o morir a causa del síndrome de muerte súbita del lactante (SIDS, por sus siglas en inglés). Incluso estar cerca del humo de un cigarrillo puede causar problemas de salud en usted y su bebé.")
       elif días_transcurridos==23:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Sin recomendación diaria")
       elif días_transcurridos==24:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Recuerde que asistir a sus controles médicos establecidos son de suma importancia ya que puede resolver dudas de su embarazo y además porque se lleva un control del feto.")
       elif días_transcurridos==25:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Es común tener cólicos durante el embarazo, pero ¿es molestoso verdad? Por eso se recomienda cuidar tu postura , evitar cambios bruscos, masajear con la punta de los  en la zona de dolor y calentar la zona de dolor con una bolsa con agua tibia.")
       elif días_transcurridos==26:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"¡Recuerda que en este proceso de embarazo llevas un ser en tu vientre , si contraes una enfermedad de transmisión sexual, este podrá contraerla también , cuidalo y cuidate!")
       elif días_transcurridos==27:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"¡Calma! Estos dolores son normales , pero lo recomendable es relajarse y estar en una posición que le transmita tranquilidad , así mismo se recomienda evitar alimentos que generan gases.")
       elif días_transcurridos==29:
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Si usted tiene la presión arterial muy alta, esto puede hacer que la placenta se desprenda del útero demasiado pronto, por ello se le recomienda asistir de inmediato donde un médico .Por otro lado, si usted tiene la presión arterial muy baja debe sentarse, respirar profundo e inclinar el cuerpo hacia adelante, tratando de llegar la cabeza a las rodillas durante algunos minutos; si esto no ayuda a su mejora se le recomienda acudir a donde un  médico de inmediato.")
       else :
           print(f"Recomendación diaria {días_transcurridos}")
           print (f"Si hasta el momento ha sentido contracciones que no son dolorosas pero sí muy frecuentes, más aún durante el sexto mes de embarazo no se alarme, es parte del flujo normal de un embarazo. Por otro lado, si siente contracciones que provocan mucho dolor, no dude en asistir al doctor porque este tipo de contracciones son conocidas como patológicas y pueden desencadenar un parto prematuro espontáneo. ")

print(R2(días_transcurridos))