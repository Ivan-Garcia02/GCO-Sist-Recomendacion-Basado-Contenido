import argparse
import json
import math
import numpy as np
from file_reader import read_documents_file, read_stop_words_file, read_lemmatization_file
from tools import documents_lemmatization, remove_stop_words, get_terms, build_matrix_term_doc, get_idf, build_matrix_tf, get_length_vector, build_matrix_tf_idf, build_matrix_tf_normalized, cosine_similitary
from file_writer import print_similitary_cosine, print_matrix, print_idf
# python3 src/main.py -d test_files/documents-01.txt -s test_files/stop-words-en.txt -l test_files/corpus-en.txt

parser = argparse.ArgumentParser(prog='Métodos Basados en Contenido', description='Sistemas de Recomendación')
parser.add_argument('-d', '--documentsPath', type=str, required=True, help="Fichero de entrada de texto plano con documentos")
parser.add_argument('-s', '--stopWordsPath', type=str, required=True, help="Fichero de entrada con palabras de parada")
parser.add_argument('-l', '--lemmatizationPath', type=str, required=True, help="Fichero de entrada con lemantizacion de terminos")
parser.add_argument('-f', '--fileOut', type=str, required=False, default="salida.txt", help="Fichero de salida de resultados")

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
terms = get_terms(documents)
matrix = build_matrix_term_doc(documents, terms)

matrix_tf = build_matrix_tf(matrix) # Matriz TF
values_idf = get_idf(len(documents), matrix, terms) # Calcula DF + IDF
matrix_tf_idf = build_matrix_tf_idf(matrix_tf, values_idf) # Matriz TF-IDF

# Similidad entre documentos
matrix_tf_normalized = build_matrix_tf_normalized(matrix_tf) # Normalizacion de vectores
similitary_vector = cosine_similitary(matrix_tf_normalized, terms)

# Imprime las matrix de terminos, matriz TF, IDF, matriz TF-IDF y similitud de coseno
name_file = args.fileOut
max_string_length = max (len(word) for word in terms)
print_matrix(name_file, matrix, terms, max_string_length, "Matrix terms")
print_matrix(name_file, matrix_tf, terms, max_string_length, "Matrix TF")
print_idf(name_file, values_idf, max_string_length)
print_matrix(name_file, matrix_tf_idf, terms, max_string_length, "Matrix TF-IDF")
print_similitary_cosine(name_file, similitary_vector)