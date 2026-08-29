from models.contacto import Contacto
from repositories.contacto_repositori import ContactoRepository
from repositories.categoria_repositori import CategoriaRepository
from services.exceptions import RegistroDuplicadoError


def validar_telefono(telefono: str) -> str:

    while len(telefono) != 10 or not telefono.isdigit():

        print(
            "El teléfono debe contener exactamente "
            "10 caracteres numéricos."
        )

        telefono = input("Ingresa el teléfono: ")

    return telefono


def validar_email(email: str) -> str:

    while (
        not email.strip()
        or "@" not in email
        or "." not in email.split("@")[1]
    ):

        print("El email no es válido.")

        email = input("Ingresa el email: ")

    return email


class ContactoService:

    def __init__(
        self,
        repository: ContactoRepository,
        categoria_repository: CategoriaRepository
    ):
        self.repository = repository
        self.categoria_repository = categoria_repository

    def seleccionar_categoria(self) -> int:

        categorias = self.categoria_repository.listar_categorias()

        if not categorias:
            raise ValueError(
                "No existen categorías disponibles."
            )

        print("\nCategorías disponibles:")

        for categoria in categorias:
            print(
                f"{categoria.id_categoria}. "
                f"{categoria.nombre}"
            )

        while True:

            try:
                id_categoria = int(
                    input("Selecciona una categoría: ")
                )

                categoria = (
                    self.categoria_repository
                    .obtener_por_id(id_categoria)
                )

                if categoria is not None:
                    return categoria.id_categoria

                print("La categoría seleccionada no existe.")

            except ValueError:
                print("Debes ingresar un número válido.")

    def registrar_contacto(self):

        nombre = input(
            "Ingresa el nombre: "
        )

        telefono = validar_telefono(
            input("Ingresa el teléfono: ")
        )

        email = validar_email(
            input("Ingresa el email: ")
        )

        if self.repository.existe_email(email):

            raise RegistroDuplicadoError(
                "Ya existe un contacto activo con ese correo."
        )

        id_categoria = self.seleccionar_categoria()

        contacto = Contacto.crear_contacto(
            nombre,
            telefono,
            email,
            id_categoria
        )

        contacto = self.repository.crear(
            contacto
        )

        print(
            f"El contacto "
            f"{contacto.nombre_contacto} "
            f"se agregó correctamente."
        )
        return contacto

    def mostrar_contactos(self):

        contactos = self.repository.listar_con_categoria()

        if not contactos:
            print("No existen contactos.")
            return

        print("\n--- CONTACTOS ---")

        for contacto in contactos:

            print(
                f"ID: {contacto['id']} | "
                f"Nombre: {contacto['nombre_contacto']} | "
                f"Teléfono: {contacto['telefono']} | "
                f"Email: {contacto['email']} | "
                f"Categoría: {contacto['categoria']} | "
                f"Fecha: {contacto['fecha_creacion']}"
            )

    def actualizar_contacto(self):

        try:
            id_contacto = int(
                input("Ingresa el ID del contacto: ")
            )

        except ValueError:
            print("El ID debe ser numérico.")
            return

        contacto = self.repository.obtener_por_id(
            id_contacto
        )

        if contacto is None:
            print("Contacto no encontrado.")
            return

        contacto.nombre_contacto = input(
            "Ingresa el nuevo nombre: "
        )

        contacto.telefono = validar_telefono(
            input("Ingresa el nuevo teléfono: ")
        )

        contacto.email = validar_email(
            input("Ingresa el nuevo email: ")
        )

        if self.repository.existe_email_en_otro_contacto(
            contacto.email,
            contacto.id
        ):

            raise RegistroDuplicadoError(
                "Ese correo ya pertenece a otro contacto activo."
            )

        contacto.id_categoria = (
            self.seleccionar_categoria()
        )

        if self.repository.actualizar(contacto):

            print(
                "Contacto actualizado correctamente."
            )
            return contacto
        
        else:

            print(
                "No se pudo actualizar el contacto."
            )
            return None

    def eliminar_contacto(self):

        try:
            id_contacto = int(
                input("Ingresa el ID del contacto: ")
            )

        except ValueError:
            print("El ID debe ser numérico.")
            return

        if self.repository.eliminar(id_contacto):

            print(
                "Contacto eliminado correctamente."
            )
            return id_contacto
        else:

            print(
                "Contacto no encontrado."
            )
            return None