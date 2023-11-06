import argparse
import json
import math
import numpy as np

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

# Obtiene todos los terminos no repetidos
def get_terms(documents):
    terms = []

    for document in documents[:]:
        for word in document[:]:
            try:
                terms.index(word) # Busca si la palabra ya se ha añadido a los terminos
            except: 
                terms.append(word) # Sino se ha añadido la añade
    return terms

# Construye la matriz término-documento
def build_matrix_term_doc(documents, terms):
    matrix = np.zeros((len(documents), len(terms))) # Crea la matriz con 0s
    
    for index_doc in range(len(documents)): # Hacemos el conteo para la matriz término-documento
        for word in documents[index_doc]:
            index_word = terms.index(word)
            matrix[index_doc][index_word] += 1
    return matrix

def get_idf(n_documents, matrix, terms):
    values_idf = []

    for index_word in range(len(terms)):
        df = 0
        for index_doc in range(len(matrix)):
            if matrix[index_doc][index_word] > 0:
                df += 1
        values_idf.append(round(math.log10(n_documents/df), 3))
    return values_idf

def build_matrix_tf(matrix):
    matrix_tf = []

    for document in matrix[:]:
        vec_aux = []
        for number in document[:]:
            if number > 0:
                vec_aux.append(round(1 + math.log10(number), 3))
            else:
                vec_aux.append(0.0)
        matrix_tf.append(vec_aux)
    return matrix_tf

def build_matrix_tf_idf(matrix_tf, values_idf):
    matrix_tf_idf = []

    for document in matrix_tf[:]:
        vec_aux = []
        for number_index in range(len(document)):
            vec_aux.append(round(document[number_index] * values_idf[number_index], 3))

        matrix_tf_idf.append(vec_aux)
    return matrix_tf_idf

def get_length_vector(matrix_tf):
    length_vector = []

    for document in matrix_tf[:]:
        val_sum = 0
        for number in document[:]:
            val_sum += math.pow(number, 2)
        length_vector.append(round(math.sqrt(val_sum), 3)) 
    return length_vector

def build_matrix_tf_normalized(matrix_tf):
    length_vector = get_length_vector(matrix_tf)
    matrix_tf_normalizada = []

    for document_index in range(len(matrix_tf)):
        vec_aux = []
        for number_index in range(len(matrix_tf[document_index])):
            vec_aux.append(round(matrix_tf[document_index][number_index] / length_vector[document_index], 3))
        matrix_tf_normalizada.append(vec_aux)
    return matrix_tf_normalizada

def cosine_similitary(matrix_tfn, terms):
    similitary_vector = []

    for index_doc1 in range(len(matrix_tfn)):
        for index_doc2 in range(index_doc1 + 1, len(matrix_tfn)):
            val_sum = 0
            for index_termino in range(len(terms)):
                val_sum += matrix_tfn[index_doc1][index_termino] * matrix_tfn[index_doc2][index_termino]
            similitary_vector.append([index_doc1 + 1, index_doc2 + 1, val_sum])
    return similitary_vector