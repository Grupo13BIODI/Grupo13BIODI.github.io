fecha=int(input("coloque la fecha:"))
print(f"{fecha}")
if fecha==1:
    i=1
    while i==1:
        print("día 1 del seguimiento")
        print("¿Ha tenido un parto  de mellizos o trillizos?")
        a=int(input("0/si 1/no"))
        if a==0 or a==1:
            print(f"a")
            i=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==2:
    j=1
    while j==1:
        print("día 2 del seguimiento")
        print("¿Ha tenido un parto prematuro ( <36 semanas ) anteriormente?")
        b=int(input("0/si 1/no"))
        if b==0 or b==1:
            print(f"b")
            j=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==3:
    k=1
    while k==1:
        print("día 3 del seguimiento")
        print("¿Ha tenido alguna cirugía por la parte superior de la espalda(cervix)?")
        c=int(input("0/si 1/no"))
        if c==0 or c==1:
            print(f"c")
            k=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==4:
    h=1
    while h==1:
        print("día 4 del seguimiento")
        print("¿Tiene alguna malformación uterina?")
        d=int(input("0/si 1/no"))
        if d==0 or d==1:
            print(f"d")
            h=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==5:
    p=1
    while p==1:
        print("día 5 del seguimiento")
        print("¿Hoy ha fumado una o más de dos veces?")
        e=int(input("0/si 1/no"))
        if e==0 or e==1:
            print(f"e")
            p=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==6:
    si=1
    while si==1:
        print("día 6 del seguimiento")
        print("¿Ha tenido un parto en los últimos 6 meses?")
        f=int(input("0/si 1/no"))
        if f==0 or f==1:
            print(f"f")
            si=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==7:
        print("día 7 del seguimiento")
        g=float(input("Coloque su peso en kilogramos(utilice la coma)"))
        print(f"{g}")
        x=1
        while x==1:
                print("¿Ya sacó cita para su próxima consulta?")
                q=int(input("0/si 1/no"))
                if q==0 or q==1:
                    print(f"q")
                    x=0
                else:
                    print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")