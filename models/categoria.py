from dataclasses import dataclass


@dataclass
class Categoria:
    id_categoria: int
    nombre: str
    descripcion: str | None
    activo: bool

    @classmethod
    def from_rows(cls, row: dict) -> "Categoria":

        return cls(
            id_categoria=row["id_categoria"],
            nombre=row["nombre"],
            descripcion=row["descripcion"],
            activo=row["activo"]
        )