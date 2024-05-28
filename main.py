board = [3, 2, 5, 4, 3, 2, 1, 3]

def get_neighbors(board):
    neighbors = []
    
    for col in range(8):
        for row in range(8):
            if board[col] != row:
                neighbor = board[:]
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors
    
print(get_neighbors(board))
