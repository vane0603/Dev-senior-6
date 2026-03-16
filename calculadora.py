operacion = """
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Division entera
6. Potencia
7. Modulo(residuo de la division)
8. Salir
"""
n1 =  int(input ("ingrese el primer nuumero:"))
n2 = int(input("ingrese el segundo numero:"))

opcion= 0
while opcion != 8:
    opcion = int(input ("elija una opcion:"))
    if opcion == 1:
        print("Resultado:", n1 + n2)

    elif opcion == 2:
        print("Resultado:", n1 - n2)

    elif opcion == 3:
        print("Resultado:", n1 * n2)

    elif opcion == 4:
        print("Resultado:", n1 / n2)
    elif opcion == 5:
        print("Resultado:", n1 // n2)

    elif opcion == 6:
        print("Resultado:", n1 ** n2)
    elif opcion == 7:
        print("Resultado:", n1 % n2)

    elif opcion == 8:
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida")
      

