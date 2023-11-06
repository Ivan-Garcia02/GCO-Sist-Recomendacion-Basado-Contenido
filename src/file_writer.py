def print_matrix(file_name, matrix, terms, max_string_length, name_matrix):
    with open(file_name, mode='a') as file_object:
        file_object.write("{:<{width}} ".format(name_matrix, width=max_string_length))
        for word in terms:
            file_object.write("{:<{width}} ".format(word, width=max_string_length))
        file_object.write('\n')

        for index_fila in range(len(matrix)):
            file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
            for col in matrix[index_fila]:
                file_object.write("{:<{width}} ".format(col, width=max_string_length))
            file_object.write('\n')
        file_object.write('\n')

def print_idf(file_name, values_idf, max_string_length):
    with open(file_name, mode='a') as file_object:
        file_object.write("{:<{width}} ".format('IDF', width=max_string_length))
        for idf in values_idf:
            file_object.write("{:<{width}} ".format(idf, width=max_string_length))
        file_object.write('\n\n')

def print_similitary_cosine(file_name, similitary_vector):
    with open(file_name, mode='a') as file_object:
        file_object.write("Similaridad coseno entre cada par de documentos:\n")
        for similitary in similitary_vector:
            file_object.write(f"cos(D{similitary[0]}, D{similitary[1]}) = {similitary[2]}\n")

def print_matrixs(file_name, matrix, matrix_tf, matrix_tf_idf, terms, max_string_length):
    with open(file_name, mode='a') as file_object:
        file_object.write("Tabla con valores por celda n_terms|TF|TF-IDF\n")
        file_object.write("{:<{width}} ".format('', width=max_string_length))
        for word in terms:
            file_object.write("{:<{width}} ".format(word, width=max_string_length))
        file_object.write('\n')

        for index_fila in range(len(matrix)):
            file_object.write("{:<{width}} ".format(f'Documento {index_fila + 1}', width=max_string_length))
            for col_index in range(len(matrix[index_fila])):
                file_object.write("{:<{width}} ".format(f'{matrix[index_fila][col_index]}|{matrix_tf[index_fila][col_index]}|{matrix_tf_idf[index_fila][col_index]}', width=max_string_length))
            file_object.write('\n')
        file_object.write('\n')