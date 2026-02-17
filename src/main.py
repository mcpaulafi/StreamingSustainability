from pathlib import Path
import csv
import experiment
import settings
import measurement

experiment1 = experiment.Experiment()

def start_experiment(exp: experiment.Experiment):
    """Starts the experiment after user confirmation."""
    if input("Type 'y' to begin experiment, 'n' to exit: ").strip().lower() != "y":
        return False
    return measurement.execute_experiment(exp)


def save_results(input_value: str, exp: experiment.Experiment):
    """Saves the experiment results to a CSV file if user confirms.
    Saves results in a 'results/' directory with a filename based on the experiment ID.
    Saves experiment class attributes and results in a human-readable format."""

    if input_value.strip().lower() != "y":
        print("Results not saved.")
        return False

    fieldnames = [
        "id", "type", "resolution", "battery", "network", "length",
        "time_start", "time_end", "battery_start", "battery_end",
        "network_start", "network_end", "battery_consumption",
        "network_consumption"
    ]
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    filename = results_dir / f"experiment_{exp.id}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(exp.results())
        #writer.writerow({k: getattr(exp, k, "") for k in fieldnames})
    print(f"Results saved to {filename}")
    return True

# Main execution flow
# Ask user to select experiment parameters.
#TODO: Add error handling for user input and file operations.

experiment1.set_type(settings.choose_experiment_type())
experiment1.set_resolution(settings.choose_resolution())
experiment1.set_battery(settings.choose_battery())
experiment1.set_network(settings.choose_network())
experiment1.set_length(settings.choose_length())

# Print selected parameters for confirmation before starting the experiment.
print("Selected experiment type:", experiment1.type)
print("Selected resolution:", experiment1.resolution)
print("Selected battery:", experiment1.battery)
print("Selected network:", experiment1.network)
print("Selected length:", experiment1.length)

print("\nREADY TO START EXPERIMENT. Start streaming.")

if start_experiment(experiment1):
    print("Battery consumption:", experiment1.return_battery_consumption(), "Wh")
    print("Network consumption:", experiment1.return_network_consumption(), "bytes")
    save_results(input("Type 'y' to save results: ").strip().lower(), experiment1)
else:
    print("Experiment execution failed or was not started.")

print("\nEND.")
