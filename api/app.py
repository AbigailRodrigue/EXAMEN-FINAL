from fastapi import FastAPI, HTTPException
from api.database import init_db, create_connection 
from datetime import datetime

app = FastAPI()

# Inicializa la base de datos
init_db()

@app.get("/estudiantes")
def leer_estudiantes():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alumnos")
    estudiantes = cur.fetchall()
    conn.close()
    return [dict(zip(["id", "nombre", "apellido", "aprobado", "nota", "fecha"], estudiante)) for estudiante in estudiantes]

@app.get("/estudiantes/{id}")
def leer_estudiante(id: int):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alumnos WHERE id=?", (id,))
    estudiante = cur.fetchone()
    conn.close()
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    return dict(zip(["id", "nombre", "apellido", "aprobado", "nota", "fecha"], estudiante))

@app.post("/estudiantes")
def crear_estudiante(nombre: str, apellido: str, aprobado: bool, nota: float):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO alumnos (nombre, apellido, aprobado, nota, fecha) VALUES (?, ?, ?, ?, ?)",
                (nombre, apellido, aprobado, nota, datetime.now()))
    conn.commit()
    conn.close()
    return {"mensaje": "Estudiante creado"}

@app.put("/estudiantes/{id}")
def actualizar_estudiante(id: int, nombre: str, apellido: str, aprobado: bool, nota: float):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE alumnos SET nombre=?, apellido=?, aprobado=?, nota=? WHERE id=?", 
                (nombre, apellido, aprobado, nota, id))
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    conn.commit()
    conn.close()
    return {"mensaje": "Estudiante actualizado"}

@app.delete("/estudiantes/{id}")
def eliminar_estudiante(id: int):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM alumnos WHERE id=?", (id,))
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    conn.commit()
    conn.close()
    return {"mensaje": "Estudiante eliminado"}


