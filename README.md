# Page Rank

Este proyecto está destinado a aprender cómo se utiliza el algoritmo de Page Rank de Google para realizar búsquedas.

El mismo busca imita a alto nivel, la arquitectura de Google.


## Búsquedas

Para buscar en la web simulando la búsqueda de Google todo lo que se necesita para poder ejecutar el proyecto es un archivo con extensión json que contenga un conjunto de urls entre las que se quiera simular la web que luego Google analizará.

El archivo debe tener el siguiente formato:

```
{
    "0": { "url": "http://www.a.com" },
    "1": { "url": "http://www.b.com" },
    "2": { "url": "http://www.c.com" }
}
```

Luego, se deberá ejecutar el script `search.py` con el siguiente comando, donde archivo_de_urls es el archivo descripto previamente:

`python search.py archivo_de_urls tipo_de_busqueda`

Una vez ejecutado, el script tratará de buscar el contenido html de cada una de las páginas provistas y generará un nuevo archivo (`archivo_de_urls.content`) almacenando el contenido de las mismas (en un campo `content`) para, en caso de correr nuevamente el script con ese archivo, no tener que obtener el contenido nuevamente en caso de que se lo quiera ejecutar devuelta.

Después de obtener el contenido se procederá a armar el grafo de la web provista y a hallar el ranking de cada página utilizando el algoritmo de PageRank. También en este caso se generará un nuevo archivo (`archivo_de_urls.page_rank`), con un campo `page_rank` para cada página.

Por último, una vez que se haya configurado correctamente la web, se permitirá al usuario realizar las búsquedas que desee, mostrando por pantalla las urls que coinciden con cada búsqueda realizada y ordenadas según su page rank.

`tipo_de_busqueda` especifica si se desea ejecutar las búsquedas para que busque por título (`title`) o por contenido (`content`). El parámetro no es necesario. Por defecto busca por contenido


### Archivos de Prueba

Dentro de la carpeta `example_files` se podrán encontrar ejemplos básicos de los archivos mencionados, con algunas urls de prueba con contenidos establecidos, de forma tal que se pueda ver las estructuras de los archivos e interacturar con ellos.

Dentro de la carpeta `california_files` se podrán encontrar algunos ejemplos de archivos con mayor cantidad de urls.

Se recomienda comenzar ejecutando el archivo `urls_maps.json` dentro de la carpeta `example_files`

_En particular el archivo original-file-california.txt fue extraido de la siguiente página web: http://www.cs.cornell.edu/courses/cs685/2002fa/_


Los comandos típicos para ejecutar los archivos actuales son:

`python search.py example_files/urls_maps.json` o `python search.py example_files/urls_maps.json.page_rank` que ya posee todos los page rank cargados

`python search.py california_files/little_urls_map.json` o `python search.py california_files/little_urls_map.json.page_rank` que ya posee todos los page rank cargados

`python search.py california_files/original_urls_maps.json` (tardará ~30 min en cargarlo) o `python search.py california_files/original_urls_maps.json.page_rank` que ya posee todos los page rank cargados


_Aclaración:_ por el momento, en el caso de proveer un archivo con muchas urls (> 10000), si muchas de ellas no son encontradas, el programa puede que demore un tiempo considerable (alrededor de los 30 minutos o más, dependiendo de la computadora utilizada).


## Algoritmo de Page Rank

También este proyecto provee un script para ejecutar el algoritmo de PageRank y poder analizar cómo funciona el mismo.

Para ello es necesario proveer un archivo que represente a un grafo de la web. Debe tener definidas la cantidad de nodos (páginas) que se utilizarán (será la primera línea del archivo) y luego las siguientes líneas las aristas que las interconectan (si es del nodo i al j)

El archivo debe tener una estructura similar a la siguiente (1000000 nodos):

```
1000000
0	867923
0	891835
11342	0
11342	27469
824020	38716
11342	309564
891835	322178
```

Luego se debe ejecutar el siguiente comando:

`python page_rank.py nombre_del_archivo tipo_de_convergencia cantidad_nodos`

y el resultado consistirá en otros dos archivos. Uno llamado `nombre_del_archivo.matrix.json` que contendrá una matriz de Markov preparada para hallar luego el page_rank de cada página. El otro llamado `nombre_del_archivo.page_rank.json` que contendrá un vector, donde cada valor representará el page rank de cada página, siguiendo las posiciones de los nodos dadas.

