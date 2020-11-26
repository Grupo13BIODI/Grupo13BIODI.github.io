fecha=int(input("coloque la fecha:"))
print(f"{fecha}")
if fecha==1:
    i=1
    while i==1:
        print("día 1 del seguimiento")
        print("¿Ha sentido cólicos en el útero?")
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
        print("¿Mantiene relaciones sexuales sin protección?")
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
        print("¿Ha sentido dolores constantes en el útero?")
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
        print("¿Ha sentido estrés corporal el día de hoy?")
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
        print("¿Ha sentido contracciones?")
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
        print("¿Ha tenido dificultad para respirar?")
        f=int(input("0/si 1/no"))
        if f==0 or f==1:
            print(f"f")
            si=0
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
if fecha==7:
    so=1
    while so==1:
        print("día 7 del seguimiento")
        print("¿Ha tenido una presión arterial alta o baja?")
        g=int(input("0/si 1/no"))
        if g==0 or g==1:
            print(f"g")
            so=0
            x=1
            while x==1:
                print("¿Ha sentido con frecuencia endurecimiento del abdomen?")
                q=int(input("0/si 1/no"))
                if q==0 or q==1:
                    print(f"q")
                    x=0
                else:
                    print("El valor introducido no está reconocido, porfavor volver a introducir el dato")
        else:
            print("El valor introducido no está reconocido, porfavor volver a introducir el dato")