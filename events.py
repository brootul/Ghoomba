import random

class Catastrophe:
    def __init__(self, name, min_reduction, max_reduction, probability):
        self.name = name
        self.min_reduction = min_reduction
        self.max_reduction = max_reduction
        self.probability = probability

    def execute_catastrophe(self, current_population):
        """Randomly reduces the population based on the defined min and max reduction percentages."""
        reduction_percentage = random.uniform(self.min_reduction, self.max_reduction) / 100
        reduced_population = current_population * (1 - reduction_percentage)
        return int(reduced_population)

class DivineIntervention:
    def __init__(self, name, increase_percentage):
        self.name = name
        self.increase_percentage = increase_percentage

    def execute_divine_intervention(self, current_population):
        """Increases the population by a defined percentage."""
        increase_amount = current_population * (self.increase_percentage / 100)
        increased_population = current_population + increase_amount
        return int(increased_population)

# List of predefined Catastrophes
CATASTROPHES = [
    Catastrophe("Minor Plague", 10, 50, 12),
    Catastrophe("Minor Famine", 10, 50, 11),
    Catastrophe("Minor Conventional War", 10, 50, 10),
    Catastrophe("Minor Biological War", 10, 50, 9),
    Catastrophe("Greater Plague", 30, 70, 8),
    Catastrophe("Greater Famine", 30, 70, 7),
    Catastrophe("Greater Conventional War", 30, 70, 6),
    Catastrophe("Greater Biological War", 30, 70, 5),
    Catastrophe("Alien Annihilation", 75, 100, 1),
    Catastrophe("Global Thermonuclear War", 75, 100, 1),
    Catastrophe("Zombie Apocalypse", 75, 100, 1),
    Catastrophe("Planet Killer Asteroid", 75, 100, 1)
]

# List of predefined Divine Interventions
DIVINE_INTERVENTIONS = [
    DivineIntervention("Ghoombavian Revival", 20),
    DivineIntervention("Divine Mantle of Ghoombvation", 40),
    DivineIntervention("Heavenly Ghoombjuvenation", 60),
    DivineIntervention("Eternal Light of Ghoombservation", 80),
    DivineIntervention("Celestial Ghoombalation", 100),
    DivineIntervention("Miraculous Ghoombusto", 200)
]
