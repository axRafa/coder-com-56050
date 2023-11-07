# Microdesafío: clase Automovil
class Auto():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def __str__(self):
        return "Marca: " + self.marca + ", Modelo: " + self.modelo

automovil_1 = Auto("Toyota", "Hilux")
print(automovil_1)

# Ejemplo de clase para mostrar algunas cosas más que podemos hacer con programación orientada a objetos
class Alumno:
    def __init__(self, nro_doc, nombre, apellido, edad):
        self.doc = nro_doc
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self):
        return self.nombre + " " + self.apellido
    
    def estudiar(self):
        print("El alumno", self.nombre, "está estudiando.")
    
    def crecer(self):
        self.edad += 1
        print("El alumno:", self.nombre, "ahora tiene", self.edad, "años.")

alumno_1 = Alumno(456859485, "Luciana", "Fernandez", 20)
alumno_2 = Alumno(2341234, "nombre", "apellido generico", 67)
print(alumno_1)
alumno_1.estudiar()
print("Edad:", alumno_1.edad)
alumno_1.crecer()
alumno_1.crecer()
alumno_1.crecer()

lista = list(26, 6, 11)