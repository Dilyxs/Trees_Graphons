import time
def process_matrix(matrix):
    row = []
    column = []
    w_counter = []

    for i in matrix:
        s = 0  
        d = len(i) 


        while sum(i) < 3:
            if s in w_counter:
                i.append(0)
            else:
                i.append(1)
                row.append(matrix.index(i)) 
                column.append(d) 
            w_counter.append(s)
            s += 1
            d += 1 


        while i.count(1) < 2:
            i.append(1)
            row.append(matrix.index(i)) 
            column.append(d) 
            d += 1  

    return matrix, row, column

def make_that_0_into_1_with_transpose(matrix, row, column):
    matrix[row][column] = 1
    matrix[column][row] = 1


    return matrix


def connect_edges(matrix, row, column):
    
    index_position = 0
    for i in row:
        matrix = make_that_0_into_1_with_transpose(matrix, i, column[index_position])
        index_position += 1
    
    return matrix

def initialize_zero_rows(matrix, row):
    max_length = 0
    for i in matrix: 
            max_length = len(i)

    for _ in range(len(row)):  
        matrix.append([0] * max_length)

    return matrix


def max_length_append_0(matrix):

    max_length = max(len(i) for i in matrix)

    for i in matrix:
        while len(i) < max_length:
            i.append(0)

    return matrix

def final_3_reg_tree(n):
    matrix = [[0]]

    for _ in range(n):
        matrix, row, column = process_matrix(matrix)
        matrix = max_length_append_0(matrix)
        matrix = initialize_zero_rows(matrix, row)
        matrix = connect_edges(matrix, row, column)

    return matrix

t0 =  time.time()

matrix = final_3_reg_tree(3)

t1 = time.time()

t_time = t1-t0

print(f"time take  is {t_time}")