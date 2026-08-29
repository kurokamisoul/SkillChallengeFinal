# Registro de conflictos de Git

## Conflicto 1: Integración de manejo de excepciones y auditoría

### Fecha

Agosto de 2026.

### Archivo afectado

`main.py`

### Ramas involucradas

- `excepciones`
- `reportes`

### Descripción del conflicto

El conflicto se produjo al integrar los cambios realizados en diferentes ramas
del proyecto.

La rama `excepciones` incorporaba el manejo de errores de dominio y de base de
datos, específicamente el uso de la excepción propia `RegistroDuplicadoError`.

Por otra parte, la rama `reportes` incorporaba el sistema de auditoría mediante
`ArchivoService`, así como el registro de las operaciones realizadas sobre los
contactos y la exportación de información a CSV.

Ambas ramas modificaron `main.py` en las mismas secciones del menú principal,
por lo que Git no pudo determinar automáticamente qué versión debía conservar.

### Cambios de la rama `excepciones`

La rama `excepciones` incorporaba:

- Importación de `RegistroDuplicadoError`.
- Manejo de `RegistroDuplicadoError` al registrar contactos.
- Manejo de errores de MySQL mediante `mysql.connector.Error`.
- Manejo de errores durante las operaciones del CRUD.
- Manejo del error de conexión con la base de datos.

Un fragmento que generó conflicto fue:

```python
from services.exceptions import RegistroDuplicadoError
```

y el manejo de la excepción al crear un contacto:

```python
try:
    service.registrar_contacto()
except RegistroDuplicadoError as error:
    print(f"Error: {error}")
except Error as error:
    print(f"Error de base de datos: {error}")
```

### Cambios de la rama `reportes`

La rama `reportes` incorporaba:

- `ArchivoService`.
- Registro de auditoría de las operaciones `CREATE`, `UPDATE` y `DELETE`.
- Exportación de contactos a CSV.
- Opción del menú para generar el reporte.
- Registro del ID del contacto afectado por cada operación.

Por ejemplo:

```python
from services.archivo_services import ArchivoService
```

y después de registrar un contacto:

```python
contacto = service.registrar_contacto()

archivo_service.registrar_auditoria(
    "CREATE",
    contacto.id
)
```

### Conflicto generado

Al realizar la integración, Git encontró modificaciones diferentes en las
mismas líneas de `main.py`.

El conflicto se mostró mediante los marcadores:

```text
<<<<<<< Updated upstream
...
=======
...
>>>>>>> Stashed changes
```

El problema consistía en que no se podía conservar únicamente una de las
versiones, ya que ambas contenían funcionalidades necesarias para el proyecto.

### Resolución

El conflicto se resolvió manualmente conservando las funcionalidades de
ambas ramas.

Se mantuvo:

1. El manejo de `RegistroDuplicadoError`.
2. El manejo de errores de base de datos.
3. La inicialización de `ArchivoService`.
4. La auditoría de las operaciones `CREATE`, `UPDATE` y `DELETE`.
5. La exportación de contactos a CSV.
6. El manejo de los valores retornados por los métodos del servicio para
   obtener el ID del contacto afectado.

Se eliminaron los marcadores de conflicto de Git y se dejó una única versión
funcional de `main.py`.

### Validación posterior

Después de resolver el conflicto se ejecutó nuevamente el programa y se
realizaron pruebas de las operaciones principales.

Se verificó que:

- El programa inicia correctamente.
- Los contactos pueden registrarse.
- Los contactos pueden consultarse.
- Los contactos pueden actualizarse.
- Los contactos pueden eliminarse.
- Los errores de negocio pueden mostrarse al usuario.
- Las operaciones realizadas pueden registrarse mediante auditoría.
- El reporte CSV puede generarse.

No se realizó el commit hasta comprobar que el programa funcionaba
correctamente después de resolver el conflicto.

### Resultado

El conflicto fue resuelto satisfactoriamente y los cambios fueron integrados
en la rama correspondiente mediante Git.

Este conflicto permitió comprobar el proceso de resolución manual de conflictos
y evitar que una funcionalidad desarrollada en una rama fuera sobrescrita por
los cambios de otra.
