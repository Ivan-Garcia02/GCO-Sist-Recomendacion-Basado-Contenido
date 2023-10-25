import re
import json

def read_documents_file(file_path):
    documents = []

    with open(file_path) as file:
        while True:
            document = file.readline()
            if not document:
                break
            clean_document = re.sub(r'[^\w\s\']', '', document).lower()
            documents.append(clean_document.split())
    file.close()
    
    return documents

def read_stop_words_file(file_path):
    stop_words = []

    with open(file_path) as file:
        while True:
            stop_word = file.readline()
            if not stop_word:
                break
            stop_words.append(stop_word.strip())
    file.close()
    
    return stop_words

def read_lemmatization_file(file_path):
    with open(file_path) as file:
        while True:
            document = file.readline()
            if not document:
                break

            file_json_dic = json.loads(document)        
    file.close()

    return file_json_dic