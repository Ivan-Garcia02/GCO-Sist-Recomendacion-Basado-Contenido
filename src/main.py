import argparse
from file_reader import read_documents_file, read_stop_words_file, read_lemmatization_file

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
print(stop_words)
print(lemmatization)