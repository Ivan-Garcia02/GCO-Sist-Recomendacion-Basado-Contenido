# Sistemas de recomendación. Modelos basados en el contenido

### Iván García González y Daniel Jorge Acosta

## Instrucciones de instalación

Durante el desarrollo del proyecto no se ha hecho uso de ninguna librería externa, por lo que para su ejecución debería bastar con la instalación del intérprete de Python.S

## Descripción del código

El código del proyecto se encuentra dividido en varios ficheros.

### main

Este archivo contiene el cuerpo principal del programa. En él se recogen los argumentos pasados por el usuario a través de la consola, se leen los archivos y se realizan las operaciones para el cálculo de los valores de similitud.

En primer lugar, se lleva a cabo la limpieza de los documentos mediante la lematización de los términos y la eliminación de las stop-words. A continuación, se calcula la matriz término-documento con los valores de apariciones, seguido del cálculo de los valores de TF, IDF y TF-IDF.

Después, se procede a realizar los cálculos para la similitud entre documentos. Se calcula la matriz TF normalizada y la similitud entre documentos. Finalmente, se imprimen las tablas y las similitudes resultantes en la terminal.

### file_reader

Contiene las funciones encargadas de leer los ficheros que se utilizarán durante la ejecución del programa.

#### `read_documents_file`

Esta función recibe la ruta del fichero que contiene los documentos a analizar. Durante su ejecución, lee el fichero, limpia el contenido, eliminando los signos de puntuación y conviertiendo las letras en minúsculas, y devuelve una matriz con los términos de cada documento contenido en el fichero separados por filas.

#### `read_stop_words_file`

Esta función recibe la ruta del fichero que contiene las palabras de parada. Durante su ejecución, lee el fichero y devuelve una lista de las palabras de parada contenidas en el mismo.

#### `read_lemmatization_file`

Esta función recibe la ruta del archivo de lematización. Durante su ejecución, lee el archivo y devuelve un diccionario JSON que contiene la asociación de palabras para la lematización, resultado del análisis del archivo JSON.

### printer

Contiene las funciones encargadas de escribir los resultados del programa.

#### `print_table`

Esta función se encarga de imprimir una tabla con los valores de un documento. Para ello, recibe el documento a imprimir, la matriz de apariciones, los valores de TF, los valores de TF-IDF, los valores IDF, los términos y un tamaño máximo de campo para el formateo de la tabla.

La tabla tendrá seis columnas que corresponden al índice del término global, el término, el número de apariciones del término en el documento, el valor TF, el valor IDF y el valor TF-IDF. Las filas estarán relacionadas con los términos del documento que tienen al menos una aparición.

#### `print_similitary_cosine`

Esta función recibe el vector con la similitud entre cada par de documentos y se encarga de imprimirlos en la terminal.

### tools

Contiene funciones utilizadas durante la ejecución del programa.

#### `documents_lemmatization`

Esta función recibe la matriz con los documentos y el vector con los términos de lematización. Durante la ejecución, los términos de los documentos que estén en el fichero de lematización serán sustituidos por su correspondiente según el diccionario JSON de términos.

#### `remove_stop_words`

Esta función recibe la matriz con los documentos y el vector con las palabras a eliminar (stop-words). Durante la ejecución, estas palabras serán eliminadas de los documentos.

#### `get_terms`

Esta función recibe una matriz que contiene los documentos y devuelve un vector que contiene todos los términos presentes en los documentos sin repeticiones. Esto es necesario para realizar cálculos y para construir la matriz término-documento.

#### `build_matrix_term_doc`

Esta función recibe la matriz que contiene los documentos y el vector que contiene los términos no repetidos. Luego, crea una matriz con dimensiones documentos x términos, en la que registra y contabiliza las apariciones de los términos en los documentos, indicándolos en esta nueva matriz.

#### `get_idf`

Esta función recibe el número máximo de documentos, la matriz término-documento y el vector de términos. Durante su ejecución, calcula el DF (Frecuencia del Documento) de cada término como el número de documentos en los que aparece dicho término. Luego, utiliza estos DFs para calcular los valores IDF (Frecuencia Inversa del Documento) de cada término como el logaritmo en base 10 del cociente entre el número total de documentos y el DF específico de cada término. Los valores resultantes se redondean a tres decimales.

#### `build_matrix_tf`

Esta función recibe la matriz término-documento y devuelve la matriz con los valores TF (Frecuencia del Término) de cada término en el documento. Los valores de TF se calculan como 1 más el logaritmo en base 10 de cada valor término-documento, en caso de que el valor sea mayor que 0. Si el valor es igual a 0, el valor de TF es 0. Los valores resultantes se redondean a tres decimales.

#### `build_matrix_tf_idf`

Esta función recibe la matriz con los valores de TF (Frecuencia del Término) de cada término en el documento y los valores IDF (Frecuencia Inversa del Documento) de cada término, y calcula la matriz TF-IDF multiplicando cada valor de TF por su correspondiente valor IDF del término. Los valores resultantes se redondean a tres decimales.

#### `get_length_vector`

Esta función recibe la matriz con los valores de TF y calcula, para cada documento, la longitud de los vectores, definida como la raíz cuadrada de la suma de los valores al cuadrado de cada término. Estos valores se utilizan para el cálculo de la matriz de TF normalizada. Los resultados se redondean a tres decimales.

#### `build_matrix_tf_normalized`

Esta función recibe la matriz con los valores de TF y calcula la matriz normalizada de vectores. Para ello, obtiene la longitud del vector llamando a la función `get_length_vector`, y luego divide cada valor del vector de términos por la longitud del vector del documento correspondiente. Los resultados se redondean a tres decimales.

#### `cosine_similitary`

Esta función recibe la matriz TF normalizada y el vector de términos, y calcula la similitud entre cada par de documentos. Para hacerlo, realiza la suma del producto de los vectores de ambos documentos. Los resultados se redondean a tres decimales.

## Ejemplo de uso

Un ejemplo de uso sería el siguiente: `python3 main.py -d documents.txt -s stop-words.txt -l corpus.txt`

Ejecutamos el intérprete _python3_ con el fichero _main.py_ y añadimos las opciones para la ejecución:

- -d | --documentsPath: Ruta del fichero de texto plano con extensión _.txt._ que contiene los documentos a analizar.
- -s | --stopWordsPath: Ruta del fichero con palabras de parada a descartar durante el proceso de recomendación.
- -l | --lemmatizationPath: Ruta del fichero de lematización de términos.
