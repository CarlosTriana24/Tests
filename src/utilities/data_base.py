import sqlite3

class DataBase:
    def __init__(self, db_name):
        """ Inicializa la conexión con la base de datos """
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        """ Abre la conexión si no está abierta """
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

    def execute_query(self, query, params=()):
        """ Ejecuta una consulta (INSERT, UPDATE, DELETE) con manejo de errores """
        try:
            self.connect()
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            self.close_connection()

    def fetch_all_rows(self, query, params=()):
        """ Obtiene todas las filas de una consulta (SELECT) """
        try:
            self.connect()
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []
        finally:
            self.close_connection()

    def fetch_one_row(self, query, params=()):
        """ Obtiene solo una fila de una consulta (SELECT) """
        try:
            self.connect()
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            self.close_connection()

    def close_connection(self):
        """ Cierra la conexión a la base de datos si está abierta """
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None
