class Estudiante:
    def __init__(self, codigo, nombre, carrera, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.carrera},{self.edad}"