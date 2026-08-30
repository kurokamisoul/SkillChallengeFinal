# SkillChallengeFinal

## Descripción

SkillChallengeFinal es una aplicación de consola desarrollada en Python para la gestión de contactos personales.

El sistema utiliza MySQL como sistema gestor de base de datos y está organizado mediante una arquitectura en capas, separando los modelos, el acceso a datos, la lógica de negocio y el punto de entrada de la aplicación.

El proyecto permite administrar contactos, asociarlos con categorías y generar reportes a partir de la información almacenada.

---

## Funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- Crear contactos.
- Consultar contactos.
- Actualizar contactos.
- Eliminar contactos mediante eliminación lógica.
- Asociar contactos con categorías.
- Validar números telefónicos.
- Validar correos electrónicos.
- Evitar registros con correos electrónicos duplicados.
- Validar que la categoría seleccionada exista.
- Registrar auditoría de operaciones mediante JSON.
- Exportar el listado de contactos a un archivo CSV.
- Generar un reporte con la cantidad de contactos por categoría.

---

## Arquitectura

El proyecto utiliza una arquitectura en capas:

```text
SkillChallengeFinal/
│
├── models/
│   └── contacto.py
│
├── repositories/
│   ├── db.py
│   ├── contacto_repositori.py
│   ├── categoria_repositori.py
│   └── reportes_repository.py
│
├── services/
│   ├── contacto_services.py
│   ├── archivo_services.py
│   ├── exceptions.py
│   └── reportes_service.py
│
├── data/
│   └── auditoria.json
│
├── reportes/
│   └── contactos.csv
│
├── sql/
│   └── ...
│
├── .env
├── .gitignore
├── CONFLICTOS.md
├── README.md
├── requirements.txt
└── main.py
```

### Models

Contiene las clases que representan las entidades utilizadas por la aplicación.

La clase `Contacto` representa la información de un contacto y utiliza `dataclass`.

### Repositories

Esta capa se encarga del acceso a la base de datos.

Contiene:

- Conexión con MySQL.
- Consultas SQL.
- Inserción de contactos.
- Consulta de contactos.
- Actualización de contactos.
- Eliminación lógica.
- Consulta de categorías.
- Consultas utilizadas para generar reportes.

### Services

Esta capa contiene la lógica de negocio de la aplicación.

Se encarga de:

- Validaciones.
- Reglas de negocio.
- Registro de contactos.
- Actualización y eliminación.
- Manejo de archivos.
- Auditoría.
- Generación de reportes.
- Manejo de excepciones propias.

### main.py

Es el punto de entrada de la aplicación.

Se encarga de:

- Mostrar el menú.
- Recibir las opciones del usuario.
- Invocar los servicios correspondientes.
- Capturar las excepciones.
- Mostrar mensajes claros al usuario.

---

## Base de datos

El proyecto utiliza **MySQL** para la persistencia de información.

La entidad principal es `contactos` y existe una relación de uno a muchos entre `categorias` y `contactos`.

```text
categorias
     1
     │
     │ id_categoria
     │
     N
contactos
```

Una categoría puede tener múltiples contactos, mientras que cada contacto pertenece a una categoría.

La tabla `contactos` utiliza `id_categoria` como llave foránea hacia la tabla `categorias`.

---

## Reporte de contactos por categoría

El proyecto cuenta con un reporte que permite conocer cuántos contactos existen en cada categoría.

La consulta utiliza la relación entre ambas tablas y funciones de agregación.

Ejemplo:

```sql
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
    cat.nombre;
```

El resultado puede mostrar información como:

```text
Amigos: 4 contactos
Familia: 2 contactos
Otros: 1 contactos
Personal: 0 contactos
Trabajo: 1 contactos
```

Se utiliza `LEFT JOIN` para que también aparezcan las categorías que no tengan contactos activos.

---

## Reglas de negocio

El sistema implementa reglas de negocio que dependen de información existente en la base de datos.

1. No se permite registrar un contacto con un correo ya existente.
2. La categoría seleccionada debe existir en la base de datos.
3. Los contactos eliminados se desactivan, no se borran físicamente.
4. El teléfono debe contener exactamente 10 caracteres numéricos.
5. El correo debe tener un formato básico válido.

La regla de correo duplicado utiliza `RegistroDuplicadoError`, una excepción propia que hereda de `Exception`.

---

## Manejo de excepciones

El proyecto utiliza excepciones específicas para evitar que el programa termine abruptamente ante errores esperados.

