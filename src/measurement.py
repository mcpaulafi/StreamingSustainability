import subprocess
import settings

def execute_experiment(experiment1):
    """Executes the experiment by measuring time, network, and battery 
    values before and after a sleep period based on the experiment length."""
    #TODO: Consider which time value is most relevant for reporting
    time_value_command = "date +%s"
    network_value_command = (
        f"cat /sys/class/net/{settings.network_types[experiment1.network]}"
        f"/statistics/rx_bytes"
    )
    battery_value_command = (
        f"upower -i /org/freedesktop/UPower/devices/"
        f"{settings.battery_types[experiment1.battery]} | grep 'energy:' | "
        f"awk '{{print $2}}' | sed 's/Wh//g'"
    )

    experiment1.set_time_start(
        int(subprocess.check_output(time_value_command, shell=True).decode().strip())
    )
    experiment1.set_network_start(
        int(subprocess.check_output(network_value_command, shell=True).decode().strip())
    )
    experiment1.set_battery_start(
        float(subprocess.check_output(battery_value_command, shell=True).decode().strip())
    )

    wait_time = int(experiment1.length) * 60
    print(f"Running experiment for {wait_time} seconds...")
    subprocess.run(f"sleep {wait_time}", shell=True, check=True)

    experiment1.set_time_end(
        int(subprocess.check_output(time_value_command, shell=True).decode().strip())
    )
    experiment1.set_network_end(
        int(subprocess.check_output(network_value_command, shell=True).decode().strip())
    )
    experiment1.set_battery_end(
        float(subprocess.check_output(battery_value_command, shell=True).decode().strip())
    )

    # TODO: If consumption is negative or zero, promt an error
    return True
