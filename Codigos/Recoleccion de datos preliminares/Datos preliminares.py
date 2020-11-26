#DATOS PRELIMINARES
#NOMBRE
a = str(input("Ingrese su nombre y apellido "))
print(f"Hola {a}! Gracias por formar parte de Baby Alert :) ")
#EDAD
i=1
while i==1:
 b = int(input("Ingrese su edad "))
 if 14<=b<=55:
    print(f"{b} años")
    i=0
    #TALLA
    j=1
    while j==1:
     c = float(input("Coloque su altura en metros (utilice punto, no coma) "))
     if 1.30<=c<=2.10:
        print(f"{c} m")
        j=0
        #PESO
        k=1
        while k==1:
         d = float(input("Coloque su peso en Kg "))
         if (((c*100)-107)-10)<=d<=(((c*100)-107)+10):
            print(f"{d} Kg")
            k=0
            #MES DE GESTACIÓN
            g=0
            while g==0:
             e = int(input("Ingrese su mes de gestación "))
             if 0<=e<=9:
                print(f"{e} mes")
                g=1
                #ENFERMEDAD
                print("Escoja una efermedad")
                f = int(input("1/Diabetes  2/Asma  3/Anomalías utero-cervicales  4/Cardiopatías  5/Anemia  "))
             elif 9<e<11:
                print("Su bebé está tardando mucho en nacer, recomendamos ver a un especialista")
                g=1
             else:
                print("Mes inválido")
                g=0
         elif d<(((c*100)-107)-10):
             print("Su peso es muy bajo con respecto a su estatura, recomendamos ver a un especialista")
             k=0
         else:
            print("Su peso es muy elevado según su estatura, recomendamos ver a un especialista")
            k=0
     elif c<1.30:
        print("Su talla es muy pequeña a comparación del promedio, recomendamos ver a un especialista")
        j=0
     else:
        print("Su talla es muy alta a compración del promedio, recomendamos ver a un especialista")
        j=0
 elif b>55:
    print("Lo sentimos, su edad es muy riesgosa para un embarazo. Le recomendamos ver un especialista.")
    i=0
 else:
    print("Edad inválida ")
    i=1




