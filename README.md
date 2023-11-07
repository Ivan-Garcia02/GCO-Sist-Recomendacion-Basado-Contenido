# Sistemas de recomendación. Modelos basados en el contenido

### Iván García González y Daniel Jorge Acosta

## Instrucciones de instalación

Durante el desarrollo del proyecto no se ha hecho uso de ninguna librería externa, por lo que para su ejecución debería bastar con la instalación del intérprete de Python.

## Descripción del código

El código del proyecto se encuentra dividido en varios ficheros.

### main

Este fichero contiene el cuerpo principal del programa. En este se recogen los argumentos pasados por consola por el usuario, se leen los ficheros y se realiza la recomendación.

### file_reader

Contiene las funciones encargadas de leer los ficheros que se utilizarán durante la ejecución del programa.

#### `read_documents_file`

Esta función recibe la ruta del fichero que contiene los documentos a analizar. Durante su ejecución, lee el fichero, limpia el contenido, eliminando los signos de puntuación y conviertiendo las letras en minúsculas, y devuelve una matriz con los términos de cada documento contenido en el fichero separados por filas.

#### `read_stop_words_file`

Esta función recibe la ruta del fichero que contiene las palabras de parada. Durante su ejecución, lee el fichero y devuelve una lista de las palabras de parada contenidas en el mismo.

#### `read_lemmatization_file`

Esta función recibe la ruta del archivo de lematización. Durante su ejecución, lee el archivo y devuelve un diccionario JSON que contiene la asociación de palabras para la lematización, resultado del análisis del archivo JSON.

### file_writer

Contiene las funciones encargadas de escribir el fichero de salida con el resultado del programa.

#### `print_table`

Esta función

#### `print_similitary_cosine`

### tools

Contiene funciones utilizadas durante la ejecución del programa.

#### `documents_lemmatization`

Esta función recibe la matriz con los documentos y el vector con los términos de lematización. Durante la ejecución, los términos de los documentos que estén en el fichero de lematización serán sustituidos por su correspondiente según el diccionario JSON de términos.

#### `remove_stop_words`

#### `get_terms`

#### `build_matrix_term_doc`

#### `get_idf`

#### `build_matrix_tf_idf`

#### `get_length_vector`

#### `build_matrix_tf_normalized`

#### `cosine_similitary`

## Ejemplo de uso

Un ejemplo de uso sería el siguiente: `python3 main.py -d documents.txt -s stop-words.txt -l corpus.txt -f out.txt`

Ejecutamos el intérprete _python3_ con el fichero _main.py_ y añadimos las opciones para la ejecución:

- -d | --documentsPath: Ruta del fichero de texto plano con extensión _.txt._ que contiene los documentos a analizar.
- -s | --stopWordsPath: Ruta del fichero con palabras de parada a descartar durante el proceso de recomendación.
- -l | --lemmatizationPath: Ruta del fichero de lematización de términos.
- -f | --fileOut: Fichero de salida de resultados, por defecto `salida.txt`
