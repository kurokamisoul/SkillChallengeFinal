from repositories.db import get_connection
from repositories.contacto_repositori import ContactoRepository
from services.contacto_services import ContactoService


def menu_contactos():

    try:
        connection = get_connection()
    except Exception as e:
        print(f"No fue posible conectar con MySQL: {e}")
        return

    repository = ContactoRepository(connection)
    service = ContactoService(repository)

    try:
        while True:

            print(
                """
            MENU DE CONTACTOS

            1. Agregar
            2. Ver
            3. Actualizar
            4. Eliminar
            5. Salir
            """
            )

            opcion = input("Opción: ")

            match opcion:

                case "1":
                    service.registrar_contacto()

                case "2":
                    service.mostrar_contactos()

                case "3":
                    service.actualizar_contacto()

                case "4":
                    service.eliminar_contacto()

                case "5":
                    break

                case _:
                    print("Opción no válida.")
    finally:
        connection.close()
    


if __name__ == "__main__":
    menu_contactos()