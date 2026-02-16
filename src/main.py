from pathlib import Path
from . import experiment
from . import settings
from . import measurement

def start_experiment(experiment1: experiment.Experiment):
    """Starts the experiment after user confirmation."""
    if input("Type 'y' to begin experiment, 'n' to exit: ").strip().lower() != "y":
        print("Experiment not started. Exiting.")
        return
    measurement.execute_experiment(experiment1)
    save_results(input("Type 'y' to save results: ").strip().lower(), experiment1)
    return

def save_results(input_value: str, experiment1: experiment.Experiment):
    """Saves the experiment results to a file if user confirms.
    Saves results in a 'results' directory with a filename based on the experiment ID.
    Saves experiment class attributes and results in a human-readable format."""
    #TODO: Save as JSON or CSV for easier parsing later.
    if input_value.strip().lower() != "y":
        print("Results not saved.")
        return
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    filename = results_dir / f"experiment_{experiment1.id}.txt"
    with open(filename, "w") as f:
        f.write(str(experiment1.results()))
        print(f"Results saved to {filename}")

# Main execution flow
# Ask user to select experiment parameters.
#TODO: Add error handling for user input and file operations.
experiment1 = experiment.Experiment()
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

start_experiment(experiment1)

print("\nEND.")
