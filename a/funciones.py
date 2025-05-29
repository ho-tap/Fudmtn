def menu():
    print("Calculadora")

    print("1. Sumar")
    print("2. Restar")    
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Salir")
    
def calcular(num1,num2,opcion):
    if opcion == 1:
        return num1 + num2
    if opcion == 2:
        return num1 - num2
    if opcion == 3:
        return num1 * num2
    if opcion == 4:
        return num1 / num2
    if opcion == 5:
        return num1 ** num2