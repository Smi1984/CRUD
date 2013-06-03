-- Borra la base de datos si existe
DROP DATABASE IF EXISTS DBCrud;

-- Crea la base de datos
CREATE DATABASE DBCrud;

-- Usuario para la conexión
GRANT ALL ON DBCrud.* TO 'crud'@'localhost' IDENTIFIED BY 'cruduser';

-- Creación de la tabla
USE DBCrud;
create table ....;

-- Algunos datos para pruebas
insert into .... values ....;
