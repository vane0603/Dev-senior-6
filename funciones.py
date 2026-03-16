"""
#no recibe nada y no devuelve nada
def suma():
    a = int(input("ingrese el primer numero:"))
    b = int(input("ingrese el segundo numero:"))
    resultado = a + b
    print(f"la suma{a} y {b} es: {resultado}")

#recibe parametros pero no devuelve nada
def suma2 (a,b):
    resultado = a + b
    print (f"la suma de {a} y {b} es: {resultado}")

print ("hola mundo")
n1 =  int(input ("ingrese el primer nuumero:"))
n2 = int(input("ingrese el segundo numero:"))
suma2(n1,n2)

#no recibe parametro pero devuelve valor
def suma3():
    a = int(input("ingrese el primer numero:"))
    b = int(input("ingrese el primer numero:"))
    resultado = a + b
    return resultado
print(suma3())"""

#recibe parametros y devuelve valor
def suma4(a,b):
    resultado = a + b
    return resultado
n1 =  int(input ("ingrese el primer nuumero:"))
n2 = int(input("ingrese el segundo numero:"))
print(suma4(n1,n2))