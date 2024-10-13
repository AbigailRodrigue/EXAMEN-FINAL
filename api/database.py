import sqlite3

def create_connection():
    conn = sqlite3.connect('estudiante.db')
    return conn

def init_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        aprobado INTEGER NOT NULL,  -- Cambiado a INTEGER
        nota REAL NOT NULL CHECK(nota >= 0 AND nota <= 10),
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Se establece la fecha automáticamente
    )
    ''')
    conn.commit()
    conn.close()
 