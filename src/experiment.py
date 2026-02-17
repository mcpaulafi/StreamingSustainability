from datetime import datetime
import settings
# pylint: disable=too-many-instance-attributes

class Experiment:
    """Parent class for all experiments. Contains common methods and attributes."""

    def __init__(self):
        self.id = datetime.now().strftime("%Y%m%d%H%M")
        self.type = None
        self.resolution = None
        self.battery = None
        self.network = None
        self.length = None
        self.time_start = 0
        self.time_end = 0
        self.battery_start = 0
        self.battery_end = 0
        self.network_start = 0
        self.network_end = 0

    def set_type(self, type1):
        self.type = type1

    def set_resolution(self, resolution):
        self.resolution = resolution

    def set_battery(self, battery):
        self.battery = battery

    def set_network(self, network):
        self.network = network

    def set_length(self, length):
        self.length = length

    def set_time_start(self, time_start):
        self.time_start = time_start

    def set_time_end(self, time_end):
        self.time_end = time_end

    def set_battery_start(self, battery_start):
        self.battery_start = battery_start

    def set_battery_end(self, battery_end):
        self.battery_end = battery_end

    def set_network_start(self, network_start):
        self.network_start = network_start

    def set_network_end(self, network_end):
        self.network_end = network_end

    def return_battery_consumption(self):
        return self.battery_start - self.battery_end

    def return_network_consumption(self):
        return self.network_end - self.network_start

    def return_time_start(self):
        dt = datetime.fromtimestamp(int(self.time_start))
        return str(dt) # e.g. 2026-02-16 14:40:50

    def return_time_end(self):
        dt = datetime.fromtimestamp(int(self.time_end))
        return str(dt) # e.g. 2026-02-16 14:40:50

    def results(self):
        return {
            "id": self.id,
            "type": settings.experiment_types.get(self.type, "Unknown"),
            "resolution": settings.resolution_types.get(self.resolution, "Unknown"),
            "battery": settings.battery_types.get(self.battery, "Unknown"),
            "network": settings.network_types.get(self.network, "Unknown"),
            "length": settings.length_types.get(self.length, "Unknown"),
            "time_start": self.return_time_start(),
            "time_end": self.return_time_end(),
            "battery_start": self.battery_start,
            "battery_end": self.battery_end,
            "network_start": self.network_start,
            "network_end": self.network_end,
            "battery_consumption": self.return_battery_consumption(),
            "network_consumption": self.return_network_consumption()
        }

    def __str__(self):
        time_start = self.time_start
        battery_consumption = self.return_battery_consumption()
        network_consumption = self.return_network_consumption()
        return f"Experiment(id={self.id}, \
        \ntype={self.type}, \
        \nresolution={self.resolution}, \
        \nbattery={self.battery}, \
        \nnetwork={self.network}, \
        \nlength={self.length}, \
        \ntime_start={time_start}, \
        \nbattery_consumption={battery_consumption}, \
        \nnetwork_consumption={network_consumption})"
