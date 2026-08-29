from repositories.db import get_connection
from repositories.contacto_repositori import ContactoRepository
from repositories.categoria_repositori import CategoriaRepository
from services.contacto_services import ContactoService
from services.exceptions import RegistroDuplicadoError
from mysql.connector import Error

def menu_contactos():
    try:
        connection = get_connection()
    except Error as error:

        print(
            f"No fue posible conectar con la base de datos: {error}"
        )

        return
    
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

                try:

                    service.registrar_contacto()

                except RegistroDuplicadoError as error:

                    print(f"Error: {error}")
                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

            case "2":

                try:

                    service.mostrar_contactos()

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

            case "3":

                try:

                    service.actualizar_contacto()

                except RegistroDuplicadoError as error:

                    print(f"Error: {error}")

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

            case "4":

                try:

                    service.eliminar_contacto()

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

            case "5":
                break

            case _:
                print("Opción no válida.")

    connection.close()


if __name__ == "__main__":
    menu_contactos()