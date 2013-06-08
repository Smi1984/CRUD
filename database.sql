-- Borra la base de datos si existe
DROP DATABASE IF EXISTS DBCrud;

-- Crea la base de datos
CREATE DATABASE DBCrud;

-- Usuario para la conexión
GRANT ALL ON DBCrud.* TO 'crud'@'localhost' IDENTIFIED BY 'cruduser';

-- Creación de la tabla
USE DBCrud;
CREATE TABLE ships (id INT,Clase VARCHAR(100),Crew INT,Longi INT, Anch INT, Alt INT);

-- Algunos datos para pruebas


--insert into .... values ....;

INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (1,"Intrepid",270,342,144,55);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (2,"Olympic",320,276,90,100);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (3,"Excelsior",750,511,195,88);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (4,"Nebula",750,442,318,130);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (5,"Defiant",50,170,134,30);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (6,"Constitution",430,289,130,73);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (7,"Prometheus",175,415,163,64);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (8,"New Orleans",300,350,300,100);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (9,"Norway",190,364,225,52);
INSERT INTO ships (id, Clase, Crew, Longi, Anch, Alt) VALUES (10,"Constellation",520,275,150,65);

