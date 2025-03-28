import numpy as np
from numpy import matlib as mp
import random
import time

from threading import Timer

def matrix_uniform_attachment(n):
    inital_row_0 = [0,1]
    second_row_1 = [1,0]
    matrix = [inital_row_0, second_row_1]
    while n> len(matrix):
        new_matrix = []
        position = random.randrange(0,len(matrix) )
        new_shape = int(len(matrix)) + 1
        new_row = [0] * new_shape
        new_row[position] = 1
        #nr = np.array(new_row)       
        for i in range(0, len(matrix)):
            
            if i != position:
                (matrix[i]).append(0)

            else:
                (matrix[i]).append(1)

            new_matrix.append(matrix[i])
        new_matrix.append(new_row)
        matrix = new_matrix


    return matrix

    
t0 = time.time()


md = matrix_uniform_attachment(1000)
t1 = time.time()

time_take =  t1-t0
print(time_take)

