import numpy as np
from numpy import matlib as mp
import random
import time
import copy
import networkx as nx
import matplotlib.pyplot as plt



def make_that_1_into_0_with_transpose(matrix, row, column):
    matrix[row][column] = 0
    matrix[column][row] = 0



def create_line_tree_adjacency_matrix(n):
    adjacency_matrix = []
    
    for i in range(0,n):
        row = [0] * n 
        adjacency_matrix.append(row)  
    
    for i in range(n):
        if i > 0:
            adjacency_matrix[i][i-1] = 1
            adjacency_matrix[i-1][i] = 1
        if i < n-1:
            adjacency_matrix[i][i+1] = 1
            adjacency_matrix[i+1][i] = 1
    
    return adjacency_matrix

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

def find_barycenter_deterministic(adj_matrix):
    leaf_cut = []    
    adj_matrix_copy = copy.deepcopy(adj_matrix)
    
    n = len(adj_matrix_copy)  # Number of nodes, number of rows
    degrees = np.sum(adj_matrix_copy, axis=1)  # Sum of row = degree
    nodes = set(range(n))  # All vertices
    
    while len(nodes) > 2: 
        # Find all leaf nodes (nodes with degree 1)
        leaf_nodes = [i for i in nodes if degrees[i] == 1]  # Only those with a single 1 are leaves
        
        for leaf in leaf_nodes:
            nodes.remove(leaf)  # Remove the leaf
            degrees[leaf] = 0  # Degree is then 0

            for neighbor in range(n):  # Check all neighbors
                if adj_matrix_copy[leaf][neighbor] == 1:  # If there is a connection
                    degrees[neighbor] -= 1  # Decrement the degree of the neighbor
                    adj_matrix_copy[leaf][neighbor] = 0  # Change the 1 to 0
                    adj_matrix_copy[neighbor][leaf] = 0  # Also change its "transpose position" to 0
        leaf_cut.append(1)

    # At this point, there should only be 1 or 2 nodes left
    remaining_nodes = list(nodes)  # Convert the set to a list

    if len(remaining_nodes) == 1:  # If only 1 vertex remains
        return remaining_nodes, adj_matrix_copy, sum(leaf_cut)
    elif len(remaining_nodes) == 2:  # If 2 vertices remain
        return remaining_nodes, adj_matrix_copy, sum(leaf_cut)



def find_barycenter_prob(matrix, vertex_to_remove):

    matrix_copy = copy.deepcopy(matrix)

    row_c = [0, 1]

    for i in vertex_to_remove:
        if vertex_to_remove.count(i) >= 2:
            return i  

    while len(row_c) != 0:
        row, column = row_colum_returner(matrix_copy, vertex_to_remove)
        row_c = row

        if len(row_c) == 0:
            break

        for r, c in zip(row, column):
                matrix_copy[r][c] = 0
                matrix[c][r] = 0


 
    for s, i in enumerate(matrix_copy):
        if sum(i) == 3:
            return s  #

    for i in vertex_to_remove:
        if sum(matrix_copy[i]) == 2:
            return i  

 
    return None
def row_colum_returner(matrix, vertex_to_remove):
    s= 0 
    column = []
    row = []
    for i in matrix:
        if sum(i) == 1:
            if s in vertex_to_remove:
                pass
            if s not in vertex_to_remove:
                d = 0
                for v in i:
                    if v==1:
                        row.append(s)
                        column.append(d)
                    d+=1
                        
    
        s+=1

    return row, column







def draw_graph_from_adjacency_matrix(adjacency_matrix):
    G = nx.Graph()

    for i in range(len(adjacency_matrix)):
        for j in range(len(adjacency_matrix[i])):
            if adjacency_matrix[i][j] != 0: 
                G.add_edge(i, j, weight=adjacency_matrix[i][j])


    G.add_nodes_from(range(len(adjacency_matrix)))

    pos = nx.spring_layout(G, seed=42)

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        edge_color='black',
        node_size=10,
        font_size=10,
        width=0.5
    )
    plt.title("Graph from Adjacency Matrix")
    plt.show()


    
def merge_trees(matrix_1, matrix_2, random_vertex_selection = True, vertex_from_matrix_1 = None, vertex_from_matrix_2 = None):
    matrix_1_cp = copy.deepcopy(matrix_1)
    matrix_2_cp = copy.deepcopy(matrix_2)


    for i in range(len(matrix_2_cp)):
        for li in matrix_1_cp:
            li.append(0)


    for i in range(len(matrix_1_cp)):
        for li in matrix_2_cp:
            li.insert(0, 0)
        


    for row in matrix_2_cp:
        matrix_1_cp.append(row)

    if random_vertex_selection: 
        vertex_for_matrix_1 = np.random.choice(list(range(len(matrix_1))))
        vertex_for_matrix_2_og = np.random.choice(list(range(len(matrix_2))))
        vertex_2_to_change = vertex_for_matrix_2_og + len(matrix_1)
        print(f"vertex {vertex_for_matrix_1} from matrix_1 and {vertex_for_matrix_2_og} from matrix_2_were chosen")
        matrix_final = make_that_0_into_1_with_transpose(matrix_1_cp, vertex_for_matrix_1, vertex_2_to_change)
        return matrix_final, vertex_for_matrix_1, vertex_for_matrix_2_og

    else:
        if vertex_from_matrix_1 is None:
            vertex_for_matrix_1 = np.random.choice(list(range(len(matrix_1))))
            vertex_2_to_change = vertex_from_matrix_2 + len(matrix_1)
            print(f"vertex {vertex_for_matrix_1} from matrix_1 and {vertex_from_matrix_2} from matrix_2_were chosen")
            matrix_final = make_that_0_into_1_with_transpose(matrix_1_cp, vertex_for_matrix_1, vertex_2_to_change)
            return matrix_final, vertex_for_matrix_1, vertex_from_matrix_2
            
        else:
            vertex_for_matrix_1 = vertex_from_matrix_1
            vertex_2_to_change = vertex_from_matrix_2 + len(matrix_1)
            print(f"vertex {vertex_for_matrix_1} from matrix_1 and {vertex_from_matrix_2} from matrix_2_were chosen")
            matrix_final = make_that_0_into_1_with_transpose(matrix_1_cp, vertex_for_matrix_1, vertex_2_to_change)
            return matrix_final, vertex_for_matrix_1, vertex_from_matrix_2


def entropy_calculator(list_s):
    entropy_sum_list = []
    for i in list_s:
        if i < 0.0000000001:
            value = 0
        else:
            value = i * np.log(i)
            entropy_sum_list.append(value)
    
    return -sum(entropy_sum_list)

def calculate_u_new(matrix, u_old = None):
    row_count = max(len(i) for i in matrix)
    u_new = [0] * row_count

    if u_old is None:
        u_old = [1 / row_count] * row_count
    
    for i in range(0, row_count):
        for j in range(0, row_count):
            for k in range(0, row_count):
                center = find_barycenter_prob(matrix, vertex_to_remove=[i, j, k])
                u_new[center] += u_old[i] * u_old[j] * u_old[k]
    
    return u_new


def main_entropy_for_each_interation(n,matrix):
    list_with_all_iteration = []
    u_old = None
    for s in set(range(n)):
        u_calculated = calculate_u_new(matrix, u_old)
        entropy_received = entropy_calculator(u_calculated)
        print(u_calculated)
        u_old = u_calculated
    
        dict_2_send = {"interation" :s,
                      "entropy":entropy_received,
                      'u_calculated':u_calculated}
    
        list_with_all_iteration.append(dict_2_send)

    return list_with_all_iteration