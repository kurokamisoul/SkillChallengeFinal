import csv
import json
from datetime import datetime
from pathlib import Path


class ArchivoService:

    def __init__(self):

        self.directorio_reportes = Path("reportes")
        self.directorio_data = Path("data")

        self.directorio_reportes.mkdir(
            exist_ok=True
        )

        self.directorio_data.mkdir(
            exist_ok=True
        )

        self.archivo_auditoria = (
            self.directorio_data / "auditoria.json"
        )

    def exportar_contactos_csv(
        self,
        contactos: list[dict]
    ) -> None:

        archivo = (
            self.directorio_reportes /
            "contactos.csv"
        )

        with archivo.open(
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Nombre",
                "Telefono",
                "Email",
                "Activo",
                "Fecha Creacion",
                "ID Categoria",
                "Categoria"
            ])

            for contacto in contactos:

                writer.writerow([
                    contacto["id"],
                    contacto["nombre_contacto"],
                    contacto["telefono"],
                    contacto["email"],
                    contacto["activo"],
                    contacto["fecha_creacion"],
                    contacto["id_categoria"],
                    contacto["categoria"]
                ])

    def registrar_auditoria(
        self,
        operacion: str,
        id_contacto: int
    ) -> None:

        operaciones = []

        if self.archivo_auditoria.exists():

            try:

                with self.archivo_auditoria.open(
                    "r",
                    encoding="utf-8"
                ) as file:

                    operaciones = json.load(file)

            except json.JSONDecodeError:

                operaciones = []

        registro = {
            "operacion": operacion,
            "id_contacto": id_contacto,
            "fecha": datetime.now().isoformat(
                timespec="seconds"
            )
        }

        operaciones.append(registro)

        with self.archivo_auditoria.open(
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                operaciones,
                file,
                indent=4,
                ensure_ascii=False
            )