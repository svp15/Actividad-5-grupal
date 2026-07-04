import os
from estudiante import Estudiante


class Gestor:

    def __init__(self):
        self.archivo = "estudiantes.txt"

    def crear(self, estudiante):

        if self.buscar(estudiante.codigo):
            return False

        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(str(estudiante) + "\n")

        return True

    def leer(self):

        estudiantes = []

        if not os.path.exists(self.archivo):
            return estudiantes

        with open(self.archivo, "r", encoding="utf-8") as f:

            for linea in f:
                linea = linea.strip()

                if linea:
                    datos = linea.split(",")

                    estudiantes.append(
                        Estudiante(datos[0], datos[1], datos[2], datos[3])
                    )

        return estudiantes

    def buscar(self, codigo):

        for estudiante in self.leer():
            if estudiante.codigo == codigo:
                return estudiante

        return None

    def actualizar(self, codigo, nuevo):

        estudiantes = self.leer()
        actualizado = False

        with open(self.archivo, "w", encoding="utf-8") as f:

            for e in estudiantes:

                if e.codigo == codigo:
                    f.write(str(nuevo) + "\n")
                    actualizado = True
                else:
                    f.write(str(e) + "\n")

        return actualizado

    def eliminar(self, codigo):

        estudiantes = self.leer()
        eliminado = False

        with open(self.archivo, "w", encoding="utf-8") as f:

            for e in estudiantes:

                if e.codigo != codigo:
                    f.write(str(e) + "\n")
                else:
                    eliminado = True

        return eliminado