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
total= 0
totalHambuerguesas = 0
cantHamburguesas = 0
totalPizza = 0
cantPizzas = 0
totalEnsalada = 0
cantEnsaladas = 0
totalSalchipapa = 0
cantSalchipapas = 0
totalPerrocaliente = 0
cantPerroscalientes = 0
opcion = 0
while opcion != 6:
    opcion = int(input ("ingrese una opción del menú:"))
    if opcion == 1:
        print("Has elegido hamburguesa")
        total += 20000
        totalHambuerguesas += 20000
        cantHamburguesas += 1
    elif opcion == 2:
        print("Has elegido pizza")   
        total += 15000 
        totalPizza += 15000
        cantPizzas +=1
    elif opcion == 3:
        print("Has elegido Ensalada")
        total += 4500 
        totalEnsalada += 4500
        cantEnsaladas +=1
    elif opcion == 4:
        print("Has elegido Salchipapa") 
        total += 8000   
        totalSalchipapa += 8000
        cantSalchipapas += 1
    elif opcion == 5:
        print("Has elegido perro caliente")
        total +=12000 
        totalPerrocaliente += 12000 
        cantPerroscalientes += 1
    elif opcion == 6:
        print ("el valor de tu cuenta es:", total)
        print ("total hamburguesas:", totalHambuerguesas,"cantidad:",cantHamburguesas)
        print ("total pizzas:", totalPizza,"cantidad:",cantPizzas)
        print ("total ensaladas:", totalEnsalada,"cantidad:",cantEnsaladas)
        print ("total salchipapas:", totalSalchipapa,"cantidad:",cantSalchipapas)
        print ("total perros calientes:", totalPerrocaliente, "cantidad:",cantPerroscalientes)   
        break 
    else:
        print("Opción no valida, por favor elige una opción del menú")                           
    print (menu)