Se implementó una excepción propia:

```python
class RegistroDuplicadoError(Exception):
    pass
```

Las excepciones se definen y lanzan en las capas correspondientes y son capturadas en `main.py`.

Ejemplo:

```python
try:
    service.registrar_contacto()
except RegistroDuplicadoError as error:
    print(f"Error: {error}")
except Error as error:
    print(f"Error de base de datos: {error}")
```

También se manejan errores relacionados con la generación y escritura de archivos.

---

## Auditoría mediante JSON

El sistema registra las operaciones realizadas sobre los contactos en:

```text
data/auditoria.json
```

Actualmente se registran las siguientes operaciones:

```text
CREATE
UPDATE
DELETE
```

Cada registro contiene:

- Operación realizada.
- ID del contacto.
- Fecha y hora.

Ejemplo:

```json
{
    "operacion": "CREATE",
    "id_contacto": 5,
    "fecha": "2026-08-29T18:00:00"
}
```

El archivo JSON funciona como un registro de auditoría de las operaciones realizadas por el usuario.

---

## Exportación CSV

El sistema permite exportar el listado completo de contactos a:

```text
reportes/contactos.csv
```

El archivo contiene información como:

- ID.
- Nombre.
- Teléfono.
- Email.
- Estado.
- Fecha de creación.
- ID de categoría.
- Categoría.

El archivo puede abrirse directamente con Microsoft Excel u otro programa compatible con archivos CSV.

---

## Menú de la aplicación

El menú principal permite realizar las operaciones disponibles:

```text
MENU DE CONTACTOS

1. Agregar
2. Ver
3. Actualizar
4. Eliminar
5. Salir
6. Exportar contactos a CSV
7. Contactos por categoría
```

---

## Requisitos

Para ejecutar el proyecto se requiere:

- Python 3.13 o compatible.
- MySQL.
- pip.
- Git.

Las dependencias de Python se encuentran en:

```text
requirements.txt
```

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/kurokamisoul/SkillChallengeFinal.git
```

Entrar al directorio:

```bash
cd SkillChallengeFinal
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## Configuración de la base de datos

Crear un archivo `.env` en la raíz del proyecto con las credenciales correspondientes:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=tu_base_de_datos
```

Las credenciales reales no deben publicarse en GitHub.

El archivo `.env` se encuentra contemplado dentro de `.gitignore`.

La estructura y creación de las tablas se encuentra en los archivos SQL del proyecto.

---

## Ejecución

Desde la raíz del proyecto ejecutar:

```bash
python main.py
```

La aplicación mostrará el menú principal y permitirá interactuar con la base de datos.

---

## Control de versiones

El desarrollo del proyecto se realizó utilizando Git y ramas de trabajo.

Las principales ramas utilizadas fueron:

```text
main
excepciones
auditoria
reportes
```

### Rama excepciones

En esta rama se implementaron:

- Excepciones propias.
- Manejo específico de errores.
- Reglas de negocio.

### Rama auditoria

En esta rama se implementaron:

- Registro de operaciones en JSON.
- Exportación de contactos a CSV.
- Actualización de documentación del proyecto.

### Rama reportes

En esta rama se implementaron:

- Consulta de contactos agrupados por categoría.
- Lógica para generar el reporte.
- Integración del reporte con la aplicación.

Las ramas de trabajo fueron integradas mediante merges hacia `main`.

---

## Conflictos

Durante el desarrollo del proyecto se provocó y resolvió un conflicto real durante la integración de cambios.

El conflicto involucró principalmente modificaciones en:

```text
main.py
```

La resolución permitió integrar correctamente las funcionalidades desarrolladas en diferentes ramas.

El proceso se encuentra documentado en:

```text
CONFLICTOS.md
```

---

## Objetivo del proyecto

El objetivo del proyecto es aplicar los conocimientos adquiridos en programación con Python y bases de datos mediante el desarrollo de una aplicación funcional.

Se aplican los siguientes conceptos:

- Programación orientada a objetos.
- Arquitectura en capas.
- Persistencia en MySQL.
- Relaciones entre tablas.
- Llaves foráneas.
- Consultas SQL.
- Reglas de negocio.
- Manejo de excepciones.
- Excepciones personalizadas.
- Manejo de archivos CSV.
- Manejo de archivos JSON.
- Auditoría.
- Reportes.
- Control de versiones con Git.

---

## Autor

Proyecto desarrollado como parte del **Skill Challenge Final**.
