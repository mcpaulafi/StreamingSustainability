import subprocess
import os

experiment_types = {1: "YleAreena", 2: "YouTube", 3: "Disney+", 
                    4: "Other service", 5: "None"}
resolution_types = {1: "Lowest", 2: "Middle", 3: "Highest"}
battery_types = {}
network_types = {}
length_types = {1: "1 minute", 2: "2 minutes", 5: "5 minutes"}
interval_types = {10: "10 seconds", 20: "20 seconds"}


def find_energy_sources():
    """Find out energy sources of the computer"""
    result = subprocess.run(["upower", "-e"], capture_output=True, text=True)
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

def choose_battery()-> str:
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

def choose_intervals() -> str:
    print("Select measurement intervals:")
    for k, v in interval_types.items():
        print(f"  {k}: {v}")
    while True:
        try:
            choice = int(input("Enter number: ").strip())
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice in interval_types:
            return choice
        print("Choice not in available interval types; try again.")
