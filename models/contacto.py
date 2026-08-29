from dataclasses import dataclass
from datetime import datetime

@dataclass
class Contacto:
    id : int | None
    nombre_contacto : str
    telefono : str
    email : str
    activo : bool
    fecha_creacion : datetime | None
    id_categoria: int

    @classmethod
    def crear_contacto(
        cls,
        nombre_contacto : str,
        telefono : str,
        email : str,
        id_categoria : int
    ) -> "Contacto":

        return cls(
            id = None,
            nombre_contacto = nombre_contacto,
            telefono = telefono,
            email = email,
            activo = True,
            fecha_creacion = None,
            id_categoria = id_categoria
        )

    @classmethod
    def from_rows(cls, row:dict) -> "Contacto":
        return cls(
             id = row['id'],
            nombre_contacto = row['nombre_contacto'],
            telefono = row['telefono'],
            email = row['email'],
            activo = row['activo'],
            fecha_creacion = row['fecha_creacion'],
            id_categoria = row['fecha_creacion']
        )

