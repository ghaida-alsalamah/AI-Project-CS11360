
#==========================================================  Helper Functions  ==========================================================

# This variable counts how many constraint checks we do.
checks_count = 0
# This function increases the check counter.
def increment_check():
    global checks_count
    checks_count += 1


# This function checks if two queens attack each other.
def check_conflict(r1, c1, r2, c2):
    global checks_count
    increment_check()  # count every conflict check
    
    # same column
    if c1 == c2:
        return True

    # same diagonal
    if abs(r1 - r2) == abs(c1 - c2):
        return True

    return False



import random
# This function creates random domain orders for each row (for random start runs).
def generate_random_start(N):
    domains = {}
    for row in range(1, N+1):
        cols = list(range(1, N+1))
        random.shuffle(cols)
        domains[row] = cols
    return domains



# This function checks if placing a queen at (row, col) is valid.
def is_consistent(assignment, row, col):
    global checks_count
    for r in assignment:
        c = assignment[r]
        if check_conflict(r, c, row, col):
            return False
    return True



import copy
# This function returns a deep copy of the domains to avoid changing the original.
def copy_domains(domain):
    return copy.deepcopy(domain)



# This function picks the next unassigned row using MRV.
def select_variable_MRV(assignment, domains):
    unassigned = [r for r in domains if r not in assignment]
    return min(unassigned, key=lambda r: len(domains[r]))



# This function orders values using LCV.
def order_values_LCV(row, domains, assignment, N):
    global checks_count

    values = domains[row]
    value_scores = []  # (value, score of how many future values it blocks)

    for val in values:
        score = 0

        # count how many values this choice would eliminate for future rows
        for future_row in range(1, N+1):
            if future_row == row or future_row in assignment:
                continue

            for future_val in domains[future_row]:
                if check_conflict(row, val, future_row, future_val):
                    score += 1

        value_scores.append((val, score))

    # sort by score so least-constraining value comes first
    value_scores.sort(key=lambda x: x[1])

    return [v for (v, s) in value_scores]



# This function prints the chessboard.
def print_board(assignment, N):
    print("\nBoard:\n")

    for row in range(1, N+1):
        line = ""
        col_with_queen = assignment.get(row)

        for col in range(1, N+1):
            if col == col_with_queen:
                line += " ♕ "
            else:
                line += " . "

        print(line)

    print()


#==========================================================  Backtracking ==========================================================

#==========================================================  MAC  ==========================================================