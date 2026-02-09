import subprocess
import settings

def execute_experiment(experiment1):
    time_value_command = "date +%s"
    network_value_command = f"cat /sys/class/net/{settings.network_types[experiment1.network]}/statistics/rx_bytes"
    battery_value_command = f"upower -i /org/freedesktop/UPower/devices/{settings.battery_types[experiment1.battery]} | grep 'energy:' | awk '{{print $2}}' | sed 's/Wh//g'"

    experiment1.set_time_start(int(subprocess.check_output(time_value_command, shell=True).decode().strip()))
    experiment1.set_network_start(int(subprocess.check_output(network_value_command, shell=True).decode().strip()))
    experiment1.set_battery_start(float(subprocess.check_output(battery_value_command, shell=True).decode().strip()))

    wait_time = int(experiment1.length) * 60
    print(f"Running experiment for {wait_time} seconds...")
    subprocess.run(f"sleep {wait_time}", shell=True)

    experiment1.set_time_end(int(subprocess.check_output(time_value_command, shell=True).decode().strip()))
    experiment1.set_network_end(int(subprocess.check_output(network_value_command, shell=True).decode().strip()))
    experiment1.set_battery_end(float(subprocess.check_output(battery_value_command, shell=True).decode().strip()))

    print("Experiment completed.\nRESULTS:\n")
    print("Battery consumption:", experiment1.return_battery_consumption(), "Wh")
    print("Network consumption:", experiment1.return_network_consumption(), "bytes")
#    print("\nExperiment details:", experiment1)
