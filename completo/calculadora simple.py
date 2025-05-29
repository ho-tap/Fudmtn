opcion = 0
num1 = 0 
num2 = 0
resultado = 0



while opcion != 5:
    opcion = int(input("Ingrese una opción: "))
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicación")
    print ("4. División")
    print ("5. Salir")
    if opcion == 1:
       num1 = int (input("Ingrese el primer número: "))
       num2 = int (input("ingrese el segundo número: "))
       resultado = num1 + num2
    
       print (f"Su resultado es: {resultado}")
           
    elif opcion == 2:
        num1 = int (input("Ingrese el primer número: "))
        num2 = int (input("ingrese el segundo número: "))
        resultado = num1 - num2
    
        print (f"Su resultado es: {resultado}")

    elif opcion == 3:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int (input("ingrese el segundo número: "))
        resultado = num1 * num2
    
        print (f"Su resultado es: {resultado}")

    elif opcion == 4:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int (input("ingrese el segundo número: "))
        resultado = num1 / num2
    
        print (f"Su resultado es: {resultado}")

    elif opcion == 5:
        print ("Gracias por usar nuestra calculadora, tenga un buen día")

    else:
        print ("Opcion ingresada incorrecta, inténtelo nuevamente")
    
           

