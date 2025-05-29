def calcular(opcion, resultado, num):
        if opcion == 1:
            while num != 0:
                num = int (input("Escoja un numero para sumar. 0 para salir "))
                resultado = resultado + num
                print (f"Su suma va en {resultado}")
            print (f"El resultado de su suma es: {resultado}")
        elif opcion == 2:
            resultado = int(input("Escoja el numero inicial de su resta: "))
            while num != 0:
                num = int (input("Escoja un numero para restarle. 0 para salir "))
                resultado = resultado - num
            print (input(f"El resultado de su resta es: {resultado}"))