from repositories.reportes_repositori import ReportesRepository


class ReportesService:

    def __init__(self, repository: ReportesRepository):
        self.repository = repository

    def mostrar_contactos_por_categoria(self):
        resultados = self.repository.contactos_por_categoria()

        if not resultados:
            print("No existen datos para generar el reporte.")
            return

        print("\n--- CONTACTOS POR CATEGORÍA ---")

        for resultado in resultados:
            print(
                f"{resultado['categoria']}: "
                f"{resultado['total_contactos']} contactos"
            )

        return resultados