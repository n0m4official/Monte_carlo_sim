import random
from collections import Counter
import matplotlib.pyplot as plt

def monte_carlo_sim():
    print("=== Monte Carlo Sim ===")
    print("\n=== Made by Mathew Dixon ===")
    
    user_input = input("\nEnter items separated by commas (e.g., apple, banna, cherry): ")
    items = [item.strip() for item in user_input.split(",") if item.strip()]

    if not items:
        print("You must enter at least one item.")
        return
    
    try:
        num_trials = int(input("Enter number of trials to run (e.g., 10000): "))
        if num_trials <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a positive integer for the number of trials.")
        return
    
    results = random.choices(items, k=num_trials)

    counts = Counter(results)

    print(f"\nResults after {num_trials} trials:")
    percentages = []
    for item in items:
        count = counts[items]
        percentage = (count / num_trials) * 100
        percentages.append(percentage)
        print(f"{item}: {count} times ({percentage:.2f}%)")
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(items, percentages, color='skyblue', edgecolor='black')
    plt.title("Monte Carlo Simulation Results", fontsize=16)
    plt.xlabel("Items", fontsize=12)
    plt.ylabel("percentage Selected (%)", fontsize=12)
    plt.ylim(0, max(percentages) + 10)

    for bar, percent in zip(bars, percentages):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{percent:.2f}%",
                 ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()

    save = input("Do you want to save the graph as an image? (yes/no): ").strip().lower()
    if save == "yes":
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "monte_carlo_results"
        plt.savefig(f"{filename}.png")
        print(f"Graph saved as '{filename}.png'.")

    plt.show()

if __name__ == "__main__":
    monte_carlo_sim()