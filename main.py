import random
import math

def create_random_board():
    board = []

    for i in range(8):
        row = random.randint(0, 7)
        board.append(row)

    return board

def get_neighbors(board):
    neighbors = []
    
    for col in range(8):
        for row in range(8):
            if board[col] != row:
                neighbor = board[:]
                
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def heuristic_function(board):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j]:
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts
    
def hill_climbing(board):
    state = board
    h_state = heuristic_function(state)
    
    while True:
        h_min = h_state
        
        neighbors = get_neighbors(state)
        
        for neighbor in neighbors:
            h_neighbor = heuristic_function(neighbor)

            if h_neighbor < h_min:
                state = neighbor
                h_min = h_neighbor

        if h_min == h_state:
            return state
        
        h_state = h_min

def cooling_speed(i):
    return 1 - 0.0001 * i

def get_random_neighbor(board):
    col = random.randint(0, 7)
    row = board[col];

    while True:
        new_row = random.randint(0, 7)

        if (new_row != row):
            neighbor = board[:]
            
            neighbor[col] = new_row
            return neighbor
    

def simulated_annealing(board):
    curr_state = board
    i = 1
    
    while True:
        temperature = cooling_speed(i)

        if temperature == 0:
            return curr_state

        next_state = get_random_neighbor(curr_state)

        delta_e = heuristic_function(curr_state) - heuristic_function(next_state)

        if delta_e > 0:
            curr_state = next_state
        else:
            probability = math.exp(delta_e / temperature)

            if random.random() < probability:
                curr_state = next_state
                
        i += 1
        
board = create_random_board()

print("Initial state: " + str(board))
print("Number of conflicts: " + str(heuristic_function(board)))

print()

solution = hill_climbing(board)

print("Solution with hill climbing: " + str(solution))
print("Number of conflicts: " + str(heuristic_function(solution)))

print()

solution = simulated_annealing(board)

print("Solution with simulated annealing: " + str(solution))
print("Number of conflicts: " + str(heuristic_function(solution)))
