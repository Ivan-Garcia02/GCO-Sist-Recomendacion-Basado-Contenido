import argparse
import json
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


# Imprimimos la matrix en un archivo
with open('salida.txt', mode='w') as file_object:
    max_string_length = max (len(word) for word in values) # Obtener la palabra mas larga para max de columna
    for word in values:
        file_object.write("{:<{width}} ".format(word, width=max_string_length))
    file_object.write('\n')

    for fila in matrix:
        for col in fila:
            file_object.write("{:<{width}} ".format(col, width=max_string_length))
        file_object.write('\n')

print(matrix)