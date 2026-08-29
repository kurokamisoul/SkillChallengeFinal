from models.contacto import Contacto
class ContactoRepository:

    def __init__(self, connection):
        self.connection = connection

    def listar_contactos(self) -> list[Contacto]:

        sql = """
            SELECT
                id,
                nombre_contacto,
                telefono,
                email,
                activo,
                fecha_creacion
            FROM contactos
            WHERE activo = TRUE
            ORDER BY id
        """

        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(sql)

            filas = cursor.fetchall()

            return [
                Contacto.from_rows(fila)
                for fila in filas
            ]

        finally:
            cursor.close()

    def obtener_por_id(
        self,
        id_contacto: int
    ) -> Contacto | None:

        sql = """
            SELECT
                id,
                nombre_contacto,
                telefono,
                email,
                activo,
                fecha_creacion
            FROM contactos
            WHERE id = %s
        """

        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(sql, (id_contacto,))

            fila = cursor.fetchone()

            if fila is None:
                return None

            return Contacto.from_rows(fila)

        finally:
            cursor.close()

    def crear(
        self,
        contacto: Contacto
    ) -> Contacto:

        sql = """
            INSERT INTO contactos (
                nombre_contacto,
                telefono,
                email,
                activo
            )
            VALUES (%s, %s, %s, %s)
        """

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                sql,
                (
                    contacto.nombre_contacto,
                    contacto.telefono,
                    contacto.email,
                    contacto.activo
                )
            )

            self.connection.commit()

            id_contacto = cursor.lastrowid

            return self.obtener_por_id(id_contacto)

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

    def actualizar(
        self,
        contacto: Contacto
    ) -> bool:

        sql = """
            UPDATE contactos
            SET
                nombre_contacto = %s,
                telefono = %s,
                email = %s
            WHERE id = %s
        """

        cursor = self.connection.cursor()

        try:

            cursor.execute(
                sql,
                (
                    contacto.nombre_contacto,
                    contacto.telefono,
                    contacto.email,
                    contacto.id
                )
            )

            self.connection.commit()

            return cursor.rowcount > 0

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()

    def eliminar(
        self,
        id_contacto: int
    ) -> bool:

        sql = """
            UPDATE contactos
            SET activo = FALSE
            WHERE id = %s
        """

        cursor = self.connection.cursor()

        try:

            cursor.execute(sql, (id_contacto,))

            self.connection.commit()

            return cursor.rowcount > 0

        except Exception:
            self.connection.rollback()
            raise

        finally:
            cursor.close()