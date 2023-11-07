def print_table(document_number, matrix, matrix_tf, matrix_tf_idf, values_idf, terms, max_string_length):
    index = 1
    print(f"Tabla para el \033[1;33mDocumento {document_number + 1}\033[0m")
    print("\033[1;34m{:<{width}} {:<{width}} {:<{width}} {:<{width}} {:<{width}} \033[0m".format('Indice', 'Termino', 'TF', 'IDF', 'TF-IDF', width=max_string_length))
    for term_index in range(len(matrix[document_number])):
        if matrix[document_number][term_index] > 0:
            print("{:<{width}} {:<{width}} {:<{width}} {:<{width}} {:<{width}} ".format(index, terms[term_index], matrix_tf[document_number][term_index], values_idf[term_index], matrix_tf_idf[document_number][term_index], width=max_string_length))
            index += 1
    print()

def print_similitary_cosine(similitary_vector):
    document_index = 1
    print("\033[1;33mSimilaridad coseno entre cada par de documentos:\033[0m")
    for similitary in similitary_vector:
        if similitary[0] != document_index:
            print()
            document_index += 1
        print(f"cos(D{similitary[0]}, D{similitary[1]}) = {similitary[2]}")