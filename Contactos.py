
#Importa la clase creada en db.conexion.py, 
# encargada de conectarse a la base de datos y ejecutar consultas.
from db_conexion import ConexionBase

#Se crea la clase Contacto.
#__init__: es el constructor, se ejecuta cuando creamos un nuevo objeto.
#Atributos: guardan la información de un contacto.

class Contacto:
    def __init__(self, nombre, apellido, telefono, email, id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

#Método guardar:
#Si el contacto no tiene id → significa que es nuevo, entonces hace un INSERT.
#Si el contacto ya tiene id → significa que existe en la BD, entonces hace un UPDATE.
#Usa ? como parámetros seguros para evitar inyección SQL.
#db.ejecutar(...) ejecuta la consulta en SQLite.

    def guardar(self):
        db = ConexionBase()
        db.conectar()
        if self.id is None:  # Alta
            db.ejecutar(
                "INSERT INTO Contactos (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)",
                (self.nombre, self.apellido, self.telefono, self.email)
            )
        else:  # Modificación
            db.ejecutar(
                "UPDATE Contactos SET nombre=?, apellido=?, telefono=?, email=? WHERE id=?",
                (self.nombre, self.apellido, self.telefono, self.email, self.id)
            )

#Método eliminar: Solo funciona si el contacto tiene un id.
#Ejecuta un DELETE en la base de datos para borrar ese contacto específico.

    def eliminar(self):
        if self.id is not None:
            db = ConexionBase()
            db.conectar()
            db.ejecutar("DELETE FROM Contactos WHERE id=?", (self.id,))
            db.cerrar()

#Método listar:
#Es un método estático (no necesita crear un objeto Contacto para usarlo → se llama directo: Contacto.listar()).
#Ejecuta un SELECT para obtener todos los contactos de la base.
#Devuelve una lista con tuplas.

    @staticmethod
    def listar():
        db = ConexionBase()
        db.conectar()
        contactos = db.consultar("SELECT * FROM Contactos")
        db.cerrar()
        return contactos
                 