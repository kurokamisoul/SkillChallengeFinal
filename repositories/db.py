import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "gestion_empleados_rh"
    )

def inicializar():
    conn = get_connection()
    cursor = conn.cursor()
    with open("gestion_empleados.sql","r",encoding="utf-8") as file:
        for sentencia in file.read().split(";"):
            if sentencia.strip():
                cursor.execute(sentencia)

    conn.commit()
    cursor.close()
    conn.close()
