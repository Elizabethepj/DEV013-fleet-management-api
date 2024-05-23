# Fleet Management Software API

## Índice

* [1. Preámbulo](#1-preámbulo)
* [2. Resumen del proyecto](#2-resumen-del-proyecto)
* [3. Objetivos de aprendizaje](#3-objetivos-de-aprendizaje)
* [4. Consideraciones generales](#4-consideraciones-generales)
* [5. Criterios de aceptación del proyecto](#5-criterios-de-aceptación-del-proyecto)
* [6. Stack de tecnologías](#6-stack-de-tecnologías)
* [7. Pistas, tips y lecturas complementarias](#7-pistas-tips-y-lecturas-complementarias)


***

## 1. Preámbulo

La internet de las cosas (IoT, por sus siglas en inglés)​ 
se refiere a una interconexión digital de objetos cotidianos con internet.
Esta conexión ha constituido un cambio importante en la vida de las personas
y en la sociedad en general. La disponibilidad de la información ha permitido
desarrollar procesos de sistematización y control útiles para la organizzación de
la vida diaria en ámbitos como la salud, la educación y el transporte, entre otros.

En el caso del transporte la internet de las cosas permite hacer seguimiento a
cada uno de los vehículos en aspectos como la ubicación, condiciones, 
daños y otras eventualidades.

![zach-vessels-utMdPdGDc8M-unsplash](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fthumb.jpg?alt=media)

Además, de los beneficios la IoT también genera grandes retos
relacionados con el almacenamiento, análisis y visualización de
la información. 
Se calcula que para el 2025 los dispositivos IoT generen
[79.4 zettabytes](https://www.statista.com/statistics/1017863/worldwide-iot-connected-devices-data-size/)
(1 zettabyte equivale a 1 trillón de gigabytes).


## 2. Resumen del proyecto

En este proyecto se construyó una API REST de un
[Fleet Management Software]
para consultar las ubicaciones de los vehículos de una empresa
de taxis en Beijing, China.

## 3. Objetivos de aprendizaje

Los objetivos de aprendizaje alcanzados en el desarrollo de este proyecto fueron los siguientes:

### Python

- [x] **Variables (declaración, asignación, ámbito)**

  <details><summary>Links</summary><p>

  * [Variables in Python – Real Python (en inglés)](https://realpython.com/python-variables/)
  * [Variables in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/python-variables/)
</p></details>

- [x] **Uso de condicionales (if, elif, ternario)**

  <details><summary>Links</summary><p>

  * [Conditional Statements in Python – Real Python (en inglés)](https://realpython.com/python-conditional-statements/)
</p></details>

- [x] **Operadores (identidad, aritméticos, comparación etc)**

  <details><summary>Links</summary><p>

  * [Python Operators - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/python-operators/)
</p></details>

- [x] **Docstrings (y su diferencia de comentarios)**

  <details><summary>Links</summary><p>

  * [Docstrings - Python Docs (en inglés)](https://docs.python.org/3/tutorial/controlflow.html#documentation-strings)
</p></details>

- [x] **Linting (pylint)**

  <details><summary>Links</summary><p>

  * [Pylint - Documentación oficial](https://pylint.pycqa.org/en/latest/)
  * [Linting Python in Visual Studio Code - Visual Studio Code Docs (en inglés)](https://code.visualstudio.com/docs/python/linting)
</p></details>

- [x] **Serialización (y deserialización)**

  <details><summary>Links</summary><p>

  * [Serialize Your Data With Python – Real Python (en inglés)](https://realpython.com/python-serialize-data/)
</p></details>

#### Tipos de datos

- [x] **Tipos de datos primitivos (int, float, str, bool)**

  <details><summary>Links</summary><p>

  * [Data Types - Python Docs (en inglés)](https://docs.python.org/3/library/datatypes.html)
  * [Data types in Python (en inglés)](https://www.educative.io/answers/data-types-in-python)
</p></details>

- [x] **Listas (arrays)**

  <details><summary>Links</summary><p>

  * [Lists - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
  * [Lists and Tuples in Python - Real Python (en inglés)](https://realpython.com/python-lists-tuples/)
</p></details>

- [x] **Tuples**

  <details><summary>Links</summary><p>

  * [Tuples - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
  * [Lists and Tuples in Python - Real Python (en inglés)](https://realpython.com/python-lists-tuples/)
</p></details>

- [x] **Dictionaries (Dicts)**

  <details><summary>Links</summary><p>

  * [Dictionaries - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  * [Dictionaries in Python - Real Python (en inglés)](https://realpython.com/python-dicts/)
</p></details>

- [x] **Sets**

  <details><summary>Links</summary><p>

  * [Sets - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#sets)
  * [Sets in Python - Real Python (en inglés)](https://realpython.com/python-sets/)
</p></details>

#### Funciones

- [x] **Conceptos basicos (params, args, default values, return)**

  <details><summary>Links</summary><p>

  * [Python Functions - GeeksforGeeks (en ingles)](https://www.geeksforgeeks.org/python-functions/)
</p></details>

- [x] ***args y **kwargs**

  <details><summary>Links</summary><p>

  * [*args and **kwargs in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/args-kwargs-python/)
</p></details>

- [x] **Cierres (closures)**

  <details><summary>Links</summary><p>

  * [Closures - Python Docs (en inglés)](https://docs.python.org/3/reference/datamodel.html#emulating-closures-and-nested-scope)
</p></details>

- [x] **Funciones lambda**

  <details><summary>Links</summary><p>

  * [Lambda Functions - Python Docs (en inglés)](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
  * [How to Use Python Lambda Functions – Real Python (en inglés)](https://realpython.com/python-lambda/)
</p></details>

- [x] **Decoradores**

  <details><summary>Links</summary><p>

  * [Decorators - Python Docs (en inglés)](https://docs.python.org/3/glossary.html#term-decorator)
  * [Decorators in Python - Geeks for Geeks (en inglés)](https://www.geeksforgeeks.org/decorators-in-python/)
</p></details>

#### Iteración

- [x] **Uso de bucles/ciclos (while, for..in)**

  <details><summary>Links</summary><p>

  * [Loops in Python - For, While and Nested Loops - GeeksforGeeks](https://www.geeksforgeeks.org/loops-in-python/)
  * [Loops - Learn Python - Free Interactive Python Tutorial](https://www.learnpython.org/en/Loops)
</p></details>

- [x] **Comprensión de listas**

  <details><summary>Links</summary><p>

  * [List Comprehension - Python Docs (en inglés)](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
  * [List Comprehension in Python - GeeksforGeeks (en inglés)](https://www.geeksforgeeks.org/list-comprehensions-in-python/)
  * [When to Use a List Comprehension in Python – Real Python (en inglés)](https://realpython.com/list-comprehension-python/)
</p></details>

- [x] **Técnicas funcionales (map, filter, reduce)**

  <details><summary>Links</summary><p>

  * [Our Guide to Map, Filter, and Reduce Functions in Python - Udacity (en inglés)](https://www.udacity.com/blog/2020/12/our-guide-to-map-filter-and-reduce-functions-in-python.html)
  * [Map, Filter, Reduce - Learn Python - Free Interactive Python Tutorial (en inglés)](https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce)
</p></details>

#### Testing en Python

- [x] **Pruebas unitarias (unit tests, unittest, pytest)**

  <details><summary>Links</summary><p>

  * [unittest - Python Docs (en inglés)](https://docs.python.org/3/library/unittest.html)
  * [pytest - Documentación oficial](https://docs.pytest.org/en/6.2.x/)
</p></details>

- [x] **Uso de mocks (y patch)**

  <details><summary>Links</summary><p>

  * [unittest.mock - Python Docs (en inglés)](https://docs.python.org/3/library/unittest.mock.html)
  * [Python Mock Library - Real Python (en inglés)](https://realpython.com/python-mock-library/)
</p></details>

- [x] **Uso de fixtures**

  <details><summary>Links</summary><p>

  * [pytest fixtures - Documentación oficial](https://docs.pytest.org/en/6.2.x/fixture.html)
</p></details>

#### Modularización

- [x] **Módulos**

  <details><summary>Links</summary><p>

  * [Módulos - Python Docs (en inglés)](https://docs.python.org/3/tutorial/modules.html)
</p></details>

- [x] **Paquetes**

  <details><summary>Links</summary><p>

  * [Paquetes - Python Docs (en inglés)](https://docs.python.org/3/tutorial/modules.html#packages)
</p></details>

#### Manejo de dependencias

- [x] **pip (instalación y uso de paquetes)**

  <details><summary>Links</summary><p>

  * [pip - Python Docs (en inglés)](https://docs.python.org/3/installing/index.html)
</p></details>

- [x] **Virtual Environment (ambientes virtuales, virtualenv)**

  <details><summary>Links</summary><p>

  * [venv — Creation of virtual environments — Python 3.12.2 documentation (en inglés)](https://docs.python.org/3/library/venv.html)
  * [Python Virtual Environments: A Primer – Real Python (en inglés)](https://realpython.com/python-virtual-environments-a-primer/)
</p></details>

- [x] **requirements.txt**

  <details><summary>Links</summary><p>

  * [requirements.txt - Documentación oficial](https://pip.pypa.io/en/stable/user_guide/#requirements-files)
</p></details>

#### Flask

##### Rutas _(Flask)_

- [x] **Decorador de ruta**

  <details><summary>Links</summary><p>

  * [Routing - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing)
</p></details>

- [x] **Función de vista**

  <details><summary>Links</summary><p>

  * [View Functions - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#view-functions)
</p></details>

- [x] **Reglas de variables (urls dinamica)**

  <details><summary>Links</summary><p>

  * [Variable Rules - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#variable-rules)
</p></details>

##### Request Object _(Flask)_

- [x] **Argumentos**

  <details><summary>Links</summary><p>

  * [Request - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
</p></details>

- [x] **Headers (cabeceras)**

  <details><summary>Links</summary><p>

  * [Request - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
</p></details>

##### Response Object _(Flask)_

- [x] **Partes de la respuesta (status, body, headers)**

  <details><summary>Links</summary><p>

  * [Response - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/quickstart/#about-responses)
</p></details>

- [x] **jsonify**

  <details><summary>Links</summary><p>

  * [jsonify - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/api/#flask.json.jsonify)
</p></details>

##### Testing en Flask _(Flask)_

- [x] **Configuración de fixtures**

  <details><summary>Links</summary><p>

  * [Testing - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/testing/#fixtures)
</p></details>

- [x] **Test Client**

  <details><summary>Links</summary><p>

  * [Testing - Flask Docs (en inglés)](https://flask.palletsprojects.com/en/3.0.x/testing/#sending-requests-with-the-test-client)
</p></details>


##### Configuración _(Django)_

- [ ] **Migraciones**

  <details><summary>Links</summary><p>

  * [Migraciones](https://docs.djangoproject.com/es/5.0/topics/migrations/#module-django.db.migrations)
</p></details>

- [ ] **Setup app**

  <details><summary>Links</summary><p>

  * [Installed apps](https://docs.djangoproject.com/es/5.0/ref/settings/#std-setting-INSTALLED_APPS)
</p></details>

##### Modelos _(Django)_

- [ ] **Fields**

  <details><summary>Links</summary><p>

  * [Field types](https://docs.djangoproject.com/en/5.0/topics/db/models/#Fields)
</p></details>

- [x] **Foreign Key**

  <details><summary>Links</summary><p>

  * [Model field reference](https://docs.djangoproject.com/en/5.0/ref/models/fields/)
</p></details>

##### Rest Framework _(Django)_

- [x] **Serializers**

  <details><summary>Links</summary><p>

  * [Serializers](https://www.django-rest-framework.org/community/third-party-packages/#serializers)
</p></details>

- [x] **Pagination**

  <details><summary>Links</summary><p>

  * [Pagination](https://www.django-rest-framework.org/api-guide/pagination/#pagination)
</p></details>

- [x] **Query params**

  <details><summary>Links</summary><p>

  * [query_params](https://www.django-rest-framework.org/api-guide/requests/#query_params)
</p></details>

- [ ] **ViewSet**

  <details><summary>Links</summary><p>

  * [ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/#viewset)
</p></details>

- [ ] **Apiview**

  <details><summary>Links</summary><p>

  * [GenericAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
</p></details>

### Programación Orientada a Objetos (OOP)

- [x] **Clases**

- [x] **Objetos**

- [x] **Métodos**

- [x] **Constructores**


### SQL

- [x] **Creación y modificación de tablas**

  <details><summary>Links</summary><p>

  * [SQL CREATE TABLE Statement - w3schools (en inglés)](https://www.w3schools.com/sql/sql_create_table.asp)
  * [CREATE TABLE Statement - PostgreSQL Docs (en inglés)](https://www.postgresql.org/docs/9.1/sql-createtable.html)
  * [ALTER TABLE Statement - PostgreSQL Docs (en inglés)](https://www.postgresql.org/docs/9.1/sql-altertable.html)
</p></details>

- [x] **Operaciones CRUD (Create-Read-Update-Delete)**

  <details><summary>Links</summary><p>

  * [INSERT](https://www.postgresql.org/docs/9.5/sql-insert.html)
  * [SELECT](https://www.postgresql.org/docs/9.5/sql-select.html)
  * [UPDATE](https://www.postgresql.org/docs/9.1/sql-update.html)
  * [DELETE](https://www.postgresql.org/docs/8.1/sql-delete.html)
</p></details>

- [ ] **Borrado de tablas o bases de datos enteras con DROP**

  <details><summary>Links</summary><p>

  * [DROP TABLE](https://www.postgresql.org/docs/8.2/sql-droptable.html)
  * [DROP DATABASE](https://www.postgresql.org/docs/8.2/sql-dropdatabase.html)
</p></details>

### Bases de datos

- [x] **Modelado de datos**

- [x] **Conexión**

- [ ] **Índices y limitaciones**

### PostgreSQL

- [ ] **Tipos de datos**

  <details><summary>Links</summary><p>

  * [Chapter 8. Data Types - Docs (en inglés)](https://www.postgresql.org/docs/14/datatype.html)
</p></details>

- [ ] **Índices**

  <details><summary>Links</summary><p>

  * [Chapter 11. Indexes - Docs (en inglés)](https://www.postgresql.org/docs/14/indexes.html)
</p></details>

## 4. Consideraciones generales

* Este proyecto se desarrollo en 5 sprints por la desarrolladora Elizabeth Patiño. 


## 5. Criterios de cumplimiento del proyecto

Nuestra cliente ha instalado dispositivos GPS en sus taxis.
Estos dispositivos utilizan señales satelitales para determinar
con precisión las coordenadas geográficas del taxi.

Nuestra clienta requiere:

1. Cargar la información de archivos SQL a una
base de datos Postgresql.
2. Desarrollar una API REST que permita consultar, mediante
peticiones HTTP, la información almancenada en la base de datos.

### Definición del producto

El [_Product Owner_](https://www.youtube.com/watch?v=r2hU7MVIzxs&t=202s)
nos presenta este _backlog_ que es el resultado de su trabajo con la clienta
hasta hoy.

***

#### [Historia de usuario 1] Cargar información a base de datos

Yo, como desarrolladora, quiero cargar la información almacenada hasta ahora en
[archivos sql](https://drive.google.com/file/d/1T5m6Vzl9hbD75E9fGnjbOiG2UYINSmLx/view?usp=drive_link)
en una base de datos PostgreSQL, para facilitar su consulta y análisis.

##### Criterios de aceptación

* Se debe tener en cuenta el siguiente diagrama para la implementación de las
relaciones entre las tablas

![mer](https://firebasestorage.googleapis.com/v0/b/laboratoria-945ea.appspot.com/o/fleet-management-api-java%2Fsql-diagram.png?alt=media)

* La tabla de _trajectories_ se debe crear con el "id" que se incremente
automáticamente (SERIAL) para poder insertar los valores sin necesidad
de especificar un identificador

##### Definición de terminado

* La base de datos tiene creada la tabla de taxis
* La tabla de taxis tiene cargada la data de taxis
* La base de datos tiene creada la tabla de trayectorias
* La tabla de taxis tiene cargada la data de trayectorias

***

##### [Historia de usuario 2] Endpoint listado de taxis

Yo como clienta de la API REST requiero un _endpoint_ para
listar todos los taxis.

##### Criterios de aceptación

* El _endpoint_ responde para cada taxi: id y placa.
* El _endpoint_ tiene paginación de los resultados para asegurar que las
respuestas sean más fáciles de manejar.

##### Contenido

* Se cuenta con una documentación en [Swagger](https://swagger.io/)
para el _endpoint_ desarrollado especificando
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parámetros,
[encabezados](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de respuesta](https://shorturl.at/bdegB)
y
[cuerpo](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages).
* El código del _endpoint_ recibió _code review_ de al
menos una compañera.
* El código _endpoint_ está cargado en un repositorio de Github.
* El código _endpoint_ tiene con test unitarios y e2e.

***

#### [Historia de usuario 3] Endpoint historial de ubicaciones

Yo como clienta de la API REST requiero un _endpoint_ para
consultar todas las ubicaciones de un taxi dado el id y una fecha.

##### Criterios de aceptación

* El _endpoint_ responde con el id del taxi y una fecha mostrando
  la siguiente información: latitud, longitud y timestamp (fecha y hora).
* El _endpoint_ tiene paginados los resultados para asegurar que las
  respuestas sean más fáciles de manejar.

##### Definición de terminado

* Se cuenta con una documentación en [Swagger](https://swagger.io/)
para el _endpoint_ desarrollado especificando
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parámetros,
[encabezados](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de respuesta](https://shorturl.at/bdegB)
y
[cuerpo](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages).
* El código del _endpoint_ debe recibir _code review_ de al
menos una compañera.
* El código _endpoint_ está cargado en un repositorio de Github.
* El código _endpoint_ cuenta con test unitarios y e2e.

***

#### [Historia de usuario 4] Endpoint última ubicación

Yo como clienta de la API REST requiero un _endpoint_ para
consultar la última ubicación reportada por cada taxi.

##### Criterios de aceptación

* El _endpoint_ responde para cada taxi la siguiente información:
id, placa, latitud, longitud y timestamp (fecha y hora).
* El _endpoint_ tiene paginados los resultados para asegurar que las
respuestas sean más fáciles de manejar.

##### Definición de terminado

* Se cuenta con una documentación en [Swagger](https://swagger.io/)
para el _endpoint_ desarrollado especificando
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parámetros,
[encabezados](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de respuesta](https://shorturl.at/bdegB)
y
[cuerpo](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages).
* El código del _endpoint_ debe recibir _code review_ de al
menos una compañera.
* El código _endpoint_ está cargado en un repositorio de Github.
* El código _endpoint_ cuenta con test unitarios y e2e.

***

## 6. Stack de tecnologías

* [Python](./docs/stack-python.md)

## 7. Pistas, tips y lecturas complementarias

### Modelamiento de datos

Se uso PostgreSQL y  [vercel Postgresql](https://vercel.com/docs/storage/vercel-postgres).

### Definir endpoints de API

Se definieron y documentaron los endpoints de tu API.
Debes usar [Swagger](https://swagger.io/) para esto.

Para una API REST en cada endpoint se establecieron entre otras cosas el
[método HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods),
url, parámetros,
[encabezados](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers),
[códigos HTTP de respuesta](https://shorturl.at/bdegB)
y
[cuerpo](https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages).


