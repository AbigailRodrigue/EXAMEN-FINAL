import sqlite3

def crear_tabla_y_insertar_datos():
    conn = sqlite3.connect('estudiante.db')
    cursor = conn.cursor()

    # Crear tabla si no existe
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

    # Datos iniciales
    alumnos = [
        ('Juan', 'Pérez', True, 7.5, '2024-09-01 00:00:00'),
        ('María', 'López', False, 4.2, '2024-09-02 00:00:00'),
        ('Carlos', 'García', True, 8.9, '2024-09-03 00:00:00'),
        ('Lucía', 'Martínez', True, 9.1, '2024-09-04 00:00:00'),
        ('Sofía', 'Fernández', False, 5.0, '2024-09-05 00:00:00')
    ]

    # Insertar los datos
    cursor.executemany('''
        INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha)
        VALUES (?, ?, ?, ?, ?)
    ''', alumnos)

    conn.commit()
    conn.close()
    print("Tabla creada y datos insertados correctamente.")

crear_tabla_y_insertar_datos()
