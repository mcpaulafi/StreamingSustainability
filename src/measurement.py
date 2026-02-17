import subprocess
import settings

def get_time():
    time_value_command = "date +%s"
    time_stamp = int(subprocess.check_output(time_value_command, shell=True).decode().strip())
    if time_stamp <= 0:
        print("Error getting time value.")
        return None
    return time_stamp

def get_battery_value(battery_key):
    battery_value_command = (
        f"upower -i /org/freedesktop/UPower/devices/"
        f"{settings.battery_types[battery_key]} | grep 'energy:' | "
        f"awk '{{print $2}}' | sed 's/Wh//g'"
    )
    try:
        battery_value = float(subprocess.check_output(battery_value_command, shell=True).decode().strip())
        return battery_value
    except Exception as e:
        print("Error getting battery value:", e)
        return None

def get_network_value(network_key):
    network_value_command = (
        f"cat /sys/class/net/{settings.network_types[network_key]}"
        f"/statistics/rx_bytes"
    )
    try:
        network_value = int(subprocess.check_output(network_value_command, shell=True).decode().strip())
        return network_value
    except Exception as e:
        print("Error getting network value:", e)
        return None

def execute_experiment(experiment1):
    """Executes the experiment by measuring time, network, and battery 
    values before and after a sleep period based on the experiment length."""

    network_value_command = (
        f"cat /sys/class/net/{settings.network_types[experiment1.network]}"
        f"/statistics/rx_bytes"
    )

    experiment1.set_time_start(get_time())

    experiment1.set_network_start(get_network_value(experiment1.network))
    experiment1.set_battery_start(get_battery_value(experiment1.battery))

    wait_time = int(experiment1.length) * 60
    print(f"Running experiment for {wait_time} seconds...")
    subprocess.run(f"sleep {wait_time}", shell=True, check=True)

    experiment1.set_time_end(get_time())

    experiment1.set_network_end(get_network_value(experiment1.network))
    experiment1.set_battery_end(get_battery_value(experiment1.battery))

    return True
