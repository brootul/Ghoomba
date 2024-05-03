from game_state import GameState
from game_view import GameView
from events import Catastrophe, CATASTROPHES, DivineIntervention, DIVINE_INTERVENTIONS

class GameController:
    def __init__(self):
        self.game_state = GameState()
        self.game_view = GameView(self.game_state)

    
    def run(self):
        """Start the main game loop with detailed flow."""
        self.game_view.display_welcome_message()
        self.collect_initial_values()
        self.confirm_initial_values()

        game_over = False

        while self.game_state.year < 10000 and not game_over:
            self.simulate_growth()  # Simulate growth and update the game state
            self.game_view.display_stats(
                self.game_state.year, 
                self.game_state.population, 
                self.game_state.determine_growth_factor(),
                self.game_state.ghoomba_aggressiveness,
                self.game_state.environment_hostility,
                self.game_state.lifespan
            )

            if self.game_state.population <= 10 or self.game_state.population >= 999e12:
                game_over = True
                continue

            # Check for and potentially handle a random catastrophe
            if self.game_state.maybe_trigger_random_catastrophe():
                self.game_state.trigger_random_catastrophe()
                self.game_view.display_stats(
                    self.game_state.year, 
                    self.game_state.population, 
                    self.game_state.determine_growth_factor(),
                    self.game_state.ghoomba_aggressiveness,
                    self.game_state.environment_hostility,
                    self.game_state.lifespan
                )

            # Prompt for adjustments and confirm if needed
            if self.prompt_for_adjustments() and not self.confirm_adjustments():
                continue  # Skip to next iteration if adjustments are not confirmed

            # Handle events based on user interaction
            self.handle_event_trigger()

        self.display_game_over_message()


    def handle_event_trigger(self):
        """Handles the triggering of specific events based on user choice."""
        if self.game_view.prompt_for_event():  # Prompt for event and check if the user wants to trigger an event
            event_type = self.game_view.get_event_type()  # Get the type of event to trigger
            if event_type == "catastrophe":
                catastrophe_name = self.select_event(self.game_state.catastrophes)
                if catastrophe_name:
                    self.game_state.trigger_specific_catastrophe(catastrophe_name)
            elif event_type == "divine intervention":
                intervention_name = self.select_event(self.game_state.divine_interventions)
                if intervention_name:
                    self.game_state.trigger_divine_intervention(intervention_name)




    def collect_initial_values(self):
        """Collects initial values for GA, EH, and LS, and generates LK."""
        self.game_state.ghoomba_aggressiveness = self.game_view.get_valid_input("Enter Ghoomba Aggressiveness (1-10): ", 1, 10)
        self.game_state.environment_hostility = self.game_view.get_valid_input("Enter Environment Hostility (1-10): ", 1, 10)
        self.game_state.lifespan = self.game_view.get_valid_input("Enter Lifespan (years): ", 1, 999e99)
        self.game_state.luck = self.game_state.randomize_luck()

    def confirm_initial_values(self):
        """Displays and confirms the initial values set by the player."""
        self.game_view.display_initial_values(self.game_state.ghoomba_aggressiveness,
                                              self.game_state.environment_hostility,
                                              self.game_state.lifespan,
                                              self.game_state.luck)

    def simulate_growth(self, years=100):
        """Simulate growth over a given number of years, silently updating the game state."""
        for _ in range(years):
            self.game_state.advance_year()  # Update the year and population based on growth rates


    def prompt_for_adjustments(self):
        # Ask the user if they want to make adjustments
        if not self.game_view.confirm("Would you like to make any adjustments? (yes/no): "):
            print("No adjustments will be made. Continuing simulation...")
            return False  # Indicates no adjustments were made

        self.adjust_game_state()
        return True  # Indicates adjustments were made
            
            

    def adjust_game_state(self):
        """Prompts the user to adjust game settings."""
        new_ga = self.game_view.get_valid_input("Adjust Ghoomba Aggressiveness (1-10): ", 1, 10)
        new_eh = self.game_view.get_valid_input("Adjust Environment Hostility (1-10): ", 1, 10)
        new_ls = self.game_view.get_valid_input("Adjust Lifespan (years): ", 1, 999e99)  # Assuming no upper limit
        
        # Apply adjustments if confirmed
        if self.game_view.confirm("Confirm these changes? (yes/no): "):
            self.game_state.ghoomba_aggressiveness = new_ga
            self.game_state.environment_hostility = new_eh
            self.game_state.lifespan = new_ls
            print("Changes confirmed. Adjustments applied.")
        else:
            print("Changes not confirmed. Keeping previous settings.")


    def confirm_adjustments(self):
        """Displays and gets confirmation on the new values after adjustments."""
        print("\nYou have entered the following adjustments:")
        print(f"Ghoomba Aggressiveness: {self.game_state.ghoomba_aggressiveness}")
        print(f"Environment Hostility: {self.game_state.environment_hostility}")
        print(f"Lifespan: {self.game_state.lifespan} years")
    
        if self.game_view.confirm("Are these adjustments correct? (yes/no): "):
            print("Adjustments confirmed.")
        else:
            print("Adjustments not confirmed. Reverting to previous values.")
            self.prompt_for_adjustments()  # Optionally, ask for re-entry if not confirmed


    def trigger_event(self, event):
        # Assuming the event object has a method to execute it
        new_population = event.execute_catastrophe(self.game_state.population) if isinstance(event, Catastrophe) \
            else event.execute_divine_intervention(self.game_state.population)
        self.game_state.population = new_population
        print(f"Event '{event.name}' executed, new population: {self.game_state.population}")


    def handle_event_trigger(self):
        if self.game_view.prompt_for_event():
            event_type = self.game_view.get_event_type()  # Should return 'catastrophe' or 'divine intervention'
            if event_type == 'catastrophe':
                catastrophe_name = self.select_catastrophe()
                if catastrophe_name:
                    self.game_state.trigger_specific_catastrophe(catastrophe_name)
            elif event_type == 'divine intervention':
                intervention_name = self.select_divine_intervention()
                if intervention_name:
                    self.game_state.trigger_divine_intervention(intervention_name)


    def select_catastrophe(self):
        # Assuming self.game_state.catastrophes has been properly populated
        print("Available Catastrophes:")
        for index, cat in enumerate(self.game_state.catastrophes, start=1):
            print(f"{index}. {cat.name}")
        index = int(input("Select a catastrophe by number: "))
        return self.game_state.catastrophes[index - 1].name

    def select_divine_intervention(self):
        # Similar logic for divine interventions
        print("Available Divine Interventions:")
        for index, di in enumerate(self.game_state.divine_interventions, start=1):
            print(f"{index}. {di.name}")
        index = int(input("Select a divine intervention by number: "))
        return self.game_state.divine_interventions[index - 1].name



    def select_event(self, events):
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event.name}")
        choice = input("Please select an event by number: ")
        try:
            selected_index = int(choice) - 1
            return events[selected_index].name
        except (IndexError, ValueError):
            print("Invalid selection.")
            return None
        

    def trigger_event_from_list(self, event_type):
        if event_type == 'catastrophe':
            self.list_and_trigger_event(self.game_state.catastrophes)  # Use the list from GameState or directly
        elif event_type == 'divine intervention':
            self.list_and_trigger_event(self.game_state.divine_interventions)

    def list_and_trigger_event(self, events):
        # Logic to list events and trigger the selected one
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event.name}")
        # Assume user selects an event
        selected_index = int(input("Select an event by number: ")) - 1
        selected_event = events[selected_index]
        self.trigger_event(selected_event)

    def post_event_actions(self):
        """Perform any actions that need to occur after an event is processed."""
        # For example, update the game view or log event results
        self.game_view.display_event_result(self.game_state.population)


    def display_game_over_message(self):
        """Displays the appropriate game over message based on the end conditions."""
        if self.game_state.population <= 10:
            self.game_view.display_message("Your population has gone extinct.")
        elif self.game_state.population >= 999e12:
            self.game_view.display_message("Congratulations! Your population has thrived and reached a tremendous size.")
        else:
            self.game_view.display_message("You've reached the year 10000. Let's see how you did!")

    def exit_game(self):
        """Handle game exit."""
        self.game_view.display_stats("Thank you for playing!")
        return False  # Signal to exit the main loop







if __name__ == "__main__":
    controller = GameController()
    controller.run()
