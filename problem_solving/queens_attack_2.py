def queensAttack(n, k, r_q, c_q, obstacles):
    """
    This function computes the maximum number of moves available to the queen.

    Args:
        n: Size of the board (n x n)
        k: Number of obstacles
        r_q: Row position of queen
        c_q: Column position of queen
        obstacles: An array with the positions of obstacles
    
    Returns:
        An integer representing the maximum number of moves available.
    """
    
    if n == 1:
        return 0
    
    # Encoding the number of moves between queen and obstacles in all 8 directions.
    # Index and meanings:
    # 0: Left, 1: Right, 2: Up, 3: Down, 4: Left Upper Diagonal
    # 5: Right Lower diagonal, 6: Left Lower diagoanal, 7: Right Upper diagonal
    moves = [-1, -2, -3, -4, -5, -6, -7, -8]

    # Calculating the maximum number of moves in any direction. Same index meanings
    # as above.
    max_moves = [c_q-1, n-c_q, n-r_q, r_q-1,
                 min(c_q-1, n-r_q), min(n-c_q, r_q-1),
                 min(c_q-1, r_q-1), min(n-c_q, n-r_q)]

    if k == 0:
        return sum(max_moves)
    
    # The main logic of this for loop is to first find which direction each obstacle
    # lies in. Then calculate the distance between the queen and the obstacle.
    # Finally store the distance in the moves array.
    for i in range(k):
        
        # This condition checks if the queen is completely blocked.
        if len(set(moves)) == 1 and moves[0] == 1:
            return 0
        
        # Horizontal
        if obstacles[i][0] == r_q:
            diff = obstacles[i][1] - c_q
            # Left
            if diff < 0:
                if moves[0] == -1 or abs(diff) < moves[0]:
                    moves[0] = abs(diff)
            # Right
            else:
                if moves[1] == -2 or abs(diff) < moves[1]:
                    moves[1] = abs(diff)
        
        # Vertical
        if obstacles[i][1] == c_q:
            diff = obstacles[i][0] - r_q
            # Up
            if diff > 0:
                if moves[2] == -3 or abs(diff) < moves[2]:
                    moves[2] = abs(diff)
            # Down
            else:
                if moves[3] == -4 or abs(diff) < moves[3]:
                    moves[3] = abs(diff)
        
        # Diagonal
        if abs(obstacles[i][0] - r_q) == abs(obstacles[i][1] - c_q):
            diff = abs(obstacles[i][0] - r_q) # Any difference is fine
            
            # Upper Left Diagonal
            if (obstacles[i][0] > r_q) and (obstacles[i][1] < c_q):
                if moves[4] == -5 or diff < moves[4]:
                    moves[4] = diff
            
            # Lower Right Diagonal
            elif (obstacles[i][0] < r_q) and (obstacles[i][1] > c_q):
                if moves[5] == -6 or diff < moves[5]:
                    moves[5] = diff
            
            # Lower Left Diagonal
            elif (obstacles[i][0] < r_q) and (obstacles[i][1] < c_q):
                if moves[6] == -7 or diff < moves[6]:
                    moves[6] = diff
            
            # Upper Right Diagonal
            else:
                if moves[7] == -8 or diff < moves[7]:
                    moves[7] = diff
    
    moves = [(moves[i] - 1) if moves[i] > 0 else max_moves[i] for i in range(8)]
    return sum(moves)
