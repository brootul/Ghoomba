from events import CATASTROPHES, DIVINE_INTERVENTIONS, DivineIntervention, Catastrophe
import random

class GameState:
    def __init__(self):
        self.year = 0
        self.population = 1000  # Starting population
        self.ghoomba_aggressiveness = 5
        self.environment_hostility = 5
        self.lifespan = 100
        self.luck = self.randomize_luck()  # Initialize luck randomly
        self.catastrophes = CATASTROPHES
        self.divine_interventions = DIVINE_INTERVENTIONS

    def randomize_luck(self):
        return random.randint(1, 10)

    def advance_year(self):
        """Advance the simulation by a given number of years."""
        self.year += 1
        self.update_population()

    

    def determine_growth_factor(self):
        """Determine the growth factor based on the attributes."""
        # Constants to define the sensitivity of growth to each attribute
        GA_WEIGHT = 0.0015
        EH_WEIGHT = -0.0015
        LS_WEIGHT = 0.000001
        LK_WEIGHT = 0.0015

        # Calculate adjustments based on attributes
        ga_adjustment = (self.ghoomba_aggressiveness - 5) * GA_WEIGHT
        eh_adjustment = (self.environment_hostility - 5) * EH_WEIGHT
        ls_adjustment = (self.lifespan - 100) * LS_WEIGHT
        lk_adjustment = (self.luck - 5) * LK_WEIGHT

        # Base growth rate as determined
        base_growth_rate = 0.0027

        # Combine all factors to determine the growth factor for the year
        growth_factor = base_growth_rate + ga_adjustment + eh_adjustment + ls_adjustment + lk_adjustment
        return growth_factor


    def update_population(self):
        """Updates the population based on the current growth rate."""
        # Get the current growth rate
        growth_rate = self.determine_growth_factor()
    
        # Apply the growth rate to update the population
        self.population *= (1 + growth_rate)
    
        # Ensure population does not go negative or below a realistic threshold
        self.population = max(self.population, 0)


    def maybe_trigger_random_catastrophe(self):
        """Determine randomly if a catastrophe occurs with a flat 1% chance, and then select which catastrophe based on their individual probabilities."""
        if random.random() < 0.008:  # 1% chance for any catastrophe to happen
            # Select which catastrophe occurs based on individual probabilities
            probabilities = [catastrophe.probability for catastrophe in self.catastrophes]
            selected_catastrophe = random.choices(self.catastrophes, weights=probabilities, k=1)[0]
        
            # Execute the selected catastrophe
            original_population = self.population
            self.population = selected_catastrophe.execute_catastrophe(self.population)
        
            # Calculate the percentage of population reduced
            population_reduced = original_population - self.population
            reduction_percentage = (population_reduced / original_population) * 100

            # Print detailed report of the catastrophe
            print(f"Catastrophe '{selected_catastrophe.name}' occurred in the year {self.year}, reducing population by {reduction_percentage:.2f}%.")
            print(f"Total population after the event: {self.population}.")

            return True
        return False
            


    def trigger_random_catastrophe(self, catastrophe):
        """Trigger a specific catastrophe and apply its effects, reporting the details of the impact."""
        # Store the original population to calculate the impact later
        original_population = self.population

        # Execute the passed catastrophe
        self.population = Catastrophe.execute_catastrophe(self.population)

        # Calculate the percentage of population reduced
        population_reduced = original_population - self.population
        reduction_percentage = (population_reduced / original_population) * 100

        # Print the detailed report of the catastrophe
        print(f"Catastrophe '{Catastrophe.name}' occurred in the year {self.year}, reducing population by {reduction_percentage:.2f}%.")
        print(f"Total population after the event: {self.population}.")

    
    def trigger_specific_catastrophe(self, catastrophe_name):
        catastrophe = next((cat for cat in self.catastrophes if cat.name == catastrophe_name), None)
        if catastrophe:
            self.population = catastrophe.execute_catastrophe(self.population)
            print(f"Catastrophe '{catastrophe.name}' has been triggered, reducing the population.")
        else:
            print("Catastrophe not found.")


    def trigger_divine_intervention(self, intervention_name):
        """Manually trigger a divine intervention by name."""
        intervention = next((di for di in DIVINE_INTERVENTIONS if di.name == intervention_name), None)
        if intervention:
            self.population = intervention.execute_divine_intervention(self.population)
            print(f"Divine intervention '{intervention.name}' occurred, increasing population to {self.population}")
        else:
            print("No such divine intervention found.")
            raise ValueError("No such divine intervention found.")