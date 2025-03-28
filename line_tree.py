import time

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



t0 = time.time()
adj_matrix = create_line_tree_adjacency_matrix(12)
t1= time.time()
t_time = t1 - t0

print(f"printing time is ({t_time})")
