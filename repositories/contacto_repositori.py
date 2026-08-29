from repositories.db import get_connection, inicializar
from models.contacto import Contacto

def listar_Contactos() -> list:
    inicializar()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Contactos")
    filas= cursor.fetchall()
    cursor.close()
    conn.close()
    return [Contacto.from_row(fila) for fila in filas]




if __name__ == "__main__":
    print("Listar Contactos services")
    print(listar_Contactos())