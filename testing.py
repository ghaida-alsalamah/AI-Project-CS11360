
from forward_checking import forward_checking
from bactracing import backtracking
# from mac import mac


def test_algorithm(algorithm, N, runs):
    times = []
    checks = []

    for run in range(runs):
        solution, t, c = algorithm(N)
        times.append(t)
        checks.append(c)

    best_time = min(times)
    worst_time = max(times)
    avg_time = sum(times) / len(times)

    best_checks = min(checks)
    worst_checks = max(checks)
    avg_checks = sum(checks) / len(checks)

    return best_time, avg_time, worst_time, best_checks, avg_checks, worst_checks



def main():

    print("=== N-Queens Testing Tool ===")

    while True:
        print("\nChoose the algorithm you want to test:")
        print("1. Backtracking")
        print("2. Forward Checking")
        print("3. MAC")
        print("4. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            print("\nBacktracking selected.")
            algorithm = backtracking

        elif choice == "2":
            print("\nForward Checking selected.")
            algorithm = forward_checking

        elif choice == "3":
            print("\nMAC selected.")
            #algorithm = mac

        elif choice == "4":
            print("Exiting...")
            return

        else:
            print("Invalid choice. Try again.\n")
            continue

        # ask user for Ns
        user_Ns = input("\nEnter N values to test (example: 4,8,16): ")
        N_values = [int(x.strip()) for x in user_Ns.split(",")]

        # how many times to repeat each N
        runs = int(input("How many runs per N? "))

        print("\n--- Starting Tests ---\n")

        for N in N_values:
            best_t, avg_t, worst_t, best_c, avg_c, worst_c = test_algorithm(algorithm, N, runs)

            print(f"N = {N}")
            print(f"  Best time   : {best_t * 1000:.4f} seconds")
            print(f"  Avg time    : {avg_t * 1000:.4f} seconds")
            print(f"  Worst time  : {worst_t * 1000:.4f} seconds")
            print(f"  Best checks : {best_c}")
            print(f"  Avg checks  : {int(avg_c)}")
            print(f"  Worst checks: {worst_c}\n")


if __name__ == "__main__":
    main()
