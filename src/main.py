import argparse
import json
from file_reader import read_documents_file, read_stop_words_file, read_lemmatization_file

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
        aux_document = document[:]
        for stop_word in stop_words:
            if stop_word in document:
                print(stop_word)
                aux_document.remove(stop_word)
        document = aux_document
        print(document)
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