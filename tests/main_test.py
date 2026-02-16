import unittest
import experiment

class TestExperiment(unittest.TestCase):
    def setUp(self):
        self.exp = experiment.Experiment()
        self.exp.set_type(1)
        self.exp.set_resolution(1)
        self.exp.set_battery(1)
        self.exp.set_network(1)
        self.exp.set_length(1)

    def test_experiment_initialization(self):
        """Test that an Experiment object initializes correctly."""
        self.assertIsInstance(self.exp, experiment.Experiment)

    def test_default_values(self):
        """Test that default values are set correctly."""
        self.assertEqual(self.exp.type, 1)
        self.assertEqual(self.exp.resolution, 1)
