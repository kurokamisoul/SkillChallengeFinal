from models.contacto import Contacto
from repositories.contacto_repositori import ContactoRepository

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
        repository: ContactoRepository
    ):
        self.repository = repository

    def registrar_contacto(self):

        nombre = input("Ingresa el nombre: ")

        telefono = validar_telefono(
            input("Ingresa el teléfono: ")
        )

        email = validar_email(
            input("Ingresa el email: ")
        )

        contacto = Contacto.crear_contacto(
            nombre,
            telefono,
            email
        )

        contacto = self.repository.crear(contacto)

        print(
            f"El contacto {contacto.nombre_contacto} "
            f"se agregó correctamente."
        )

    def mostrar_contactos(self):

        contactos = self.repository.listar_contactos()

        if not contactos:
            print("No existen contactos.")
            return

        for contacto in contactos:
            print(contacto)

    def actualizar_contacto(self):

        id_contacto = int(
            input("Ingresa el ID del contacto: ")
        )

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

        if self.repository.actualizar(contacto):
            print("Contacto actualizado.")

    def eliminar_contacto(self):

        id_contacto = int(
            input("Ingresa el ID del contacto: ")
        )

        if self.repository.eliminar(id_contacto):
            print("Contacto eliminado.")
        else:
            print("Contacto no encontrado.")