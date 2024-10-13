import sqlite3

def create_connection():
    """Establece la conexión con la base de datos."""
    conn = sqlite3.connect('estudiante.db')
    return conn

def init_db():
    """Inicializa la base de datos creando la tabla 'alumnos' si no existe."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            aprobado BOOLEAN NOT NULL,
            nota REAL NOT NULL CHECK(nota >= 0 AND nota <= 10),
            fecha TIMESTAMP NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def verificar_tablas():
    """Verifica si la tabla 'alumnos' existe en la base de datos."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='alumnos'")
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        print("La tabla 'alumnos' existe.")
    else:
        print("La tabla 'alumnos' no existe.")
