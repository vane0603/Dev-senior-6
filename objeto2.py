"""
Crear una clase Libro con:

🔹 Atributos (privados)
título
autor
ISBN
precio
🔹 Requisitos
Constructor parametrizado
Getters y setters para todos los atributos
Método que muestre la información del libro
Crear mínimo 3 libros
Mostrar la información de cada uno
"""
class Libro:
    def __init__(self, titulo, autor, isbn, precio):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__precio = precio

# Getters
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_isbn(self):
        return self.__isbn

    def get_precio(self):
        return self.__precio
    
# Setters
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_isbn(self, isbn):
        self.__isbn = isbn
    
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            print("El precio debe ser mayor que 0")

# Método para mostrar información
    def mostrar_info(self):
        print("Título:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("ISBN:", self.get_isbn())
        print("Precio:", self.get_precio())
        print("------------------------")

# Clase principal
def main():
    libro1 = Libro("Python Básico", "Juan Pérez", "12345", 50000)
    libro2 = Libro("IA para todos", "Ana Gómez", "67890", 75000)
    libro3 = Libro("POO en Python", "Carlos Ruiz", "11223", 60000)

    libro1.mostrar_info()
    libro2.mostrar_info()
    libro3.mostrar_info()

    # Ejemplo de uso de setter
    libro1.set_precio(55000)
    print("Nuevo precio del libro 1:", libro1.get_precio())
    libro1.mostrar_info()

if __name__ == "__main__":    main()

class Perro:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    def get_edad(self):
        return self.__edad

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser mayor que 0")

    # Método para mostrar información
    def mostrar_info(self):
        print("Nombre:", self.get_nombre())
        print("Raza:", self.get_raza())
        print("Edad:", self.get_edad())
        print("------------------------")


# Clase principal
def main():
    perro1 = Perro("Max", "Labrador", 5)
    perro2 = Perro("Bella", "Golden Retriever", 3)
    perro3 = Perro("Rocky", "Bulldog", 4)

    perro1.mostrar_info()
    perro2.mostrar_info()
    perro3.mostrar_info()

    # Ejemplo de uso de setter
    perro1.set_edad(6)
    print("Nueva edad del perro 1:", perro1.get_edad())
    perro1.mostrar_info()

perro4 = Perro("Luna", "Poodle", 2)
perro4.mostrar_info()
main()
