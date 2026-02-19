import sys
from pathlib import Path
from datetime import datetime
import csv
import experiment
import settings
import measurement

experiment_list = []

def start_experiment(exp: experiment.Experiment):
    """Starts the experiment after user confirmation."""
    if input("Start experiment (y/n): ").strip().lower() != "y":
        return False
    return measurement.execute_experiment(exp)

def save_results(experiments: list):
    """Saves the experiment results to a CSV file if user confirms.
    Saves results in a 'results/' directory with a filename based on the experiment ID.
    Saves experiment class attributes and results in a human-readable format."""

    if experiments is None or len(experiments) == 0:
        print("No experiments to save.")
        return False

    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    file_id = datetime.now().strftime("%Y%m%d%H%M")
    file_type = settings.experiment_types.get(experiments[0].type, "Unknown") if experiments else "Unknown"
    filename = results_dir / f"experiment_{file_type[0:5]}_{file_id}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=experiments[0].get_parameters())
        writer.writeheader()
        for exp in experiments:
            writer.writerow(exp.results())
    print(f"Results saved to {filename}")
    return True

# Test if energy and network values are accessible and working
if not measurement.get_time():
    print("Time value from bash not accessible. Exiting.")
    sys.exit()

if not settings.find_energy_sources():
    print("Energy sources not found. Exiting.", settings.find_energy_sources())
    sys.exit()

if not settings.find_network_interfaces():
    print("Network interfaces not found. Exiting.")
    sys.exit()

# Main execution flow
while True:
    print("\nEXPERIMENT SETTINGS")
    # Ask user to select experiment parameters.
    exp_type = settings.choose_experiment_type()
    exp_battery = settings.choose_battery()
    # Check if battery value is accessible before proceeding with the experiment.
    if measurement.get_battery_value(exp_battery) is None:
        print("Battery value not accessible. Exiting.")
        sys.exit()
    exp_network = settings.choose_network()
    # Check if network value is accessible before proceeding with the experiment.
    if measurement.get_network_value(exp_network) is None:
        print("Network value not accessible. Exiting.")
        sys.exit()
    exp_length = settings.choose_length()

    for res in settings.resolution_types:
        # Loop all resolutions for the selected experiment parameters.
        experiment1 = experiment.Experiment()
        experiment1.set_type(exp_type)
        experiment1.set_battery(exp_battery)
        experiment1.set_network(exp_network)
        experiment1.set_length(exp_length)
        experiment1.set_resolution(res)
        experiment1.get_basic_settings()

        print("\nSTART STREAMING: ", settings.experiment_types.get(exp_type, "Unknown"), " ",
              settings.resolution_types.get(res, "Unknown"))

        # Start experiment and save results if it was executed successfully.
        if start_experiment(experiment1):
            experiment_list.append(experiment1)
            print("\tBattery consumption:", experiment1.return_battery_consumption(), "Wh")
            print("\tNetwork consumption:", experiment1.return_network_consumption(), "bytes")
            if res == max(settings.resolution_types.keys()):
                break
            if input("Continue experiment (y/n): ").lower() != "y":
                break
        else:
            print("Experiment execution was ended, failed or was not started.")
            break

    save_results(experiment_list)

    break

print("\nEND.")
