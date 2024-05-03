import unittest
from unittest.mock import patch
from game_state import GameState  # Adjust import as per your file and class structure
from events import Catastrophe, DivineIntervention, CATASTROPHES, DIVINE_INTERVENTIONS

'''
class TestGameStateEvents(unittest.TestCase):
    def setUp(self):
        """Initialize GameState before each test."""
        self.game = GameState()
        self.game.population = 1000  # Set a known population for predictability in tests

    def test_random_catastrophe_trigger(self):
        """Test that triggering a random catastrophe reduces the population."""
        initial_population = self.game.population
        self.game.trigger_random_catastrophe()
        # Check the population has decreased
        self.assertLess(self.game.population, initial_population)

    def test_manual_divine_intervention_trigger(self):
        """Test manually triggering a divine intervention increases the population."""
        initial_population = self.game.population
        # Example intervention name - adjust as per your actual divine intervention names
        intervention_name = "Ghoombavian Revival"
        self.game.trigger_divine_intervention(intervention_name)
        # Check the population has increased
        self.assertGreater(self.game.population, initial_population)

    def test_divine_intervention_not_found(self):
        """Test handling of non-existent divine intervention."""
        initial_population = self.game.population
        intervention_name = "Nonexistent Intervention"
        # Assuming the method to raise a ValueError if intervention is not found
        with self.assertRaises(ValueError):
            self.game.trigger_divine_intervention(intervention_name)
        # Ensure population remains unchanged if intervention is not found
        self.assertEqual(self.game.population, initial_population)


class TestRandomCatastropheChance(unittest.TestCase):
    def setUp(self):
        self.game = GameState()
        self.game.population = 1000  # Set a known initial population

    def test_random_catastrophe_trigger_probability(self):
        """Test the 10% triggering mechanism by simulating multiple trials."""
        triggered = 0
        trials = 10000
        for _ in range(trials):
            initial_population = self.game.population
            # Mock the trigger_random_catastrophe to avoid actual population change
            with patch.object(self.game, 'trigger_random_catastrophe') as mocked_method:
                self.game.maybe_trigger_random_catastrophe()
                if mocked_method.called:
                    triggered += 1
            self.game.population = 1000  # Reset population after each trial

        # Check if the trigger rate is approximately 10%
        self.assertAlmostEqual(triggered / trials, 0.1, delta=0.01)

'''


class TestGameStateCatastrophes(unittest.TestCase):
    def setUp(self):
        """Initialize GameState before each test."""
        self.game = GameState()
        self.game.population = 1000  # Set a known population for predictability in tests

    def test_trigger_specific_valid_catastrophe(self):
        """Test triggering a valid specific catastrophe reduces the population."""
        initial_population = self.game.population
        valid_catastrophe_name = CATASTROPHES[0].name  # Assuming at least one catastrophe is defined
        self.game.trigger_specific_catastrophe(valid_catastrophe_name)
        # Check the population has decreased
        self.assertLess(self.game.population, initial_population, 
                        f"Population should decrease after {valid_catastrophe_name}")

    def test_trigger_specific_invalid_catastrophe(self):
        """Test handling of non-existent catastrophe name."""
        initial_population = self.game.population
        with self.assertRaises(ValueError) as context:
            self.game.trigger_specific_catastrophe("Nonexistent Catastrophe")
        # Ensure population remains unchanged if catastrophe is not found
        self.assertEqual(self.game.population, initial_population,
                         "Population should not change when triggering a non-existent catastrophe")
        # Check that the error message is correct
        self.assertIn("Catastrophe not found", str(context.exception),
                      "Error message for non-existent catastrophe is incorrect")




if __name__ == '__main__':
    unittest.main()
