
#CONEXION DE LA BASE Y PYTHON

#Se importa el modulo sqlite3 para establecer la conexion y 
# trabajar con bases de datos SQLite.

import sqlite3

#Se define la clase ConexionBase, que centraliza la conexión a la base de datos.
#__init__: el constructor de la clase. Los guiones permiten encapsularlo.
#nombre_bd: nombre del archivo de la base ("libreta_contactos.db").
#conexion: guarda la conexión activa con SQLite.
#cursor: permite ejecutar sentencias SQL.

class ConexionBase:
    def __init__(self,nombre_db = 'Libreta_Contactos.db'):
        self.nombre_db = nombre_db
        self.conexion = None
        self.cursor = None

#Método conectar: abre la conexión con la base (.connect()) y crea un cursor, 
#para ejecutar sentencias SQL (.cursor()).

    def conectar(self):
        self.conexion = sqlite3.connect(self.nombre_bd)
        self.cursor = self.conexion.cursor()
    
#Método ejecutar:
#Recibe una sentencia SQL (sql) y opcionalmente parámetros (params).
#Usa cursor.execute(sql, params) para ejecutarla.
#Llama a commit() para guardar los cambios en la base (ejemplo: INSERT, UPDATE, DELETE).

    def ejecutar(self, sql, params=()):
        self.cursor.execute(sql, params)
        self.conexion.commit()

#Método consultar: Se usa para sentencias SELECT.
#Ejecuta la consulta y devuelve todos los resultados con .fetchall().
#Devuelve una lista de tuplas (cada tupla es una fila de la tabla).

    def consultar(self, sql, params=()):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

#Método cerrar: Cierra la conexión con la base de datos.

    def cerrar(self):
        self.conexion.close()    
