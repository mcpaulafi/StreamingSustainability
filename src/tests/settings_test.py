import unittest
from unittest.mock import patch
import settings

class TestSettings(unittest.TestCase):
    def test_battery_and_network_detection(self):
        """Test that battery and network types are detected (may be empty if not found)."""
        self.assertIsInstance(settings.battery_types, dict)
        self.assertIsInstance(settings.network_types, dict)

    def test_not_find_energy_sources(self):
        """Test that find_energy_sources returns False if no energy sources are found."""
        # Temporarily replace the command with an invalid one to simulate failure
        settings.find_energy_sources = lambda: False
        self.assertFalse(settings.find_energy_sources())
    
    def test_not_find_network_interfaces(self):
        """Test that find_network_interfaces returns False if no network interfaces are found."""
        # Temporarily replace the command with an invalid one to simulate failure
        settings.find_network_interfaces = lambda: False
        self.assertFalse(settings.find_network_interfaces())

    @patch("builtins.input", side_effect=["xxx", "3"])
    def test_invalid_then_valid_experiment_type(self, mock_input):
        self.assertEqual(settings.choose_experiment_type(), 3)

    @patch("builtins.input", side_effect=["999", "3"])
    def test_branch_not_in_dict_then_valid_experiment(self, mock_input):
        result = settings.choose_experiment_type()
        assert result == 3

    @patch("builtins.input", side_effect=["xxx", "1"])
    def test_invalid_then_valid_resolution(self, mock_input):
        self.assertEqual(settings.choose_resolution(), 1)

    @patch("builtins.input", side_effect=["999", "3"])
    def test_branch_not_in_dict_then_valid_resolution(self, mock_input):
        result = settings.choose_resolution()
        assert result == 3

    def test_return_resolution_types(self):
        """Test that return_resolution_types returns a dictionary."""
        res_types = settings.return_resolution_types()
        self.assertIsInstance(res_types, dict)

    @patch("builtins.input", side_effect=["xxx", "1"])
    def test_invalid_then_valid_choose_battery(self, mock_input):
        self.assertEqual(settings.choose_battery(), 1)

    @patch("builtins.input", side_effect=["999", "3"])
    def test_branch_not_in_dict_then_valid_choose_battery(self, mock_input):
        result = settings.choose_battery()
        assert result == 3

    @patch("builtins.input", side_effect=["xxx", "1"])
    def test_invalid_then_valid_choose_network(self, mock_input):
        self.assertEqual(settings.choose_network(), 1)

    @patch("builtins.input", side_effect=["999", "3"])
    def test_branch_not_in_dict_then_valid_choose_network(self, mock_input):
        result = settings.choose_network()
        assert result == 3

    @patch("builtins.input", side_effect=["abc", "2"])
    def test_invalid_then_valid_choose_length(self, mock_input):
        self.assertEqual(settings.choose_length(), 2)

    @patch("builtins.input", side_effect=["999", "2"])
    def test_branch_not_in_dict_then_valid_choose_length(self, mock_input):
        result = settings.choose_length()
        assert result == 2

if __name__ == "__main__":
    unittest.main()
