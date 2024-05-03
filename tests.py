import unittest
from game_state import GameState 

class TestGrowthFactorCalculation(unittest.TestCase):
    def setUp(self):
        """Setup the game state with neutral values for all attributes."""
        self.game_state = GameState()
        self.game_state.ghoomba_aggressiveness = 5  # Neutral value
        self.game_state.environment_hostility = 5   # Neutral value
        self.game_state.lifespan = 100              # Neutral value
        self.game_state.luck = 5                    # Neutral value

    def test_base_growth_factor(self):
        """Test that the base growth factor is correctly calculated with neutral attributes."""
        # Set attributes to neutral values
        self.game_state.ghoomba_aggressiveness = 5
        self.game_state.environment_hostility = 5
        self.game_state.lifespan = 100
        self.game_state.luck = 5
        self.assertEqual(self.game_state.determine_growth_factor(), 0.0027)

    def test_aggressiveness_influence(self):
        """Test that increasing Ghoomba Aggressiveness increases the growth factor."""
        # Only change the attribute under test
        self.game_state.ghoomba_aggressiveness = 10
        expected_growth_factor = 0.0027 + (10 - 5) * 0.0001
        actual_growth_factor = self.game_state.determine_growth_factor()
        self.assertAlmostEqual(actual_growth_factor, expected_growth_factor, places=5)



    def test_hostility_influence(self):
        """Test that increasing Environment Hostility decreases the growth factor."""
        self.game_state.environment_hostility = 10
        eh_adjustment = (10 - 5) * -0.0001  # EH_WEIGHT is -0.0001
        expected_growth_factor = 0.0027 + eh_adjustment
        actual_growth_factor = self.game_state.determine_growth_factor()
        self.assertAlmostEqual(actual_growth_factor, expected_growth_factor, places=5)

    
    def test_lifespan_influence(self):
        """Test that increasing Lifespan slightly increases the growth factor."""
        self.game_state.lifespan = 150
        expected_growth_factor = 0.0027 + (150 - 100) * 0.00001
        self.assertAlmostEqual(self.game_state.determine_growth_factor(), expected_growth_factor, places=5)
    

    def test_luck_influence(self):
        """Test that increasing Luck increases the growth factor."""
        self.game_state.luck = 10
        expected_growth_factor = 0.0027 + (10 - 5) * 0.00005
        self.assertEqual(self.game_state.determine_growth_factor(), expected_growth_factor)





if __name__ == '__main__':
    unittest.main()
