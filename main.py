from backtracking import backtracking
from forward_checking import forward_checking
#from mac import mac
import helper_functions as hf


def main():

    print("======== N-Queens Solver ========")

    while True:

        # -----------------------------
        # Step 1: Choose N
        # -----------------------------
        N = int(input("\nEnter the value of N: "))
        print(f"N is set to {N}")

        while True:
            print("\nChoose an algorithm:")
            print("1. Backtracking")
            print("2. Forward Checking")
            print("3. MAC")
            print("4. Choose a NEW N value")
            print("5. Exit")

            choice = input("Enter your choice: ")

            # Backtracking
            if choice == "1":
                print("\nRunning Backtracking...")
                solution, t, checks = backtracking(N)
                print("Solution:", solution)
                hf.print_board(solution, N)
                print(f"Time: {t * 1000:.6f} ms")
                print("Checks:", checks)

            # Forward Checking
            elif choice == "2":
                print("\nRunning Forward Checking...")
                solution, t, checks = forward_checking(N)
                print("Solution:", solution)
                hf.print_board(solution, N)
                print(f"Time: {t * 1000:.6f} second")
                print("Checks:", checks)

            # MAC
            elif choice == "3":
                print("\nRunning MAC...")
                print("Not implemented yet.")

            # NEW N
            elif choice == "4":
                print("\nRestarting to choose a new N...\n")
                break   # breaks inner loop, goes back to ask for N again

            # EXIT
            elif choice == "5":
                print("Exiting...")
                return

            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    main()

