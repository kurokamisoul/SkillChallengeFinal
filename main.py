from repositories.db import get_connection

from repositories.contacto_repositori import ContactoRepository

from repositories.categoria_repositori import CategoriaRepository

from services.contacto_services import ContactoService

from services.exceptions import RegistroDuplicadoError

from services.archivo_services import ArchivoService

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

    archivo_service = ArchivoService()

    while True:

        print(
            """
        MENU DE CONTACTOS

        1. Agregar
        2. Ver
        3. Actualizar
        4. Eliminar
        5. Salir
        6. Exportar contactos a CSV
        """
        )

        opcion = input("Opción: ")

        match opcion:

            case "1":

                try:

                    contacto = service.registrar_contacto()

                    archivo_service.registrar_auditoria(
                        "CREATE",
                        contacto.id
                    )

                except RegistroDuplicadoError as error:

                    print(
                        f"Error: {error}"
                    )

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

                except OSError as error:

                    print(
                        f"Error al registrar la auditoría: {error}"
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

                    contacto = service.actualizar_contacto()

                    if contacto is not None:

                        archivo_service.registrar_auditoria(
                            "UPDATE",
                            contacto.id
                        )

                except RegistroDuplicadoError as error:

                    print(
                        f"Error: {error}"
                    )

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

                except OSError as error:

                    print(
                        f"Error al registrar la auditoría: {error}"
                    )

            case "4":

                try:

                    id_contacto = service.eliminar_contacto()

                    if id_contacto is not None:

                        archivo_service.registrar_auditoria(
                            "DELETE",
                            id_contacto
                        )

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

                except OSError as error:

                    print(
                        f"Error al registrar la auditoría: {error}"
                    )

            case "5":

                break

            case "6":

                try:

                    contactos = (
                        contacto_repository
                        .listar_con_categoria()
                    )

                    archivo_service.exportar_contactos_csv(
                        contactos
                    )

                    print(
                        "Reporte CSV generado correctamente."
                    )

                except Error as error:

                    print(
                        f"Error de base de datos: {error}"
                    )

                except OSError as error:

                    print(
                        f"Error al generar el archivo: {error}"
                    )

            case _:

                print(
                    "Opción no válida."
                )

    connection.close()


if __name__ == "__main__":

    menu_contactos()