# ==============================
# SISTEMA DE GESTIÓN DE ESTUDIANTES
# ==============================

def registrar_estudiante():

    nombre = input("Ingrese el nombre del estudiante: ")

    while True:
        edad = int(input("Ingrese la edad: "))
        if edad > 0:
            break
        else:
            print("edad incorrecta.")

    while True:
        nota1 = float(input("Ingrese nota 1: "))
        if 0 <= nota1 <= 5:
            break
        else:
            print("La nota debe estar entre 0 y 5")

    while True:
        nota2 = float(input("Ingrese nota 2: "))
        if 0 <= nota2 <= 5:
            break
        else:
            print("La nota debe estar entre 0 y 5")

    while True:
        nota3 = float(input("Ingrese nota 3: "))
        if 0 <= nota3 <= 5:
            break
        else:
            print("La nota debe estar entre 0 y 5")

    return nombre, edad, nota1, nota2, nota3


def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio


def evaluar_estado(promedio):

    if promedio >= 4.0:
        return "Aprobado"

    elif promedio >= 3.0:
        return "En recuperación"

    else:
        return "Reprobado"


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

total_estudiantes = 0
suma_promedios = 0

while True:

    print("===== SISTEMA DE ESTUDIANTES =====")
    print("1. Registrar estudiante")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre, edad, n1, n2, n3 = registrar_estudiante()

        promedio = calcular_promedio(n1, n2, n3)

        estado = evaluar_estado(promedio)

        print("Promedio del estudiante:", round(promedio, 2))
        print("Estado académico:", estado)

        total_estudiantes += 1
        suma_promedios += promedio

    elif opcion == "2":
        break

    else:
        print("Opción inválida")


# ==============================
# RESUMEN FINAL
# ==============================

print("===== RESUMEN FINAL =====")

print("Total de estudiantes registrados:", total_estudiantes)

if total_estudiantes > 0:
    promedio_general = suma_promedios / total_estudiantes
    print("Promedio general del grupo:", round(promedio_general, 2))
else:
    print("No se registraron estudiantes.")