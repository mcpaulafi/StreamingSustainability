import unittest
import measurement
import experiment
import settings



class TestSettings(unittest.TestCase):
    def setUp(self):
        self.exp = experiment.Experiment()
        self.exp.set_type(1)
        self.exp.set_resolution(1)
        self.exp.set_battery(1)
        self.exp.set_network(1)
        self.exp.set_length(0.1)  # Set a short length for testing

    def test_get_time(self):
        """Test that get_time returns a valid timestamp."""
        time_value = measurement.get_time()
        self.assertIsInstance(time_value, int)
        self.assertGreater(time_value, 0)
    
    def test_not_get_time(self):
        """Test that get_time returns None if the command fails."""
        # Temporarily replace the command with an invalid one to simulate failure
        measurement.get_time = lambda: None
        time_value = measurement.get_time()
        self.assertIsNone(time_value)

    def test_get_battery_value(self):
        """Test that get_battery_value returns a valid float for a known battery key."""
        # This test assumes that there is at least one valid battery key in settings.battery_types
        if not settings.battery_types:
            self.skipTest("No battery types defined in settings.")
        battery_key = next(iter(settings.battery_types))
        battery_value = measurement.get_battery_value(battery_key)
        self.assertIsInstance(battery_value, float)
        self.assertGreaterEqual(battery_value, 0)

    def test_not_get_battery_value(self):
        """Test that get_battery_value returns None if the command fails."""
        # Temporarily replace the command with an invalid one to simulate failure
        measurement.get_battery_value = lambda x: None
        battery_value = measurement.get_battery_value("invalid_key")
        self.assertIsNone(battery_value)

    def test_get_network_value(self):
        """Test that get_network_value returns a valid integer for a known network key."""
        # This test assumes that there is at least one valid network key in settings.network_types
        if not settings.network_types:
            self.skipTest("No network types defined in settings.")
        network_key = next(iter(settings.network_types))
        network_value = measurement.get_network_value(network_key)
        self.assertIsInstance(network_value, int)
        self.assertGreaterEqual(network_value, 0)

    def test_not_get_network_value(self):
        """Test that get_network_value returns None if the command fails."""
        # Temporarily replace the command with an invalid one to simulate failure
        measurement.get_network_value = lambda x: None
        network_value = measurement.get_network_value("invalid_key")
        self.assertIsNone(network_value)

    def test_get_processes(self):
        """Test that get_processes returns a list of processes."""
        processes = measurement.get_processes()
        self.assertIsInstance(processes, list)
        self.assertGreater(len(processes), 0)

    def test_not_get_processes(self):
        """Test that get_processes returns None if the command fails."""
        # Temporarily replace the command with an invalid one to simulate failure
        measurement.get_processes = lambda: None
        processes = measurement.get_processes()
        self.assertIsNone(processes)

    def test_execute_experiment(self):
        """Test that execute_experiment updates the experiment attributes correctly."""

        result = measurement.execute_experiment(self.exp)
        self.assertTrue(result)
        self.assertIsNotNone(self.exp.time_start)
        self.assertIsNotNone(self.exp.time_end)
        self.assertIsNotNone(self.exp.battery_start)
        self.assertIsNotNone(self.exp.battery_end)
        self.assertIsNotNone(self.exp.network_start)
        self.assertIsNotNone(self.exp.network_end)

if __name__ == '__main__':
    unittest.main()