from random import randint
num1 = 0 
num2 = 0
flag = True

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
numero_secreto = randint(num1,num2)

intento1 = int(input(f"Ingrese su primer intento: "))
if intento1 == numero_secreto:
    print("Felicidades, ganó")
    flag = False
elif intento1 < numero_secreto:
    print("El numero es mayor")
elif intento1 > numero_secreto:
    print("El numero es menor")
    
if flag:
    diferencia1 = abs(numero_secreto-intento1)

if flag:
    intento2 = int(input(f"Ingrese su segundo intento: "))
    if intento2 == numero_secreto:
        print("Felicidades, ganó")
    elif intento2 < numero_secreto:
        print("El numero es mayor")
    elif intento2 > numero_secreto:
        print("El numero es menor")
        
if flag:        
    diferencia2 = abs(numero_secreto-intento2)
    if diferencia1 < diferencia2:
        print(f"El número secreto está mas cerca de {intento1} que de {intento2}")
    if diferencia1 > diferencia2: 
        print (f"El numero secreto está mas cerca de {intento2} que de {intento1}")

if flag:
    intento3 = int(input(f"Ingrese su tercer y último intento: "))
    if intento3 == numero_secreto:
        print("Felicidades, ganó")
    else:
        print(f"El numero era {numero_secreto}")
        print("No has podido adivinar el número esta vez, intentalo nuevamente")