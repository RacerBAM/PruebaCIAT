# Enunciado de la Prueba

La Alianza de Bioversity International y el Centro Internacional de Agricultura Tropical (CIAT) brindan soluciones científicas que aprovechan la biodiversidad agrícola y transforman los sistemas alimentarios de manera sostenible para mejorar la vida de las personas. Las soluciones de la Alianza abordan las crisis mundiales de malnutrición, cambio climático, pérdida de la biodiversidad y degradación ambiental.

Colombia es uno de los países que ha firmado el acuerdo de París (COP21: la 21ª Conferencia de las Partes de la Convención de Naciones Unidas sobre Cambio Climático). La Alianza de Bioversity International y el Centro Internacional de Agricultura Tropical (CIAT) desean apoyar al gobierno Colombiano en este acuerdo, trabajando en uno de los temas más importantes en torno al cambio climático: La ganadería y la deforestación, por lo cual te han convocado a ti, para que juntos trabajemos por un mejor mundo.

El gobierno y CIAT desean desarrollar un sistema que permita realizar la trazabilidad de ganado, permitiendo identificar cuáles animales provienen de zonas en las cuales se está deforestando el bosque con el fin de sembrar pastos para los animales. Usted puede suponer que ya se cuenta con las siguientes bases de datos debidamente pobladas:
- Ubicación de los animales (latitud, longitud, propietario de los animales)
- Zonas de deforestación (latitud, longitud, área de deforestación o cambio de cobertura)

Con esta información el gobierno quiere poder identificar el ganado que está en zonas de riesgo de deforestación y realizar campañas pedagogicas para evitar la tala de los árboles e implementar otras soluciones. Su misión es la de diseñar un sistema de información que ayude a identificar que animales se encuentran en dichas zonas de deforestación y cuales no lo están. No existen restricciones de tecnologias a usar, pero se desea que la solución se encuentre en una imagen de Docker para su rápido despliegue.

Como entregables se solicita lo siguiente:
- Lista de requerimientos debidamente clasificados
- **Sistema de información que ayude a la solución**

Opcionales:
- Despligue en Docker
- Arquitectura del sistema

Los requisitos anteriores deben estar contenidos en un repositorio de GitHub.

## Requisitos Funcionales

Los Requisitos Funcionales que identifique a partir del enunciado son:
- El sistema necesita leer informacion de las bases de datos de Ubicacion y Zonas
- El sistema debe identificar los animales ubicadas en zonas de deforestacion, comparando las ubciaciones de las 2 bases de datos para encontrar coincidencias


## Requisitos No Funcionales

Los Requisitos No Funcionales que identifique a partir del enunciado son:
- Un nivel de interoperabilidad: Idealmente, deberia poderse desplegar con Docker.
- Un nivel de Portabilidad: Ademas de ser compatible con Docker, la prueba se debe desarrollar sobre un repositorio GitHub.
- Costo cero: Se desea un rapido despliegue donde yo entrego un sistema ya listo.

## Restricciones
   
No se especificaron Restricciones en el documento (es mas, el documento dice que no hay restricciones de tecnologias a usar). No hay presupuesto, pues es una prueba, por lo que Costo Cero seria la unica restriccion tecnicamente.

## Requisitos de Interfaz de Usuario

No se habla sobre la interfaz an el documento, entonces esta seccion tampoco aplica. Para el sistema, habra una interfaz muy sencilla por terminal con impresiones e inputs.