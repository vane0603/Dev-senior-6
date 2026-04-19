from abc import ABC, abstractmethod

# ------------------ PERSONA ------------------
class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    @abstractmethod
    def mostrar_rol(self):
        pass


class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"Veterinario ({self.especialidad})"

    def atender_mascota(self, mascota):
        print(f"{self.nombre} está atendiendo a {mascota.nombre}")


class Recepcionista(Persona):
    def mostrar_rol(self):
        return "Recepcionista"

    def registrar_cliente(self, cliente):
        print(f"Cliente {cliente.nombre} registrado")


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []

    def mostrar_rol(self):
        return "Cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_mascotas(self):
        for m in self.mascotas:
            print(m.nombre)


# ------------------ MASCOTA ------------------
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return f"{self.nombre} - {self.especie}"


# ------------------ TRATAMIENTO ------------------
class Tratamiento:
    def __init__(self, nombre, costo, duracion):
        self.nombre = nombre
        self.costo = costo
        self.duracion = duracion

    def mostrar_tratamiento(self):
        return f"{self.nombre} - ${self.costo}"


# ------------------ CONSULTA ------------------
class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []

    def crear_tratamiento(self, nombre, costo, duracion):
        t = Tratamiento(nombre, costo, duracion)
        self.tratamientos.append(t)

    def calcular_costo_consulta(self):
        return sum(t.costo for t in self.tratamientos)

    def mostrar_resumen(self):
        print(f"Mascota: {self.mascota.nombre}")
        print(f"Veterinario: {self.veterinario.nombre}")
        print("Tratamientos:")
        for t in self.tratamientos:
            print("-", t.mostrar_tratamiento())


# ------------------ METODO DE PAGO ------------------
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago en efectivo: ${monto}")


class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago con tarjeta: ${monto} + comisión")


class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Pago por transferencia: ${monto}")


# ------------------ FACTURA ------------------
class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * 0.19
        self.total = self.subtotal + self.impuesto

    def calcular_total(self):
        return self.total

    def pagar(self, metodo_pago):
        metodo_pago.procesar_pago(self.total)


# ------------------ PRUEBA ------------------
if __name__ == "__main__":

    # Crear cliente
    cliente = Cliente("Vanessa", "123", "300123456")

    # Crear mascotas
    m1 = Mascota("Max", "Perro", 3, 10)
    m2 = Mascota("Luna", "Gato", 2, 5)

    cliente.agregar_mascota(m1)
    cliente.agregar_mascota(m2)

    # Veterinario
    vet = Veterinario("Dr. Juan", "999", "Cirugía")

    # Consulta
    consulta = Consulta(m1, vet, "Dolor", "Infección")

    # Tratamientos
    consulta.crear_tratamiento("Antibiótico", 50000, 5)
    consulta.crear_tratamiento("Vitaminas", 30000, 3)

    consulta.mostrar_resumen()

    # Factura
    factura = Factura(consulta)
    print("Total:", factura.calcular_total())

    # Pago 1
    pago1 = PagoEfectivo()
    factura.pagar(pago1)

    # Pago 2 (polimorfismo)
    pago2 = PagoTarjeta()
    factura.pagar(pago2)