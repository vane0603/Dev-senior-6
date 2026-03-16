menu  = """
restaurante el buen sabor
1. Hamburguesa - $20.000
2. Pizza - $15.000
3. Ensalada - $4.500
4. Salchipapa - $8.000
5. Perro caliente - $12.000
6. Salir
""" 
print (menu)
opcion = 0
while opcion != 6:
    opcion = int(input ("ingrese una opción del menú:"))
    if opcion == 1:
        print("Has elegido hamburguesa")
    elif opcion == 2:
        print("Has elegido pizza")    
    elif opcion == 3:
        print("Has elegido Ensalada") 
    elif opcion == 4:
        print("Has elegido Salchipapa")    
    elif opcion == 5:
        print("Has elegido perro caliente")    
    elif opcion == 6:
        print("Gracias por visitar el restaurante el buen sabor. ¡Hasta luego!")   
        break 
    else:
        print("Opción no valida, por favor elige una opción del menú")                           
    print (menu)
