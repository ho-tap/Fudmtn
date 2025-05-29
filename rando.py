from random import randint
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

numero_random = randint(num1,num2)
flag = True

intento1 = int(input(f"El numero es {numero_random}. Ingrese el primer intento: "))
if intento1 == numero_random:
    print("Felicitaciones, ha ganado en el primer intento")
    flag = False
elif numero_random < intento1:
    print ("El numero es menor")
else:
    print ("El numero es mayor")
    
if flag:
    intento2 = int(input("Ingrese el segundo intento: "))
    if intento2 == numero_random:
        print ("Felicidades ganaste en tu segundo intento")
        flag = False
    elif numero_random < intento2:
        print ("El numero es menor")
    else:
        print ("El numero es mayor")

if flag:
    intento3= int(input("Ingrese el tercer intento: "))
    if intento3 == numero_random:
        print ("Felicidades ganaste en tu tercer intento")
        flag = False
    elif numero_random < intento3:
        print ("El numero es menor")
    else:
        print ("El numero es mayor")

if flag:
    intento4 = int(input("Ingrese el cuarto intento: "))
    if intento4 == numero_random:
        print ("Felicidades ganaste en tu cuarto intento")
        flag = False
    elif numero_random < intento4:
        print ("El numero es menor")
    else:
        print ("El numero es mayor")

if flag:
    intento5 = int(input("Ingrese el quinto intento: "))
    if intento5 == numero_random:
        print ("Felicidades ganaste en tu quinto intento")
        flag = False
    else:
        print ("No has podido adivinar el número esta vez. Intentalo de nuevo")


