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