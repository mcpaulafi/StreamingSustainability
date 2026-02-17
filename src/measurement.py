import subprocess
import time
import settings

def get_time():
    """Gets the current time as a timestamp from the bash command."""
    time_value_command = "date +%s"
    time_stamp = int(subprocess.check_output(time_value_command, shell=True).decode().strip())
    if time_stamp <= 0:
        print("Error getting time value.")
        return None
    return time_stamp

def get_battery_value(battery_key):
    """Gets the current battery energy value in Wh for the specified battery key."""
    battery_value_command = (
        f"upower -i /org/freedesktop/UPower/devices/"
        f"{settings.battery_types[battery_key]} | grep 'energy:' | "
        f"awk '{{print $2}}' | sed 's/Wh//g'"
    )
    try:
        battery_value = float(subprocess.check_output(battery_value_command,
                        shell=True).decode().strip())
        return battery_value
    except (subprocess.CalledProcessError, ValueError) as e:
        print("Error getting battery value:", e)
        return None

def get_network_value(network_key):
    """Gets the current network received bytes value for the specified network key."""
    network_value_command = (
        f"cat /sys/class/net/{settings.network_types[network_key]}"
        f"/statistics/rx_bytes"
    )
    try:
        network_value = int(subprocess.check_output(network_value_command,
                        shell=True).decode().strip())
        return network_value
    except (subprocess.CalledProcessError, ValueError) as e:
        print("Error getting network value:", e)
        return None

def get_processes():
    """Gets the list of processes running on the system."""
    processes_command = "ps -eo pid,cmd,%cpu,%mem --sort=-%cpu | awk 'NR==1 || $3+0 > 1'"
    try:
        processes_output = subprocess.check_output(processes_command, shell=True).decode()
        processes = processes_output.splitlines(keepends=True)
        return processes
    except subprocess.CalledProcessError as e:
        print("Error getting processes:", e)
        return None


def execute_experiment(experiment1):
    """Executes the experiment by measuring time, network, and battery 
    values before and after a sleep period based on the experiment length."""

    experiment1.set_time_start(get_time())

    experiment1.set_network_start(get_network_value(experiment1.network))
    experiment1.set_battery_start(get_battery_value(experiment1.battery))
    experiment1.set_processes(get_processes())

    wait_time = int(experiment1.length) * 60
    print(f"Running experiment for {wait_time} seconds...")
    # If there is significant difference between bash time and python time counting,
    # we can use this sleep method instead of while loop.
#    subprocess.run(f"sleep {wait_time}", shell=True, check=True)

    remaining = wait_time

    while remaining > 0:
        step = min(15, remaining)
        time.sleep(step)
        remaining -= step
        print(f"{remaining} seconds left..")

    experiment1.set_time_end(get_time())

    experiment1.set_network_end(get_network_value(experiment1.network))
    experiment1.set_battery_end(get_battery_value(experiment1.battery))

    return True
