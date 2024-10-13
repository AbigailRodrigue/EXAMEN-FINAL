import sqlite3
from datetime import datetime

conn = sqlite3.connect('estudiante.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    aprobado INTEGER NOT NULL,  -- Cambiado a INTEGER
    nota REAL NOT NULL,
    fecha TIMESTAMP NOT NULL
)
''')

alumnos = [
    ('Juan', 'Pérez', 1, 7.5, '2024-09-01 00:00:00'),  # Cambiado a 1
    ('María', 'López', 0, 4.2, '2024-09-02 00:00:00'),  # Cambiado a 0
    ('Carlos', 'García', 1, 8.9, '2024-09-03 00:00:00'),  # Cambiado a 1
    ('Lucía', 'Martínez', 1, 9.1, '2024-09-04 00:00:00'),  # Cambiado a 1
    ('Sofía', 'Fernández', 0, 5.0, '2024-09-05 00:00:00')  # Cambiado a 0
]

cur.executemany('''
    INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha)
    VALUES (?, ?, ?, ?, ?)
''', alumnos)

conn.commit()
conn.close()

print("Base de datos creada y registros insertados correctamente.")

print("Base de datos creada y registros insertados correctamente.")
