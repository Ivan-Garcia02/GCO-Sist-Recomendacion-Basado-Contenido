import argparse
import json
import math
import numpy as np
from file_reader import read_documents_file, read_stop_words_file, read_lemmatization_file
# python3 src/main.py -d test_files/documents-01.txt -s test_files/stop-words-en.txt -l test_files/corpus-en.txt

def documents_lemmatization(documents, lemmatization):
    for i in range(len(documents)):
        for j in range(len(documents[i])):
            try:
                documents[i][j] = lemmatization[documents[i][j]]
            except:
                pass
           
    return documents

def remove_stop_words(documents, stop_words):
    for document in documents[:]:
        for stop_word in stop_words:
            while stop_word in document:
                document.remove(stop_word)
    return documents

parser = argparse.ArgumentParser(prog='Métodos Basados en Contenido', description='Sistemas de Recomendación')
parser.add_argument('-d', '--documentsFilename', type=str, required=True, help="Fichero de entrada de texto plano con documentos")
parser.add_argument('-s', '--stopWordsFilename', type=str, required=True, help="Fichero de entrada con palabras de parada")
parser.add_argument('-l', '--lemmatizationFilename', type=str, required=True, help="Fichero de entrada con lemantizacion de terminos")

args = parser.parse_args()

if args.documentsFilename.endswith(".txt") == False:
    print('El fichero de documentos debe tener extensión .txt')
    quit()

documents = read_documents_file(args.documentsFilename)
stop_words = read_stop_words_file(args.stopWordsFilename)
lemmatization = read_lemmatization_file(args.lemmatizationFilename)

print(documents)
documents_lemmatization(documents, lemmatization)
remove_stop_words(documents, stop_words)
print(documents)

# Cosntruir la matriz termino-documento
values = []
for document in documents[:]: # Obtener las columnas con las palabras sin repetir en values
    for word in document[:]:
        try:
            values.index(word)
        except: 
            values.append(word)
print(values)

matrix = np.zeros((len(documents), len(values))) # Creamos la matriz con 0s
for idex_doc in range(len(documents)): # Hacemos el conteo para la matriz termino documento
    for word in documents[idex_doc]:
        index_word = values.index(word)
        matrix[idex_doc][index_word] += 1

# Calcular df + idf
values_df = []
values_idf = []
n_documents = len(documents)
for index_word in range(len(values)):
    val_sum = 0
    for index_doc in range(len(matrix)):
        val_sum += matrix[index_doc][index_word]
    values_df.append(val_sum)
    values_idf.append(round(math.log10(n_documents/val_sum), 3))


# Imprimimos la matrix en un archivo + df + idf
with open('salida.txt', mode='w') as file_object:
    max_string_length = max (len(word) for word in values) # Obtener la palabra mas larga para max de columna
    file_object.write("{:<{width}} ".format('', width=max_string_length))
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for index_fila in range(len(matrix)):
        file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
        for col in matrix[index_fila]:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')

    file_object.write("{:<{width}} ".format('DF', width=max_string_length))
    for df in values_df:
        file_object.write("{:<{width}} ".format(df, width=max_string_length))
    file_object.write('\n')

    file_object.write("{:<{width}} ".format('IDF', width=max_string_length))
    for idf in values_idf:
        file_object.write("{:<{width}} ".format(idf, width=max_string_length))
    file_object.write('\n\n')
print(matrix)

# Matrix tf
matrix_tf = []
for document in matrix[:]:
    vec_aux = []
    for number in document[:]:
        if number > 0:
            vec_aux.append(round(1 + math.log10(number), 3))
        else:
            vec_aux.append(0.0)
    matrix_tf.append(vec_aux)

# Imprimimos la matrix en un archivo
with open('salida.txt', mode='a') as file_object:
    max_string_length = max (len(word) for word in values) # Obtener la palabra mas larga para max de columna
    file_object.write("{:<{width}} ".format('VALORES TF', width=max_string_length))
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for index_fila in range(len(matrix_tf)):
        file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
        for col in matrix_tf[index_fila]:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')
print(matrix_tf)