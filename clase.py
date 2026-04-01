class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def ladrar(self):
        return "¡GUAU!"
    def rascarse(self):
        print("¡me estoy rascando!")

perro1 = Perro("Trosky,",5)
perrito = Perro("firulis",3)
print(perro1.nombre, perro1.edad)
print(perrito.nombre,perrito.edad)
print(perro1.ladrar())
print(perrito.ladrar())
perro1.rascarse()
perrito.rascarse()