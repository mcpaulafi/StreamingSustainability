from pathlib import Path
from datetime import datetime
import csv
import experiment
import settings
import measurement

def start_experiment(exp: experiment.Experiment):
    """Starts the experiment after user confirmation."""
    if input("Start experiment (y/n): ").strip().lower() != "y":
        return False
    return measurement.execute_experiment(exp)

def print_experiment_parameters(exp: experiment.Experiment):
    """Prints the selected experiment parameters in a human-readable format."""
    print("\nSELECTED PARAMETERS:")
    print("\tType:", settings.experiment_types.get(exp.type, "Unknown"))
    print("\tBattery:", settings.battery_types.get(exp.battery, "Unknown"))
    print("\tNetwork:", settings.network_types.get(exp.network, "Unknown"))
    print("\tLength:", settings.length_types.get(exp.length, "Unknown"))
    print("\tResolution:", settings.resolution_types.get(exp.resolution, "Unknown"))
    return

def save_results(experiments):
    """Saves the experiment results to a CSV file if user confirms.
    Saves results in a 'results/' directory with a filename based on the experiment ID.
    Saves experiment class attributes and results in a human-readable format."""

    fieldnames = [
        "id", "type", "resolution", "battery", "network", "length",
        "time_start", "time_end", "battery_start", "battery_end",
        "network_start", "network_end", "battery_consumption",
        "network_consumption"
    ]
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    file_id = datetime.now().strftime("%Y%m%d%H%M")
    filename = results_dir / f"experiment_{file_id}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for exp in experiments:
            writer.writerow(exp.results())
    print(f"Results saved to {filename}")
    return True

# Main execution flow
# Ask user to select experiment parameters.

experiments = []

while True:
    exp_type = settings.choose_experiment_type()
    exp_battery = settings.choose_battery()
    exp_network = settings.choose_network()
    exp_length = settings.choose_length()

    for res in settings.resolution_types:
        """Loop all resolutions for the selected experiment parameters."""
        experiment1 = experiment.Experiment()
        experiment1.set_type(exp_type)
        experiment1.set_battery(exp_battery)
        experiment1.set_network(exp_network)
        experiment1.set_length(exp_length)
        experiment1.set_resolution(res)
        print_experiment_parameters(experiment1)

        print("\nSTART STREAMING: ", settings.experiment_types.get(exp_type, "Unknown"), " ",
              settings.resolution_types.get(res, "Unknown"))

        if start_experiment(experiment1):
            experiments.append(experiment1)
            print("\tBattery consumption:", experiment1.return_battery_consumption(), "Wh")
            print("\tNetwork consumption:", experiment1.return_network_consumption(), "bytes")
            if input("Continue experiment? (y/n): ").lower() != "y":
                break

        else:
            print("Experiment execution failed or was not started.")
            break

    
    save_results(experiments)

    break

print("\nEND.")
