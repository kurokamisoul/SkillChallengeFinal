-- ============================================================
-- SkillChallengeFinal
-- Base de datos para gestión de contactos
-- ============================================================


-- ============================================================
-- 1. CREACIÓN DE LA BASE DE DATOS
-- ============================================================

CREATE DATABASE IF NOT EXISTS skillchallengefinal
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_0900_ai_ci;


USE skillchallengefinal;


-- ============================================================
-- 2. ELIMINAR TABLAS SI EXISTEN
-- ============================================================
-- Se utiliza para poder ejecutar nuevamente el script
-- durante el desarrollo sin conflictos de llaves foráneas.
-- ============================================================

DROP TABLE IF EXISTS contactos;
DROP TABLE IF EXISTS categorias;


-- ============================================================
-- 3. TABLA: categorias
-- ============================================================

CREATE TABLE categorias (

    id_categoria INT UNSIGNED NOT NULL AUTO_INCREMENT,

    nombre VARCHAR(50) NOT NULL,

    descripcion VARCHAR(255),

    activo BOOLEAN NOT NULL DEFAULT TRUE,

    PRIMARY KEY (id_categoria),

    CONSTRAINT uk_categoria_nombre
        UNIQUE (nombre)

) ENGINE=InnoDB;


-- ============================================================
-- 4. TABLA: contactos
-- ============================================================

CREATE TABLE contactos (

    id INT UNSIGNED NOT NULL AUTO_INCREMENT,

    nombre_contacto VARCHAR(100) NOT NULL,

    telefono VARCHAR(10) NOT NULL,

    email VARCHAR(254) NOT NULL,

    activo BOOLEAN NOT NULL DEFAULT TRUE,

    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    id_categoria INT UNSIGNED NOT NULL,

    PRIMARY KEY (id),

    CONSTRAINT uk_contacto_email
        UNIQUE (email),

    CONSTRAINT fk_contacto_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
        ON UPDATE CASCADE
        ON DELETE RESTRICT

) ENGINE=InnoDB;


-- ============================================================
-- 5. ÍNDICES
-- ============================================================

CREATE INDEX idx_contactos_nombre
    ON contactos(nombre_contacto);

CREATE INDEX idx_contactos_categoria
    ON contactos(id_categoria);


-- ============================================================
-- 6. DATOS INICIALES DE CATEGORÍAS
-- ============================================================

INSERT INTO categorias (
    nombre,
    descripcion
)
VALUES
    (
        'Personal',
        'Contactos personales'
    ),
    (
        'Trabajo',
        'Contactos relacionados con trabajo'
    ),
    (
        'Familia',
        'Contactos familiares'
    ),
    (
        'Amigos',
        'Contactos de amigos'
    ),
    (
        'Otros',
        'Contactos que no pertenecen a otra categoría'
    );


-- ============================================================
-- 7. DATOS INICIALES DE CONTACTOS
-- ============================================================
-- Estos registros solamente sirven para comprobar que la BD,
-- las relaciones y los JOIN funcionan correctamente.
-- ============================================================

INSERT INTO contactos (
    nombre_contacto,
    telefono,
    email,
    id_categoria
)
VALUES
    (
        'Juan Perez',
        '4771234567',
        'juan.perez@example.com',
        1
    ),
    (
        'Maria Lopez',
        '4779876543',
        'maria.lopez@example.com',
        2
    ),
    (
        'Carlos Ramirez',
        '4774567890',
        'carlos.ramirez@example.com',
        3
    ),
    (
        'Ana Martinez',
        '4773216549',
        'ana.martinez@example.com',
        4
    );


-- ============================================================
-- 8. CONSULTA BÁSICA DE CONTACTOS
-- ============================================================

SELECT
    id,
    nombre_contacto,
    telefono,
    email,
    activo,
    fecha_creacion,
    id_categoria
FROM contactos
ORDER BY id;


-- ============================================================
-- 9. INNER JOIN
-- ============================================================
-- Muestra los contactos junto con el nombre de su categoría.
-- ============================================================

SELECT
    c.id,
    c.nombre_contacto,
    c.telefono,
    c.email,
    c.activo,
    c.fecha_creacion,
    cat.nombre AS categoria
FROM contactos AS c
INNER JOIN categorias AS cat
    ON c.id_categoria = cat.id_categoria
WHERE c.activo = TRUE
ORDER BY c.id;


-- ============================================================
-- 10. LEFT JOIN
-- ============================================================
-- Muestra todas las categorías aunque no tengan contactos.
-- ============================================================

SELECT
    cat.id_categoria,
    cat.nombre AS categoria,
    c.nombre_contacto,
    c.email
FROM categorias AS cat
LEFT JOIN contactos AS c
    ON cat.id_categoria = c.id_categoria
ORDER BY
    cat.nombre,
    c.nombre_contacto;


-- ============================================================
-- 11. CANTIDAD DE CONTACTOS POR CATEGORÍA
-- ============================================================

SELECT
    cat.id_categoria,
    cat.nombre AS categoria,
    COUNT(c.id) AS cantidad_contactos
FROM categorias AS cat
LEFT JOIN contactos AS c
    ON cat.id_categoria = c.id_categoria
    AND c.activo = TRUE
GROUP BY
    cat.id_categoria,
    cat.nombre
ORDER BY
    cantidad_contactos DESC;


-- ============================================================
-- 12. VERIFICACIÓN DE LA ESTRUCTURA
-- ============================================================

DESCRIBE categorias;

DESCRIBE contactos;


-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================