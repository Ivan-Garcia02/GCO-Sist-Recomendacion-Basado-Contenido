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

Esta función recibe la ruta del fichero de lematización.

## Ejemplo de uso

Un ejemplo de uso sería el siguiente: `python3 main.py -d documents.txt -s stop-words.txt -l corpus.txt`

Ejecutamos el intérprete _python3_ con el fichero _main.py_ y añadimos las opciones para la ejecución:

- -d | --documentsPath: Ruta del fichero de texto plano con extensión _.txt._ que contiene los documentos a analizar.
- -s | --stopWordsPath: Ruta del fichero con palabras de parada a descartar durante el proceso de recomendación.
- -l | --lemmatizationPath: Ruta del fichero de lematización de términos.
