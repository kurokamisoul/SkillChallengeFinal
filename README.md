# SkillChallengeFinal

Aplicación de consola desarrollada en Python para la gestión de contactos,
utilizando MySQL como sistema de persistencia y una arquitectura organizada
por capas.

## Descripción

El proyecto permite administrar contactos mediante un CRUD completo:

- Crear contactos.
- Consultar contactos.
- Actualizar contactos.
- Eliminar contactos mediante desactivación lógica.
- Asociar cada contacto con una categoría.
- Validar teléfono y correo electrónico.
- Evitar el registro de correos electrónicos duplicados.
- Registrar auditoría de las operaciones realizadas.
- Exportar el listado de contactos a CSV.

El proyecto fue desarrollado como parte del Skill Challenge y busca aplicar
principios de programación orientada a objetos, separación de responsabilidades,
persistencia en base de datos, manejo de excepciones y control de versiones
con Git.

## Tecnologías

- Python 3.13
- MySQL
- mysql-connector-python
- python-dotenv
- Git / GitHub

## Arquitectura

El proyecto utiliza una arquitectura en capas:

```text
SkillChallengeFinal/
│
├── main.py
├── CONFLICTOS.md
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── models/
│   └── contacto.py
│
├── repositories/
│   ├── db.py
│   ├── contacto_repositori.py
│   └── categoria_repositori.py
│
├── services/
│   ├── contacto_services.py
│   ├── archivo_services.py
│   └── exceptions.py
│
├── sql/
│   └── skillchallengefinal.sql
│
├── data/
│   └── auditoria.json
│
└── reportes/
    └── contactos.csv
```

### Capas

#### Models

Contiene las clases que representan las entidades del sistema.

`Contacto` utiliza `dataclass` para representar los datos de un contacto.

#### Repositories

Contiene la comunicación con MySQL y las operaciones de persistencia.

Los repositorios se encargan de ejecutar consultas SQL para crear, consultar,
actualizar y eliminar registros.

#### Services

Contiene la lógica de negocio de la aplicación.

Aquí se encuentran las validaciones, selección de categorías, reglas de negocio
y manejo de las operaciones del sistema.

#### Main

`main.py` es el punto de entrada de la aplicación y contiene el menú de
interacción con el usuario.

## Base de datos

La aplicación utiliza MySQL para la persistencia de información.

La base de datos contiene principalmente las tablas:

- `contactos`
- `categorias`

Existe una relación de uno a muchos entre categorías y contactos:

```text
categorias
    │
    │ 1
    │
    └──────── N
             contactos
```

Cada contacto contiene una llave foránea `id_categoria` que referencia a la
categoría correspondiente.

También se utiliza un `INNER JOIN` para mostrar los contactos junto con el
nombre de su categoría.

El script completo de creación de la base de datos se encuentra en:

```text
sql/skillchallengefinal.sql
```

## Configuración

La conexión a MySQL utiliza variables de entorno mediante un archivo `.env`.

Crear un archivo `.env` en la raíz del proyecto:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=skillchallengefinal
```

Los valores deben sustituirse por las credenciales correspondientes al entorno
local.

**No subir el archivo `.env` a GitHub.**

El archivo `.gitignore` del proyecto está configurado para ignorarlo.

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/kurokamisoul/SkillChallengeFinal.git
```

Entrar al proyecto:

```bash
cd SkillChallengeFinal
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración de la base de datos

1. Abrir MySQL.
2. Ejecutar el script:

```text
sql/skillchallengefinal.sql
```

3. Crear el archivo `.env` con las credenciales de conexión.
4. Verificar que MySQL esté disponible.

## Ejecución

Desde la raíz del proyecto ejecutar:

```bash
python main.py
```

Se mostrará el menú principal:

```text
MENU DE CONTACTOS

1. Agregar
2. Ver
3. Actualizar
4. Eliminar
5. Salir
6. Exportar contactos a CSV
```

## CRUD

### Crear

Permite registrar un nuevo contacto solicitando:

- Nombre.
- Teléfono.
- Email.
- Categoría.

El sistema genera automáticamente el identificador y la fecha de creación
desde la base de datos.

### Leer

Muestra los contactos activos y utiliza un `JOIN` con la tabla de categorías
para mostrar el nombre de la categoría.

### Actualizar

Permite modificar los datos de un contacto existente y seleccionar una nueva
categoría.

### Eliminar

El contacto no se elimina físicamente de la base de datos. Se realiza una
eliminación lógica mediante el campo `activo`.

## Reglas de negocio

El proyecto implementa reglas de negocio más allá de la validación de campos
vacíos.

Entre ellas:

- El teléfono debe contener exactamente 10 caracteres numéricos.
- El correo debe tener un formato básico válido.
- No se permite registrar un correo electrónico que ya exista.
- La categoría seleccionada debe existir en la base de datos.
- Los contactos eliminados lógicamente no aparecen en el listado normal.

La regla de correo duplicado se maneja mediante la excepción propia:

```text
RegistroDuplicadoError
```

## Manejo de excepciones

El proyecto utiliza excepciones específicas para evitar que la aplicación se
cierre inesperadamente.

Se utiliza una excepción propia:

```python
class RegistroDuplicadoError(Exception):
    pass
```

Las excepciones se generan en la capa correspondiente y se capturan en
`main.py`, donde se muestran mensajes comprensibles para el usuario.

También se manejan errores específicos relacionados con MySQL y operaciones
de archivos.

## Auditoría JSON

Las operaciones realizadas sobre los contactos se registran en:

```text
data/auditoria.json
```

Se registran operaciones como:

```text
CREATE
UPDATE
DELETE
```

Cada registro contiene la operación, el ID del contacto y la fecha en que se
realizó.

## Exportación CSV

La opción:

```text
6. Exportar contactos a CSV
```

genera:

```text
reportes/contactos.csv
```

El archivo contiene el listado completo de contactos junto con su categoría y
puede abrirse utilizando Excel u otra aplicación compatible con CSV.

## Git

El desarrollo del proyecto se realizó mediante ramas de funcionalidad para
separar diferentes etapas de implementación.

Entre las funcionalidades desarrolladas se encuentran:

- Manejo de excepciones.
- Auditoría.
- Exportación de reportes.

También se realizó la resolución de un conflicto real durante la integración
de cambios entre ramas.

El conflicto y su resolución se documentan en:

```text
CONFLICTOS.md
```

## Seguridad

Las credenciales de la base de datos se almacenan mediante variables de
entorno y el archivo `.env` está excluido del repositorio mediante `.gitignore`.

No se deben colocar contraseñas u otras credenciales directamente en el código
fuente.

## Autor

Proyecto desarrollado por Miguel Angel Mtz. Chávez como parte del Skill
Challenge.
