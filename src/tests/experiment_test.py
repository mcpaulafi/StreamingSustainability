import unittest
from datetime import datetime
import experiment
import settings

class TestExperiment(unittest.TestCase):
    def setUp(self):
        self.exp = experiment.Experiment()
        self.exp.set_type(1)
        self.exp.set_resolution(1)
        self.exp.set_battery(1)
        self.exp.set_network(1)
        self.exp.set_length(1)
        self.exp.set_time_start(1770815525)
        self.exp.set_time_end(1770815550)
        self.exp.set_battery_start(100)
        self.exp.set_battery_end(80)
        self.exp.set_network_start(50)
        self.exp.set_network_end(70)

    def test_experiment_initialization(self):
        """Test that an Experiment object initializes correctly."""
        self.assertIsInstance(self.exp, experiment.Experiment)

    def test_default_values(self):
        """Test that default values are set correctly."""
        self.assertEqual(self.exp.type, 1)
        self.assertEqual(self.exp.resolution, 1)
        self.assertEqual(self.exp.battery, 1)
        self.assertEqual(self.exp.network, 1)
        self.assertEqual(self.exp.length, 1)

    def test_set_type(self):
        """Test that set_type correctly updates the type attribute."""
        self.exp.set_type(2)
        self.assertEqual(self.exp.type, 2)

    def test_set_resolution(self):
        """Test that set_resolution correctly updates the resolution attribute."""
        self.exp.set_resolution(2)
        self.assertEqual(self.exp.resolution, 2)

    def test_set_battery(self):
        """Test that set_battery correctly updates the battery attribute."""
        self.exp.set_battery(2)
        self.assertEqual(self.exp.battery, 2)

    def test_set_network(self):
        """Test that set_network correctly updates the network attribute."""
        self.exp.set_network(2)
        self.assertEqual(self.exp.network, 2)

    def test_set_length(self):
        """Test that set_length correctly updates the length attribute."""
        self.exp.set_length(2)
        self.assertEqual(self.exp.length, 2)

    def test_set_time_start(self):
        """Test that set_time_start correctly updates the time_start attribute."""
        self.exp.set_time_start("1770815525")
        self.assertEqual(self.exp.time_start, "1770815525")

    def test_set_time_end(self):
        """Test that set_time_end correctly updates the time_end attribute."""
        self.exp.set_time_end("1770815550")
        self.assertEqual(self.exp.time_end, "1770815550")

    def test_set_battery_start(self):
        """Test that set_battery_start correctly updates the battery_start attribute."""
        self.exp.set_battery_start(100)
        self.assertEqual(self.exp.battery_start, 100)

    def test_set_battery_end(self):
        """Test that set_battery_end correctly updates the battery_end attribute."""
        self.exp.set_battery_end(80)
        self.assertEqual(self.exp.battery_end, 80)

    def test_set_network_start(self):
        """Test that set_network_start correctly updates the network_start attribute."""
        self.exp.set_network_start(50)
        self.assertEqual(self.exp.network_start, 50)

    def test_set_network_end(self):
        """Test that set_network_end correctly updates the network_end attribute."""
        self.exp.set_network_end(30)
        self.assertEqual(self.exp.network_end, 30)

    def test_return_battery_consumption(self):
        """Test that return_battery_consumption calculates correctly."""
        self.exp.set_battery_start(100)
        self.exp.set_battery_end(80)
        self.assertEqual(self.exp.return_battery_consumption(), 20)

    def test_return_network_consumption(self):
        """Test that return_network_consumption calculates correctly."""
        self.exp.set_network_start(50)
        self.exp.set_network_end(70)
        self.assertEqual(self.exp.return_network_consumption(), 20)

    def test_str_method(self):
        """Test that the __str__ method returns a string containing key information."""
        result_str = str(self.exp)
        self.assertIsInstance(result_str, str)

    def test_str_contains_key_info(self):
        """Test that the __str__ method output contains key information."""
        result_str = str(self.exp)
        self.assertIn("type=1", result_str)
        self.assertIn("resolution=1", result_str)
        self.assertIn("battery=1", result_str)
        self.assertIn("network=1", result_str)
        self.assertIn("length=1", result_str)
        self.assertIn("time_start=1770815525", result_str)
        self.assertIn("battery_consumption=20", result_str)
        self.assertIn("network_consumption=20", result_str)

    def test_results_method(self):
        """Test that the results method returns a dictionary with expected keys and values."""

        results = self.exp.results()
        self.assertIsInstance(results, dict)
        self.assertEqual(results["type"], settings.experiment_types.get(self.exp.type, "Unknown"))
        self.assertEqual(results["resolution"], settings.resolution_types.get(self.exp.resolution, "Unknown"))
        self.assertEqual(results["battery"], settings.battery_types.get(self.exp.battery, "Unknown"))
        self.assertEqual(results["network"], settings.network_types.get(self.exp.network, "Unknown"))
        self.assertEqual(results["length"], settings.length_types.get(self.exp.length, "Unknown"))
        self.assertEqual(results["time_start"], "2026-02-11 15:12:05")
        self.assertEqual(results["time_end"], "2026-02-11 15:12:30")
        self.assertEqual(results["battery_start"], 100)
        self.assertEqual(results["battery_end"], 80)
        self.assertEqual(results["network_start"], 50)
        self.assertEqual(results["network_end"], 70)
        self.assertEqual(results["battery_consumption"], 20)
        self.assertEqual(results["network_consumption"], 20)

if __name__ == "__main__":
    unittest.main()
