# Definicion de la clase vehiculo de la cual van a heredar todos los vehiculos
class Vehiculo:
    def __init__(self, marca, modelo, capacidad_combustible):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_combustible = capacidad_combustible
        
    def __str__(self):
        return "Marca: " + self.marca + " Modelo: " + self.modelo
    
    def moverse(self):
        print("El vehículo de la marca", self.marca, "modelo", self.modelo, "está en movimiento")
        
# Esta clase solamente le da funcionalidades a los objetos de tipo embarcación
class MovimientosEmbarcacion:
    def virar_a_estribor(self):
        print("Esta embarcación esta virando a estribor!")
    def virar_a_babor(self):
        print("Esta embarcación esta virando a babor")

# ----------------- Definición de Vehiculos -----------------------

class Auto(Vehiculo):
    cantidad_ruedas = 4
    def __init__(self, marca, modelo, comb, color, nro_puertas):
        super().__init__(marca, modelo, comb)
        self.color = color
        self.puertas = nro_puertas
    
    def tocar_bocina(self):
        print("Este auto esta haciendo piiiii piiiiiiii!!")
        
class Lancha(Vehiculo, MovimientosEmbarcacion):
    def __init__(self, marca, modelo, comb, asientos, calado):
        super().__init__(marca, modelo, comb)
        self.nro_asientos = asientos
        self.calado = calado
        
#-------------------------------------------------------------------
# Creación de instancias de vehiculos
automovil_1 = Auto("Toyota", "Corola", 50, "Verde Musgo", 3)
automovil_2 = Auto("Audi", "A4", 50, "Azul espacial", 4)
lancha_1 = Lancha("Yamaha", "125", 100, 5, 1.5)

# Realizando pruebas sobre los vehiculos creados
print(automovil_1)
print(lancha_1)

automovil_2.moverse()
lancha_1.virar_a_babor()
lancha_1.virar_a_estribor()
automovil_1.tocar_bocina()