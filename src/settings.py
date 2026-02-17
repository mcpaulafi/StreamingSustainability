import subprocess
import os

# Fixed values for settings
experiment_types = {1: "YleAreena", 2: "YouTube", 3: "Disney+",
                    4: "Other service", 5: "None"}
resolution_types = {1: "Lowest", 2: "Middle", 3: "Highest"}
length_types = {1: "1 minute", 2: "2 minutes", 5: "5 minutes"}
#interval_types = {10: "10 seconds", 20: "20 seconds"}

# Values retrieved from the system
battery_types = {}
network_types = {}

def find_energy_sources():
    """Find out energy sources of the computer"""
    result = subprocess.run(["upower", "-e"], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        print("Error finding energy sources:", result.stderr)
        return
    key = 1
    for line in result.stdout.splitlines():
        line = line.replace("/org/freedesktop/UPower/devices/", "")
        battery_types[key] = line
        key += 1
    #print("Battery types:", battery_types)
    return
find_energy_sources()

def find_network_interfaces():
    """Find out network interfaces of the computer"""
    if not os.path.exists("/sys/class/net"):
        print("Network interfaces directory not found.")
        return
    key = 1
    for iface in os.listdir("/sys/class/net"):
        network_types[key] = iface
        key += 1
    return
find_network_interfaces()

def choose_experiment_type() -> str:
    """Prompts the user to select an experiment type from the available options."""
    print("Select experiment type:")
    for k, v in experiment_types.items():
        print(f"  {k}: {v}")
    while True:
        try:
            choice = int(input("Enter number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice in experiment_types:
            return choice
        print("Choice not in available experiment types; try again.")

def choose_resolution() -> str:
    """Prompts the user to select a resolution from the available options."""
    print("Select resolution:")
    for k, v in resolution_types.items():
        print(f"  {k}: {v}")
    while True:
        try:
            choice = int(input("Enter number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice in resolution_types:
            return choice
        print("Choice not in available resolution types; try again.")

def return_resolution_types() -> dict:
    """Returns the available resolution types."""
    return resolution_types

def choose_battery()-> str:
    """Prompts the user to select a battery type from the available options."""
    print("Select battery type:")
    for k, v in battery_types.items():
        print(f"  {k}: {v}")
    while True:
        try:
            choice = int(input("Enter number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice in battery_types:
            return choice
        print("Choice not in available battery types; try again.")

def choose_network() -> str:
    """Prompts the user to select a network type from the available options."""
    print("Select network type:")
    for k, v in network_types.items():
        print(f"  {k}: {v}")
    while True:
        try:
            choice = int(input("Enter number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice in network_types:
            return choice
        print("Choice not in available network types; try again.")

def choose_length() -> str:
    """Prompts the user to select an experiment length from the available options."""
    print("Select experiment length:")
    for k, v in length_types.items():
        print(f"  {k}: {v}")
    while True:
        try:
            choice = int(input("Enter number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice in length_types:
            return choice
        print("Choice not in available length types; try again.")
