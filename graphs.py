import matplotlib.pyplot as plt

# Here we store the testing results for each algorithm.
results = {
    "Forward Checking": {
        "N": [4, 8, 16, 32, 64],
        "avg_times": [0.0, 4.0282, 6.3412, 38.5707, 920.8952],
        "avg_checks": [118, 1449, 14477, 192409, 3045307]
    },

    "Backtracking": {
        "N": [],    
        "avg_times": [],
        "avg_checks": []
    },

    "MAC": {
        "N": [],        
        "avg_times": [],
        "avg_checks": []
    }
}


# This function draws the time plot.
def plot_time(N, times, title):
    plt.figure()
    plt.plot(N, times)
    plt.xlabel("Board Size (N)")
    plt.ylabel("Average Time (seconds)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# This function draws the checks plot.
def plot_checks(N, checks, title):
    plt.figure()
    plt.plot(N, checks)
    plt.xlabel("Board Size (N)")
    plt.ylabel("Average Constraint Checks")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():

    print("====== Algorithm Performance Visualizer ======\n")

    while True:

        # user chooses which algorithm results they want to see
        print("Choose an algorithm to visualize:")
        print("1. Backtracking")
        print("2. Forward Checking")
        print("3. MAC")
        print("4. Exit")

        algo_choice = input("Your choice: ")

        if algo_choice == "4":
            print("Exiting...")
            break

        algo_map = {"1": "Backtracking", "2": "Forward Checking", "3": "MAC"}

        # invalid input
        if algo_choice not in algo_map:
            print("Invalid choice.\n")
            continue

        algo = algo_map[algo_choice]
        data = results[algo]

        print(f"\n{algo} selected.\n")

        # user picks what plot they want to see
        print("Choose a plot to display:")
        print("1. Average Time vs N")
        print("2. Average Checks vs N")
        print("3. Back")

        plot_choice = input("Your choice: ")

        if plot_choice == "1":
            plot_time(data["N"], data["avg_times"], f"{algo} – Average Time vs N")

        elif plot_choice == "2":
            plot_checks(data["N"], data["avg_checks"], f"{algo} – Average Checks vs N")

        elif plot_choice == "3":
            continue

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
