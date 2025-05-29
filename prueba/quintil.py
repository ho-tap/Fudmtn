subsidio_Arriendo = 0
quintil = 0
edad = 0

quintil = int(input("Cual es su quintil? (1-5): "))

empleo = int(input("Usted esta empleado? (1= Si 2 = No): "))

edad = int(input("Ingrese su edad: "))

if edad > 60:
    subsidio_Arriendo +=30000

if quintil == 1 or quintil == 2:
    subsidio_Arriendo += 50000
    if empleo == 2:
        subsidio_Arriendo += 300000
    elif empleo == 1:
        subsidio_Arriendo += 250000
        
if quintil == 3:
    if empleo == 2:
        subsidio_Arriendo += 200000
    elif empleo == 1:
        subsidio_Arriendo += 150000

print(f"Su subsidio arriendo es de {subsidio_Arriendo}")