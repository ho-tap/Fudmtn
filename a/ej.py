from funciones import menu
from funciones import calcular
opcion = 0


menu()


while opcion !=6:
    opcion = int(input("Ingrese su opcion: "))
    if opcion < 6 and opcion > 0:
        num1 = int(input("Escoja el primer numero: "))
        num2 = int(input("Escoja el segundo numero: "))
        resultado = calcular(num1,num2,opcion)
        print (f"El resultado de su operacion es: {resultado}")
    elif opcion == 6:
        print ("Chao")
    else:
        print ("Opcion incorrecta")
        