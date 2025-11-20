import helper_functions as hf
import time

#==========================================================  Backtracking  ==========================================================

def bt_backtrack(assignment, domains, N):
    # If all N queens are placed
    if len(assignment) == N:
        return True

    # Select row with Minimum Remaining Values (MRV)
    row = hf.select_variable_MRV(assignment, domains)

    # Try columns in Least Constraining Value (LCV) order
    for val in hf.order_values_LCV(row, domains, assignment, N):
        if hf.is_consistent(assignment, row, val):
            assignment[row] = val  # Place queen

            if bt_backtrack(assignment, domains, N):
                return True

            del assignment[row]  # Backtrack

    return False


def backtracking(N):
    hf.checks_count = 0  # reset REAL counter

    start_time = time.time()

    domains = hf.generate_random_start(N)  # randomized columns for each row
    assignment = {}

    bt_backtrack(assignment, domains, N)

    end_time = time.time()

    return assignment, (end_time - start_time) * 1000, hf.checks_count