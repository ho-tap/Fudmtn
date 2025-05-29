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
    
    import calculadora
    
    num1 = int (input("Escoja el primer numero"))
    num2 = int (input("Escoja el segundo numero"))
    
 
    
    if opcion == 5:
        print ("Gracias por usar nuestra calculadora, tenga un buen día")

    else:
        print ("Opcion ingresada incorrecta, inténtelo nuevamente")
    
           

