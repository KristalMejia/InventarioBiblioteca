print("Dhayana Kristal")
print("Mat. 2021-0046")
print("==== Proyeco Final Estrcutura de Datos ====")

from datetime import datetime
import uuid

class Libro: 
    # Clase para representar un libro con su información

    def __init__(self, codigo, titulo, apellido_autor, nombre_autor, etiqueta, editora, fecha_publicacion):
        self.codigo = codigo
        self.titulo = titulo
        self.apellido_autor = apellido_autor
        self.nombre_autor = nombre_autor
        self.etiqueta = etiqueta 
        self.editora = editora
        self.fecha_publicacion = fecha_publicacion
        self.estado = "en sala" # Agregamos un atributo para el estado del libro

        """
        Constructor de la clase Libro.
        
        Parámetros:
        - código (str): Código único del libro.
        - titulo (str): Título del libro 
        - apellido_autor (str): Apellido del autor del Libro.
        - nombre_autor (str): Nombre del autor de Libro.
        - etiqueta (str): Género del libro
        - Editora (str): Editora del libro.
        - fecha_publicacion (datetime): Fecha de publicacion del libro.
        """

# Clase que representa una biblioteca y maneja la lista de Libros.
class Biblioteca:
    def __init__(self):
        
        #constructor de la clase Biblioteca
        #Inicializa la lista de libros.
        self.libros = []

def agrega_libros(self, libro):

    # Se debe de agregar un libro a la lista de la biblioteca 
    """
    - Libro (Libro): Objeto de la clase Libro a agregar
    """
    self.libros.append(libro)
    print("Libro agregado con éxito.")

def mostrar_libro(self):
    
    # Se debe de mostrar la lista de libros almacenados en la biblioteca

    if not self.libros:
        print("No hay libros en la biblioteca.")
    else:
        print("Lista de Libros:")
        for libro in self.libros:
            print(f"Código: {libro.codigo}")
            print(f"Título: {libro.titulo}")
            print(f"Autor: {libro.apellido_autor}, {libro.nombre_autor}")
            print(f"Etiqueta: {libro.etiqueta}")
            print(f"Editora: {libro.editora}")
            print(f"Fecha: {libro.fecha_publicacion}")
            print("=" *40)

def  eliminar_libro(self, codigo_libro):
    for libro in self.libro:
        if libro.codigo == codigo_libro:
            self.libro.remove(libro)
            print(f"Libro con código {codigo_libro} eliminado de la biblioteca.")
            return 
        print(f"No se encontró ningún lirbo con código {codigo_libro}.")
        

class Autoservicio:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

        def prestamo(self, estudiante, codigo_libro):
            for libro in self.biblioteca.libro:
                if libro.codigo == codigo_libro and libro.estado == "en sala":
                    libro.estado = "prestado"
                    print(f"Préstamo del libro '{libro.titulo}' realizado por el estudiante {estudiante.id_estudiante}.")

class Estudiante:
    def __init__(self, nombre, apellido):
        self.id_estudiante = str(uuid.uuid4())[:8] # Genera un ID único automáticamente
        self.nombre = nombre
        self.apellido = apellido

#Esto sirve para elegir el nombre del estudiante
nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido: ")
estudiante = Estudiante(nombre, apellido)
print(f"Estudiante creado: ID={estudiante.id_estudiante}, Nombre={estudiante.nombre}, Apellido={estudiante.apellido}")

class Autoservicio:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

        def prestamo(self, estudiante, codigo_libro):
            for libro in self.biblioteca.libro:
                if libro.codigo == codigo_libro and libro.estado == "en sala":
                    libro.estado = "prestado"
                    print(f"Préstamo del libro '{libro.titulo}' realizado por el estudiante {estudiante.id_estudiante}.")

        def renovacion(self, estudiante, codigo_libro):
            for libro in self.biblioteca.libro:
                if libro.codigo == codigo_libro and libro.estado == "prestamo":
                    print(f"Renovación del libro ' {libro.titulo} 'realizada por el estudiante {estudiante.id_estudiante}.")

        def devolucion(self, estudiante, codigo_libro):
            for libro in self.biblioteca.libros: 
                if libro.codigo == codigo_libro and libro.estado == "Prestado":
                    libro.estado = "en sala"
                    print(f"Devolución del libro ' {libro.titulo}' realizada por el estudiante {estudiante.id_estudiante}.")

class Controlador:
    def __init__(self):
        self.libros_salida_irregular = set()

        def reportar_salida_irregular(self, codigo_libro):
            self.libro_salida_irregular.add(codigo_libro)
            print(f"Alerta: El libro con código {codigo_libro} ha salido irregularmente de la biblioteca")

class AntenaRFID:
    def __init__(self, controlado):
        self.controlador = Controlador


    def detectar_salida_irregular(self, codigo_libro):
        self.controlador.reportar_salida_irregular(codigo_libro)

def main():
    biblioteca = Biblioteca()
    autoservicio = Autoservicio(biblioteca)
    controlador = Controlador()
    antena_rfid = AntenaRFID(controlador)

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Prestamo")
        print("4. Renovacion")
        print("5. Devolucion")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del libro: ")
            titulo = input("Título del libro: ")
            apellido_autor = input("Apellido del autor: ")
            nombre_autor = input("Nombre del autor: ")
            area_conocimiento = input("Área de Conocimiento: ")
            publicador = input("Publicador: ")
            tramo_asignado = input("Tramo Asignado: ")
            fecha_publicacion = input("Fecha de publicación (YYYY-MM-DD): ")

            try:
                fecha_publicacion = datetime.strptime(fecha_publicacion, "%Y-%m-%d")
                libro = Libro(codigo, titulo, apellido_autor, nombre_autor, area_conocimiento, publicador, tramo_asignado, fecha_publicacion)
                biblioteca.agregar_libro(libro)
            except ValueError:
                print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")

        elif opcion == "2":
            biblioteca.mostrar_libros()

        elif opcion == "3":
            id_estudiante = input("ID del estudiante: ")
            codigo_libro = input("Código del libro: ")
            estudiante = Estudiante(id_estudiante)
            autoservicio.prestamo(estudiante, codigo_libro)

        elif opcion == "4":
            id_estudiante = input("ID del estudiante: ")
            codigo_libro = input("Código del libro: ")
            estudiante = Estudiante(id_estudiante)
            autoservicio.renovacion(estudiante, codigo_libro)

        elif opcion == "5":
            id_estudiante = input("ID del estudiante: ")
            codigo_libro = input("Código del libro: ")
            estudiante = Estudiante(id_estudiante)
            autoservicio.devolucion(estudiante, codigo_libro)

        elif opcion == "6":
            codigo_libro = input("Ingrese el código del libro a eliminar: ")
            biblioteca.eliminar_libro(codigo_libro)

            print("¡Hasta luego!")
            break
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
