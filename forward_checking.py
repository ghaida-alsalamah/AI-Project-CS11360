import helper_functions as hf
import time

#==========================================================  Forward Checking  ==========================================================

def remove_conflict_from_domains(row, val, domains, assignment):

    for r in domains:

        if r in assignment or r == row:
            continue
        
        new_domain = []

        for v in domains[r]:
            if not hf.check_conflict(row, val, r, v):
                new_domain.append(v)

        if len(new_domain) == 0:
            return False
        
        domains[r] = new_domain
    
    return True


def fc_backtrack(assignment, domains, N):

    if len(assignment) == N:
        return True
    
    row = hf.select_variable_MRV(assignment, domains)

    for val in hf.order_values_LCV(row, domains, assignment, N):

        if hf.is_consistent(assignment, row, val):
            assignment[row] = val

            old_domains = hf.copy_domains(domains)

            if remove_conflict_from_domains(row, val, domains, assignment):

                if fc_backtrack(assignment, domains, N):
                    return True

            domains.clear()
            domains.update(old_domains)
            del assignment[row]

    return False 


def forward_checking(N):
    
    hf.checks_count = 0  # reset REAL counter

    start_time = time.time()

    domains = hf.generate_random_start(N)
    assignment = {}

    fc_backtrack(assignment, domains, N)

    end_time = time.time()

    return assignment, end_time - start_time, hf.checks_count
