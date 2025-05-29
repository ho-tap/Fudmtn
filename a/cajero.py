from funcionesCajero import menu
saldo = 100000
saldoIngresado = 0
saldoRetirado = 0
opcion = 0
usando = True

menu()

while opcion != 4:
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        print(f"Tu saldo actual es: ${saldo}")
        print ("Desea realizar otra opcion?")
        opcion = int(input("1. Si / 2. No"))
        if opcion == 1:
            continue
        if opcion == 2:
            print("Gracias por usar nuestro cajero")
            break
    elif opcion == 2:
        saldoIngresado = int(input("Ingrese el monto que desea ingresar: "))
        saldo += saldoIngresado
        print(f"Saldo ingresado exitosamente. Su saldo actual es: {saldo}")
        print ("Desea realizar otra opcion?")
        opcion = int(input("1. Si / 2. No"))
        if opcion == 1:
            continue
        if opcion == 2:
            print("Gracias por usar nuestro cajero")
            break
    elif opcion == 3:
        saldoRetirado = int(input("Ingrese el monto que desea retirar"))
        saldo = saldo - saldoRetirado
        print(f"Saldo retirado exitosamente. Su saldo actual es: {saldo}")
        print ("Desea realizar otra opcion?")
        opcion = int(input("1. Si / 2. No"))
        if opcion == 1:
            continue
        if opcion == 2:
            print("Gracias por usar nuestro cajero")
            break
    elif opcion == 4:
        print("Gracias por usar nuestro cajero")
        usando = False
    elif opcion == 5:
        menu()
    else: 
        print("Opción no válida. Por favor, seleccione una opción válida")