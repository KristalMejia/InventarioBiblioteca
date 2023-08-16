# InventarioBiblioteca
Proyecto Final de Estructura de Datos
Dhayana Kristal
Mat. 2021-0046

Por supuesto, aquí tienes una breve descripción del proyecto:

**Descripción del Proyecto: Sistema de Gestión de Biblioteca**

El Sistema de Gestión de Biblioteca es una aplicación de consola desarrollada en Python que permite administrar de manera eficiente y organizada la información relacionada con los libros y préstamos en una biblioteca. El proyecto se ha diseñado para ofrecer funcionalidades clave como agregar, mostrar y eliminar libros, realizar operaciones de préstamo, renovación y devolución, y registrar alertas de salida irregular. El sistema está estructurado en varias clases, cada una con su conjunto de métodos para abordar diferentes aspectos de la gestión bibliotecaria.

**Características Principales:**

1. **Registro de Libros:** El sistema permite el ingreso de detalles esenciales de los libros, como su código, título, autor, área de conocimiento, fecha de publicación y más. Estos detalles se almacenan en una estructura de datos que representa la biblioteca.

2. **Operaciones de Autoservicio:** Los estudiantes pueden realizar operaciones de préstamo, renovación y devolución sin la intervención del personal de la biblioteca. Estas acciones se pueden llevar a cabo a través de un lector RFID y un sistema tipo kiosco.

3. **Alertas de Salida Irregular:** El sistema incorpora un controlador que registra las salidas irregulares de los libros de la biblioteca. Cuando un libro marcado como "en sala" sale de manera inusual, se genera una alerta para su posterior seguimiento.

4. **Interfaz de Usuario Intuitiva:** El sistema cuenta con un menú de opciones que permite a los usuarios, tanto personal de la biblioteca como estudiantes, seleccionar y ejecutar diversas operaciones. La interfaz guía al usuario a través de las diferentes funcionalidades disponibles.

5. **Gestión de Estudiantes:** Los estudiantes son representados por la clase `Estudiante`, que almacena su nombre, apellido y un ID único generado automáticamente. Esta información se utiliza en las operaciones de préstamo, renovación y devolución.

**Beneficios:**

- **Eficiencia:** El sistema automatiza muchas de las tareas manuales relacionadas con la gestión de libros y préstamos, lo que permite un flujo de trabajo más eficiente para el personal de la biblioteca y los estudiantes.

- **Organización:** La información sobre libros y préstamos se almacena y organiza de manera estructurada, facilitando la búsqueda y gestión de datos.

- **Seguimiento:** La funcionalidad de alertas de salida irregular ayuda a controlar la integridad de la colección de libros y detectar posibles problemas de seguridad.

- **Experiencia del Usuario:** La interfaz de usuario amigable hace que el sistema sea accesible y fácil de usar tanto para el personal de la biblioteca como para los estudiantes.

Este proyecto es un ejemplo de cómo se puede desarrollar una aplicación simple pero efectiva para la gestión de bibliotecas utilizando programación en Python y conceptos de estructuras de datos.
