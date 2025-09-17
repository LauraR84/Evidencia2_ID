
# Importa la clase creada en db_conexion.py,
# encargada de conectarse a la base de datos y ejecutar consultas.
from db_conexion import ConexionBase

# Se crea la clase Contacto.
class Contacto:
    def __init__(self, nombre, apellido, telefono, email, id=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    # Método guardar
    def guardar(self):
        db = ConexionBase()
        try:
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
        finally:
            db.cerrar()

    # Método eliminar
    def eliminar(self):
        if self.id is not None:
            db = ConexionBase()
            db.conectar()
            db.ejecutar("DELETE FROM Contactos WHERE id=?", (self.id,))
            db.cerrar()

    # Método listar (estático)
    @staticmethod
    def listar():
     conexion = ConexionBase()
     conexion.conectar()
     conexion.cursor.execute("SELECT id, nombre, apellido, telefono, email FROM Contactos")
     contactos = conexion.cursor.fetchall()
     conexion.cerrar()
     return contactos

