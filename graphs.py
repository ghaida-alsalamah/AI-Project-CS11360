import matplotlib.pyplot as plt

# Here we store the testing results for each algorithm.
results = {
    "Backtracking": {
        "N": [4, 8, 16, 20],
        "avg_times": [0.0769, 2.5729, 796.6400, 5166.2863],
        "avg_checks": [179, 6593, 6859329, 43609592]
    },

    "Forward Checking": {
        "N": [4, 8, 16, 20, 32, 64],
        "avg_times": [0.1500, 0.7571, 4.4687, 9.0303, 34.9870, 437.6198],
        "avg_checks": [108, 1329, 15117, 34480, 193259, 2892255]
    },

    "MAC": {
        "N": [4, 8, 16, 20, 32, 64],
        "avg_times": [0.1078, 1.1622, 8.2347, 18.5038, 82.4607, 2119.9937],
        "avg_checks": [107, 2146, 30426, 65983, 400092, 6326681]
    }
}



# This function draws the time plot.
def plot_time(N, times, title):
    plt.figure()
    plt.plot(N, times)
    plt.yscale("log")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Average Time (ms)")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# This function draws the checks plot.
def plot_checks(N, checks, title):
    plt.figure()
    plt.plot(N, checks)
    plt.yscale("log")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Average Constraint Checks")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# This function comparison of average times for all algorithms.
def plot_all_times(results):
    plt.figure()
    for name, data in results.items():
        plt.plot(data["N"], data["avg_times"], marker='o', label=name)
    plt.yscale("log")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Average Time (ms)")
    plt.title("Comparison: Average Time vs N")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# This function comparison of average checks for all algorithms.
def plot_all_checks(results):
    plt.figure()
    for name, data in results.items():
        plt.plot(data["N"], data["avg_checks"], marker='o', label=name)
    plt.yscale("log")
    plt.xlabel("Board Size (N)")
    plt.ylabel("Average Constraint Checks")
    plt.title("Comparison: Average Checks vs N")
    plt.grid(True)
    plt.legend()
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
        print("3. Compare ALL Times")
        print("4. Compare ALL Checks")
        print("5. Back")

        plot_choice = input("Your choice: ")

        if plot_choice == "1":
            plot_time(data["N"], data["avg_times"], f"{algo} – Average Time vs N")

        elif plot_choice == "2":
            plot_checks(data["N"], data["avg_checks"], f"{algo} – Average Checks vs N")

        elif plot_choice == "3":
            plot_all_times(results)
        elif plot_choice == "4":
            plot_all_checks(results)

        elif plot_choice == "5":
            continue

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
