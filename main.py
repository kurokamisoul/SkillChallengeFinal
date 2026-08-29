from repositories.db import get_connection
from repositories.contacto_repositori import ContactoRepository
from repositories.categoria_repositori import CategoriaRepository
from services.contacto_services import ContactoService


def menu_contactos():

    connection = get_connection()

    contacto_repository = ContactoRepository(
        connection
    )

    categoria_repository = CategoriaRepository(
        connection
    )

    service = ContactoService(
        contacto_repository,
        categoria_repository
    )

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

    connection.close()


if __name__ == "__main__":
    menu_contactos()