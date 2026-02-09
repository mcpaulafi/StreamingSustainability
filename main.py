import experiment
import settings
import measurement
import os
from pathlib import Path

def start_experiment(experiment1: experiment.Experiment):
    if input("Type 'y' to begin experiment: ").strip().lower() != "y":
        print("Experiment not started. Exiting.")
        return
    else:
        measurement.execute_experiment(experiment1)
        save_results(input("Type 'y' to save results: ").strip().lower(), experiment1)
    return

def save_results(input_value: str, experiment1: experiment.Experiment):
    if input_value.strip().lower() != "y":
        print("Results not saved.")
        return
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    filename = results_dir / f"experiment_{experiment1.id}.txt"
    with open(filename, "w") as f:
        f.write(str(experiment1.results()))
        print(f"Results saved to {filename}")

experiment1 = experiment.Experiment()
experiment1.set_type(settings.choose_experiment_type())
experiment1.set_resolution(settings.choose_resolution())
experiment1.set_battery(settings.choose_battery())
experiment1.set_network(settings.choose_network())
experiment1.set_length(settings.choose_length())
#experiment1.set_intervals(choose_intervals())
print("Selected experiment type:", experiment1.type)
print("Selected resolution:", experiment1.resolution)
print("Selected battery:", experiment1.battery)
print("Selected network:", experiment1.network)
print("Selected length:", experiment1.length)
# Not implemented yet
#print("Selected intervals:", experiment1.intervals, "-", settings.interval_types.get(list(settings.interval_types.keys())[list(settings.interval_types.values()).index(experiment1.intervals)]))
print("\nREADY TO START EXPERIMENT. Start streaming.")

start_experiment(experiment1)

print("\nEND.")
