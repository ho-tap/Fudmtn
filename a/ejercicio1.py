opcion = 0
num = 1
resultado = 0
suma = 0



while opcion != 5:
    
    opcion = int(input("Ingrese una opción: "))
    
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicación")
    print ("4. División")
    print ("5. Salir")
    
    
    if opcion == 1:
        while num != 0:
            num = int (input("Escoja un numero para sumar. 0 para salir"))
            resultado = resultado + num
        print (f"El resultado de su suma es: {resultado}")
    elif opcion == 2:
        resultado = int(input("Escoja el numero inicial de su resta: "))
        while num != 0:
            num = int (input("Escoja un numero para restarle. 0 para salir"))
            resultado = resultado - num
        print (input(f"El resultado de su resta es: {resultado}"))
            
    