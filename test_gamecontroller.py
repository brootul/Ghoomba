import unittest
from unittest.mock import MagicMock, patch
from game_controller import GameController

class TestGameController(unittest.TestCase):
    def setUp(self):
        """Mock dependencies and initialize GameController."""
        with patch('game_controller.GameState') as MockGameState, \
             patch('game_controller.GameView') as MockGameView:
            self.mock_game_state = MockGameState()
            self.mock_game_view = MockGameView()
            self.controller = GameController()
            self.controller.game_state = self.mock_game_state
            self.controller.game_view = self.mock_game_view

            # Set up return values for mocked attributes
            self.mock_game_state.year = 0
            self.mock_game_state.population = 1000

    def test_run_initialization(self):
        """Test that the game initialization process is correct."""
        self.mock_game_view.get_valid_input.return_value = 5
        self.mock_game_state.randomize_luck.return_value = 7
        self.controller.run()
        self.mock_game_view.display_welcome_message.assert_called_once()
        self.assertEqual(self.mock_game_state.ghoomba_aggressiveness, 5)
        self.assertEqual(self.mock_game_state.environment_hostility, 5)
        self.assertEqual(self.mock_game_state.lifespan, 5)
        self.assertEqual(self.mock_game_state.luck, 7)

    

    @patch('builtins.input', side_effect=['show population', 'exit'])
    def test_run_terminates_properly(self, mock_input):
        """Test that the run method processes commands and exits."""
        self.controller.run()
        self.assertTrue(self.controller.game_state.year >= 10000 or not self.controller.keep_running)
        self.mock_game_view.display_population.assert_called()  # Assuming this would be called after 'show population'

    def test_game_termination_logic(self):
        """Ensure the game loop can terminate under the right conditions."""
        self.mock_game_state.year = 10000
        self.mock_game_state.population = 1  # Ensuring it does not hit population-based termination
        with patch('builtins.input', side_effect=['exit']):
            self.controller.run()  # This should not hang as 'exit' triggers termination
        self.mock_game_view.display_game_over_message.assert_called_once()



if __name__ == '__main__':
    unittest.main()
