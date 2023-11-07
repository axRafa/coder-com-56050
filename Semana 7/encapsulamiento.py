class Alumno:
    def __init__(self, nro_doc, nombre, apellido, edad):
        self.__documento = nro_doc
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
        
    def get_documento(self):
        print("El numero de documento es:", self.__documento)
        return self.__documento
    
    def set_documento(self, nuevo_nro_documento):
        self.__documento = nuevo_nro_documento            
    
alumno_1 = Alumno(456859485, "Luciana", "Fernandez", 20)

print(alumno_1.edad)
print(alumno_1.nombre)
nro_documento = alumno_1.get_documento()
print(nro_documento)

alumno_1.set_documento(11111111111)
alumno_1.get_documento()