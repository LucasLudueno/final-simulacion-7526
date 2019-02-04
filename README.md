# Page Rank

Este proyecto está destinado a aprender cómo se utiliza el algoritmo de Page Rank de Google para realizar búsquedas.

El mismo busca imita a alto nivel, la arquitectura de Google.


## Búsquedas

Para buscar en la web, simulando la búsqueda de Google, todo lo que se necesita para poder ejecutar el proyecto es un archivo con extensión json que contenga un conjunto de urls entre las que se quiera simular la web que luego Google analizará.

El archivo debe tener el siguiente formato:

```
{
    "0": { "url": "http://www.a.com" },
    "1": { "url": "http://www.b.com" },
    "2": { "url": "http://www.c.com" }
}
```

Luego, se deberá ejecutar el script `main.py` con el siguiente comando, donde archivo_de_urls es el archivo descripto previamente:

`python main.py archivo_de_urls`

Una vez ejecutado, el script tratará de buscar el contenido html de cada una de las páginas provistas y generará un nuevo archivo (`archivo_de_urls.content`), almacenando el contenido de las mismas (en un campo `content`) para, en caso de correr nuevamente el script con ese archivo, no tener que obtener el contenido nuevamente

Después de obtener el contenido, se procederá a armar el grafo de la web provista, y a hallar el ranking de cada página utilizando el algoritmo de PageRank. También en este caso se generará un nuevo archivo (`archivo_de_urls.page_rank`), con un campo `page_rank` para cada página.

Por último, una vez que se haya configurado correctamente la web, se permitirá al usuario realizar las búsquedas que desee, mostrando por pantalla las urls que coinciden con cada búsqueda realizada y ordenadas según su page rank.


### Archivos de Prueba

Dentro de la carpeta `example_files` se podrán encontrar ejemplos básicos de los archivos mencionados, con algunas urls de prueba con contenidos establecidos, de forma tal que se pueda ver las estructuras de los archivos e interacturar con ellos.

Dentro de la carpeta `california_files` se podrán encontrar algunos ejemplos de archivos con mayor cantidad de urls.

Se recomienda comenzar ejecutando el archivo `urls_maps.json` dentro de la carpeta `example_files`

_En particular el archivo original-file-california.txt fue extraido de la siguiente página web: http://www.cs.cornell.edu/courses/cs685/2002fa/_


_Aclaración:_: por el momento, en el caso de proveer un archivo con muchas urls (> 10000), si muchas de ellas no son encontradas, el programa puede que demore un tiempo considerable (>30 minutos), sino el mismo ronda el orden de los minutos.


## Algoritmo de Page Rank

También este proyecto, provee un script para ejecutar el algoritmo de PageRank y poder analizar cómo funciona el mismo.

Para ello, es necesario proveer un archivo que represente a un grafo de la web. Debe tener definidas la cantidad de nodos (páginas) y aristas (referencias a otras páginas) que se utilizarán (serán la primera y la segunda línea del archivo respectivamente) y luego las siguientes líneas, las aristas que las interconectan (si fue del nodo i al j)

El archivo debe tener una estructura similar a la siguiente (1000000 nodos y 1300000 aristas):

```
1000000
1300000
0	867923
0	891835
11342	0
11342	27469
824020	38716
11342	309564
891835	322178
```

Luego se debe ejecutar el siguiente comando:

`python page_rank.py nombre_del_archivo`

y el resultado consistirá en otros dos archivos. Uno llamado `nombre_del_archivo.matrix.json` que contendrá una matriz de Markov preparada para hallar luego el page_rank de cada página. El otro llamado `nombre_del_archivo.page_rank.json` que contendrá un vector, donde cada valor representará el page rank de cada página, siguiendo las posiciones de los nodos dadas.

_Aclaración_: dentro del script está establecido que el máximo de nodos que se leerán son 3000, dado que con estos consume 100% de CPU y aproximadamente 2 GB de memoria. En el caso de que se desee ejecutar con más nodos, solo hay que modificar la constante: `DEFAULT_MATRIX_DIM` dentro del script


### Archivos de Prueba

Dentro de la carpeta `page_rank_files` se podrán encontrar ejemplos básicos de los archivos mencionados, con algunas matrices de prueba, de forma tal que se pueda ver las estructuras de los archivos e interacturar con ellos.
Se recomienda comenzar ejecutando el archivo `basic_graph.txt`
_En particular los archivos google_matrix.txt y notre_dam_graph.txt fueron extraidos de las siguiente páginas: http://snap.stanford.edu/data/ y http://networkrepository.com/web.php, donde también se pueden encontrar otros sets de datos_


## Tests

Para ejecutar los tests, en el directorio `tests` se debe ejecutar el siguiente comando:

`python tests.py`


## Mejoras

1. Eficiencia: si bien el proyecto es solo para mostrar cómo funciona el buscador de Google en base a PageRank, el mismo podría ser más eficiente aún sin cambiar de lenguaje de programación (C por ejemplo). En particular se podrían mejorar las operaciones con matrices.

2. Experiencia en las búsquedas: también se podrían mejorar las búsquedas que se realizan en las páginas; por ejemplo, mejorando el parseo del html de las páginas para analizar su contenido, en lugar de buscar dentro de todo el html de la misma

3. Flexibilidad: se podría mejorar aún más la flexibilidad de los scripts provistos para, por ejemplo, recibir por parámetros el número de iteraciones de PageRank que se desea calcular u otros de configurabilidad del sistema.
