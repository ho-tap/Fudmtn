from funciones import menu
from funciones import calcular

opcion = 0 
resultado = 0
num1 = 0
num2 = 0

menu()

while opcion != 6:
    opcion = int(input("Escoja su opcion: "))
    num1 = int (input("Escoja el primer numero: "))
    num2 = int (input("Escoja el segundo numero: "))
    resultado = calcular(num1,num2,opcion)
    print (f"Su resultado es {resultado}")  
    if opcion == 6:
        print ("Buenas noches")