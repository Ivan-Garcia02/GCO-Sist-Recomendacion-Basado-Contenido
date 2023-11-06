import argparse
import json
import math
import numpy as np
from file_reader import read_documents_file, read_stop_words_file, read_lemmatization_file
from tools import documents_lemmatization, remove_stop_words, get_terms, build_matrix_term_doc, get_idf, build_matrix_tf, get_length_vector, build_matrix_tf_idf, build_matrix_tf_normalized, cosine_similitary
# python3 src/main.py -d test_files/documents-01.txt -s test_files/stop-words-en.txt -l test_files/corpus-en.txt

parser = argparse.ArgumentParser(prog='Métodos Basados en Contenido', description='Sistemas de Recomendación')
parser.add_argument('-d', '--documentsPath', type=str, required=True, help="Fichero de entrada de texto plano con documentos")
parser.add_argument('-s', '--stopWordsPath', type=str, required=True, help="Fichero de entrada con palabras de parada")
parser.add_argument('-l', '--lemmatizationPath', type=str, required=True, help="Fichero de entrada con lemantizacion de terminos")

args = parser.parse_args()

if args.documentsPath.endswith(".txt") == False:
    print('El fichero de documentos debe tener extensión .txt')
    quit()

documents = read_documents_file(args.documentsPath)
stop_words = read_stop_words_file(args.stopWordsPath)
lemmatization = read_lemmatization_file(args.lemmatizationPath)

documents_lemmatization(documents, lemmatization)
remove_stop_words(documents, stop_words)

# Construye la matriz término-documento
values = get_terms(documents)
matrix = build_matrix_term_doc(documents, values)

# Calcula DF + IDF
values_idf = get_idf(len(documents), matrix, values)

# Imprime la matriz en un archivo + DF + IDF
with open('salida.txt', mode='w') as file_object:
    max_string_length = max (len(word) for word in values)
    file_object.write("{:<{width}} ".format('', width=max_string_length))
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for index_fila in range(len(matrix)):
        file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
        for col in matrix[index_fila]:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')

    #file_object.write("{:<{width}} ".format('DF', width=max_string_length))
    #for df in values_df:
    #    file_object.write("{:<{width}} ".format(df, width=max_string_length))
    #file_object.write('\n')

    file_object.write("{:<{width}} ".format('IDF', width=max_string_length))
    for idf in values_idf:
        file_object.write("{:<{width}} ".format(idf, width=max_string_length))
    file_object.write('\n\n')
print(matrix)

# Matriz TF
matrix_tf = build_matrix_tf(matrix)

# Longitud de vectores
long_vectores = get_length_vector(matrix_tf)

# Matriz TF-IDF
matrix_tf_idf = build_matrix_tf_idf(matrix_tf, values_idf)

# Imprime la matriz en un archivo
with open('salida.txt', mode='a') as file_object:
    max_string_length = max (len(word) for word in values)
    file_object.write("{:<{width}} ".format('VALORES TF', width=max_string_length))
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for index_fila in range(len(matrix_tf)):
        file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
        for col in matrix_tf[index_fila]:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')
    file_object.write('\n')

    file_object.write("{:<{width}} ".format('VALORES TF-IDF', width=max_string_length))
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for index_fila in range(len(matrix_tf_idf)):
        file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
        for col in matrix_tf_idf[index_fila]:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')

    file_object.write("{:<{width}} ".format('VALORES longitud vector', width=max_string_length))
    for word in long_vectores:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n\n')


# Normalizacion de vectores
matrix_tf_normalizada = build_matrix_tf_normalized(matrix_tf)

# Longitud de vectores
long_vectores_normalizada = get_length_vector(matrix_tf_normalizada)

# Imprime la matriz en un archivo
with open('salida.txt', mode='a') as file_object:
    file_object.write("{:<{width}} ".format('VALORES TFN', width=max_string_length))
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for index_fila in range(len(matrix_tf_normalizada)):
        file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
        for col in matrix_tf_normalizada[index_fila]:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')

    file_object.write("{:<{width}} ".format('VALORES longitud vector N', width=max_string_length))
    for word in long_vectores_normalizada:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

# Similidad entre documentos
similitud_coseno = cosine_similitary(matrix_tf_normalizada, values)
print(similitud_coseno)