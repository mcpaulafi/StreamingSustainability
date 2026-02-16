import unittest
from unittest.mock import patch
import src.settings as settings

class TestSettings(unittest.TestCase):
    def test_battery_and_network_detection(self):
        """Test that battery and network types are detected (may be empty if not found)."""
        self.assertIsInstance(settings.battery_types, dict)
        self.assertIsInstance(settings.network_types, dict)

    @patch("builtins.input", side_effect=["2"])
    def test_valid_type_value(self, mock_input):
        """Test that valid input returns correct choice."""
        result = settings.choose_experiment_type()
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["xxx", "8", "3"])
    def test_invalid_then_valid(self, mock_input):
        """Test behavior with invalid inputs first"""
        result = settings.choose_experiment_type()
        self.assertEqual(result, 3)

    @patch("builtins.input", side_effect=["2"])
    def test_valid_resolution_value(self, mock_input):
        """Test that valid input returns correct choice."""
        result = settings.choose_resolution()
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["2"])
    def test_valid_battery_value(self, mock_input):
        """Test that valid input returns correct choice."""
        result = settings.choose_battery()
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["2"])
    def test_valid_network_value(self, mock_input):
        """Test that valid input returns correct choice."""
        result = settings.choose_network()
        self.assertEqual(result, 2)

    @patch("builtins.input", side_effect=["2"])
    def test_valid_length_value(self, mock_input):
        """Test that invalid input prompts again and valid input is accepted."""
        result = settings.choose_length()
        self.assertEqual(result,2)

if __name__ == "__main__":
    unittest.main()
