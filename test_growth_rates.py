import random
import unittest
from game_view import display_population

class GameState:
    def __init__(self):
        self.year = 0
        self.population = 1000
        self.ghoomba_aggressiveness = 5
        self.environment_hostility = 5
        self.lifespan = 100
        self.luck = self.randomize_luck()
        self.current_growth_rate = 0.0027  # Initial growth rate, neutral conditions

    def randomize_luck(self):
        return random.randint(1, 10)

    def simulate_years(self, years):
        for _ in range(years):
            self.update_year()
            self.update_population()

    def update_year(self):
        self.year += 1

    def update_population(self):
        self.current_growth_rate = self.determine_growth_factor()
        self.population = max(self.population * (1 + self.current_growth_rate), 0)

    def determine_growth_factor(self):
        GA_WEIGHT = 0.0015
        EH_WEIGHT = -0.0015
        LS_WEIGHT = 0.000001
        LK_WEIGHT = 0.0015
        base_growth_rate = 0.0027
        ga_adjustment = (self.ghoomba_aggressiveness - 5) * GA_WEIGHT
        eh_adjustment = (self.environment_hostility - 5) * EH_WEIGHT
        ls_adjustment = (self.lifespan - 100) * LS_WEIGHT
        lk_adjustment = (self.luck - 5) * LK_WEIGHT
        return base_growth_rate + ga_adjustment + eh_adjustment + ls_adjustment + lk_adjustment

class TestPopulationGrowth(unittest.TestCase):
    def test_population_growth_at_intervals(self):
        game_state = GameState()
        intervals = [100, 200, 500, 700, 1000, 1500, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        current_interval_index = 0

        # Set example attributes for testing
        game_state.ghoomba_aggressiveness = 5
        game_state.environment_hostility = 5
        game_state.lifespan = 100
        game_state.luck = 5

        while game_state.year < max(intervals):
            game_state.simulate_years(1)
            if game_state.year == intervals[current_interval_index]:
                display_population(game_state.year, game_state.population, game_state.current_growth_rate)
                if current_interval_index < len(intervals) - 1:
                    current_interval_index += 1

if __name__ == '__main__':
    unittest.main()
