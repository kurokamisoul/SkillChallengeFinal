from models.categoria import Categoria


class CategoriaRepository:

    def __init__(self, connection):
        self.connection = connection

    def listar_categorias(self) -> list[Categoria]:

        sql = """
            SELECT
                id_categoria,
                nombre,
                descripcion,
                activo
            FROM categorias
            WHERE activo = TRUE
            ORDER BY nombre
        """

        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(sql)

            filas = cursor.fetchall()

            return [
                Categoria.from_rows(fila)
                for fila in filas
            ]

        finally:
            cursor.close()

    def obtener_por_id(
        self,
        id_categoria: int
    ) -> Categoria | None:

        sql = """
            SELECT
                id_categoria,
                nombre,
                descripcion,
                activo
            FROM categorias
            WHERE id_categoria = %s
        """

        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(sql, (id_categoria,))

            fila = cursor.fetchone()

            if fila is None:
                return None

            return Categoria.from_rows(fila)

        finally:
            cursor.close()