Los parámetros `tipo_de_convergencia` y `cantidad_nodos` son opcionales y sus valores por defecto son: `matrix` para el primer parámetro y 2000 para el segundo.
En el caso de `tipo_de_convergencia` los tipos permitidos son: `matrix` `random` y `eigen`.

`matrix:` halla la convergencia de la matriz de probabilidades en n pasos a través de la multiplicación de la matriz sobre si misma.

`random:` halla la convergencia de la matriz de probabilidades en n pasos a través de navegar sobre todo el grafo de la web de manera random siguiendo las probabilidades de cada arista.

`eigen:` halla la convergencia de la matriz de probabilidades en n pasos a través de la multiplicación de la matriz diagonal D de autovalores sobre si misma y luego ejecuta la siguiente operacion E.Dn.E-1 donde E es la matriz de autovectores posicionados en columnas y Dn el resultado de multiplicar D n veces.

_Aclaración_: dentro del script está establecido que el máximo de nodos que se leerán son 2000, dado que ya con esta cantidad consume 100% de CPU y aproximadamente 2 GB de memoria. En el caso de que se desee ejecutar con más nodos, solo hay que completar el parámetro opcional `cantidad_nodos`


### Archivos de Prueba

Dentro de la carpeta `page_rank_files` se podrán encontrar ejemplos básicos de los archivos mencionados, con algunas matrices de prueba, de forma tal que se pueda ver las estructuras de los archivos e interacturar con ellos.
Se recomienda comenzar ejecutando el archivo `basic_graph.txt`

_En particular los archivos epa_graph.txt y notre_dam_graph.txt fueron extraidos de las siguiente páginas: http://snap.stanford.edu/data/ y http://networkrepository.com/web.php, donde también se pueden encontrar otros sets de datos_

Los comandos típicos para ejecutar los archivos actuales son:

`python page_rank.py page_rank_files/basic_graph.txt`

`python page_rank.py page_rank_files/epa_graph.txt`

`python page_rank.py page_rank_files/notre_dam_graph.txt`


## Tests

Para ejecutar los tests, en el directorio `tests` se debe ejecutar el siguiente comando:

`python tests.py`


## Bibliotecas necesarias para ejecutar el proyecto

Se necesita tener `python 2.7` instalado: https://www.python.org/download/releases/2.7/

Luego se necesitan tener instaladas estas bibliotecas de python (que pueden instalarse utilizando el comando `pip install nombre_biblioteca` https://www.makeuseof.com/tag/install-pip-for-python/)

`numpy`
`requests`
`copy`
`re`
`json`
`futures`
`BeautifulSoup`


## Mejoras

1. _Experiencia en las búsquedas:_ se podrían mejorar las búsquedas que se realizan en las páginas; por ejemplo, mejorando el parseo del html de las páginas para analizar su contenido, en lugar de buscar que las frases se encuentren dentro de todo el html de la misma, sin separar entre las palabras del contenido.

2. _Flexibilidad:_ se podría mejorar aún más la flexibilidad de los scripts provistos para, por ejemplo, recibir por parámetros el número de iteraciones de PageRank que se desea calcular u otros de configurabilidad del sistema

3. _Obtención de páginas web:_ también se puede mejorar la obtención de páginas web a través de internet, para hacer la misma más rápida y optimizando la cantidad de páginas obtenidas correctamente

4. _Memoria consumida:_ dado que la aplicación carga los archivos junto con su contenido en memoria, esto puede llegar a ser una limitación si se desean realizar pruebas con sets de datos muy grandes. Se puede optimizar utilizando más memoria o simplemente guardar el contenido de las páginas en alguna base de datos externa o en disco (aunque sea una manera más lenta) 

5. _Performance:_ si bien el proyecto es solo para mostrar cómo funciona el buscador de Google en base a PageRank, el mismo podría ser más eficiente aún sin cambiar de lenguaje de programación (C por ejemplo). En particular se podrían mejorar las operaciones con matrices (por ejemplo cuando la matriz es demasiado grande (dim > 1500) la multiplicación de la misma falla utilizando autovalores y autovectores. Dada la similitud en perforce entre las dos maneras de multiplicar matrices se ha decidido no utilizar este caso por defecto)
