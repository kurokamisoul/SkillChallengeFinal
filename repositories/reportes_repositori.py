class ReportesRepository:

    def __init__(self, connection):
        self.connection = connection

    def contactos_por_categoria(self) -> list[dict]:
        sql = """
            SELECT
                cat.nombre AS categoria,
                COUNT(c.id) AS total_contactos
            FROM categorias AS cat
            LEFT JOIN contactos AS c
                ON c.id_categoria = cat.id_categoria
                AND c.activo = TRUE
            GROUP BY
                cat.id_categoria,
                cat.nombre
            ORDER BY
                cat.nombre
        """

        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()