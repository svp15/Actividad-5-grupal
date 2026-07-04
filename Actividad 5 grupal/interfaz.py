import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from estudiante import Estudiante
from gestor import Gestor


class Interfaz:

    def __init__(self):

        self.gestor = Gestor()

        self.ventana = tk.Tk()
        self.ventana.title("CRUD de Estudiantes")
        self.ventana.geometry("850x500")

        # Etiquetas
        tk.Label(self.ventana, text="Código").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.ventana, text="Nombre").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.ventana, text="Carrera").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.ventana, text="Edad").grid(row=3, column=0, padx=10, pady=10)

        # Entradas
        self.codigo = tk.Entry(self.ventana)
        self.nombre = tk.Entry(self.ventana)
        self.carrera = tk.Entry(self.ventana)
        self.edad = tk.Entry(self.ventana)

        self.codigo.grid(row=0, column=1)
        self.nombre.grid(row=1, column=1)
        self.carrera.grid(row=2, column=1)
        self.edad.grid(row=3, column=1)

        # Botones
        tk.Button(self.ventana, text="Crear", width=12, command=self.crear).grid(row=0, column=2, padx=10)

        tk.Button(self.ventana, text="Buscar", width=12, command=self.buscar).grid(row=1, column=2, padx=10)

        tk.Button(self.ventana, text="Actualizar", width=12, command=self.actualizar).grid(row=2, column=2, padx=10)

        tk.Button(self.ventana, text="Eliminar", width=12, command=self.eliminar).grid(row=3, column=2, padx=10)

        tk.Button(self.ventana, text="Mostrar Todos", width=20, command=self.mostrar).grid(row=4, column=0, columnspan=3, pady=10)

        # Tabla
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=("codigo", "nombre", "carrera", "edad"),
            show="headings"
        )

        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("carrera", text="Carrera")
        self.tabla.heading("edad", text="Edad")

        self.tabla.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def iniciar(self):
        self.ventana.mainloop()

    # Las funciones se agregarán después
    def crear(self):

        if self.codigo.get() == "" or self.nombre.get() == "" or self.carrera.get() == "" or self.edad.get() == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        estudiante = Estudiante(
            self.codigo.get(),
            self.nombre.get(),
            self.carrera.get(),
            self.edad.get()
        )

        if self.gestor.crear(estudiante):
            messagebox.showinfo("Éxito", "Estudiante creado correctamente")
            self.mostrar()
        else:
            messagebox.showerror("Error", "El código ya existe")

    def buscar(self):

        estudiante = self.gestor.buscar(self.codigo.get())

        if estudiante:
            self.nombre.delete(0, tk.END)
            self.carrera.delete(0, tk.END)
            self.edad.delete(0, tk.END)

            self.nombre.insert(0, estudiante.nombre)
            self.carrera.insert(0, estudiante.carrera)
            self.edad.insert(0, estudiante.edad)
        else:
            messagebox.showerror("Error", "No se encontró el estudiante")

    def actualizar(self):

        estudiante = Estudiante(
            self.codigo.get(),
            self.nombre.get(),
            self.carrera.get(),
            self.edad.get()
        )

        if self.gestor.actualizar(self.codigo.get(), estudiante):
            messagebox.showinfo("Éxito", "Actualizado correctamente")
            self.mostrar()
        else:
            messagebox.showerror("Error", "No existe el estudiante")

    def eliminar(self):

        if self.gestor.eliminar(self.codigo.get()):
            messagebox.showinfo("Éxito", "Eliminado correctamente")
            self.mostrar()
        else:
            messagebox.showerror("Error", "No se encontró el estudiante")

    def mostrar(self):

        # limpiar tabla
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # cargar datos
        for estudiante in self.gestor.leer():
            self.tabla.insert("", "end", values=(
                estudiante.codigo,
                estudiante.nombre,
                estudiante.carrera,
                estudiante.edad
            ))