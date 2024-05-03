from events import CATASTROPHES, DIVINE_INTERVENTIONS

class GameView:
    def __init__(self, game_state):
        self.game_state = game_state

    def display_welcome_message(self):
        print("Welcome to the Game!")
        print("Type 'help' to see a list of commands.")

    def display_help(self):
        print("Available Commands:")
        print("  trigger <event_name> - Trigger a specific event.")
        print("  show population - Displays current population.")
        print("  exit - Exit the game.")

    
    def display_initial_values(self, aggressiveness, hostility, lifespan, luck):
        """Displays the initial game settings to the player and asks for confirmation."""
        print("Initial Game Settings:")
        print(f"Ghoomba Aggressiveness: {aggressiveness}")
        print(f"Environment Hostility: {hostility}")
        print(f"Lifespan: {lifespan} years")
        print(f"Luck: {luck}")
        
        # Optionally confirm these values
        return self.confirm("Are these values correct? (yes/no): ")

    def confirm_initial_values(self):
        """Displays and confirms the initial values set by the player."""
        if not self.game_view.display_initial_values(
            self.game_state.ghoomba_aggressiveness,
            self.game_state.environment_hostility,
            self.game_state.lifespan,
            self.game_state.luck
        ):
            print("Please re-enter the initial values.")
            self.collect_initial_values()  # Optionally, recollect values if not confirmed

    def confirm(self, prompt):
        """Asks the user a yes/no question and returns True for 'yes' and False for 'no'."""
        response = input(prompt).strip().lower()
        while response not in ['yes', 'no']:
            print("Invalid response. Please enter 'yes' or 'no'.")
            response = input(prompt).strip().lower()
        return response == 'yes'
    
    
    def display_population(self, year, population):
        formatted_population = self.format_population(population)
        print(f"Year: {year}, Population: {formatted_population}")


    def handle_command(self, command):
        commands = command.split()
        if commands[0] == 'trigger' and len(commands) > 1:
            self.game_state.trigger_specific_catastrophe(commands[1])
        elif commands[0] == 'show' and len(commands) > 1:
            if commands[1] == 'population':
                self.show_population()
        elif commands[0] == 'help':
            self.display_help()
        elif commands[0] == 'exit':
            print("Exiting game.")
            return False
        return True

    def main_loop(self):
        self.display_welcome_message()
        keep_running = True
        while keep_running:
            command = input("Enter command: ")
            keep_running = self.handle_command(command)

    def get_valid_input(self, prompt, min_value, max_value):
        """Prompt the user for input and validate the range and type."""
        while True:
            try:
                user_input = int(input(prompt))
                if min_value <= user_input <= max_value:
                    return user_input
                else:
                    print(f"Please enter a number between {min_value} and {max_value}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def format_population(self, number):
        if number >= 1e12:  # Trillion
            return f"{number / 1e12:.2f} trillion"
        elif number >= 1e9:  # Billion
            return f"{number / 1e9:.2f} billion"
        elif number >= 1e6:  # Million
            return f"{number / 1e6:.2f} million"
        else:
            return f"{int(number)}"  # Numbers less than a million
        

    def display_message(self, message):
        """Display a general message to the console."""
        print(message)

    
    def display_stats(self, year, population, growth_rate, ghoomba_aggressiveness, environment_hostility, lifespan):
        """Display the current statistics of the game on separate lines for clarity."""
        formatted_population = self.format_population(population)
        formatted_growth_rate = int(growth_rate * 1000)
        print(f"Year: {year}, Population: {formatted_population}, Growth Rate: {formatted_growth_rate}")
        print(f"Ghoomba Aggressiveness: {ghoomba_aggressiveness}")
        print(f"Environment Hostility: {environment_hostility}")
        print(f"Lifespan: {lifespan} years")


    def display_events(self, events):
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event.name}")
    
    def ask_for_event_trigger(self):
        return input("Would you like to trigger an event? (yes/no): ").strip().lower()
    
    def get_event_type(self):
        while True:
            event_type = input("Type of event to trigger (catastrophe/divine intervention): ").strip().lower()
            if event_type in ['catastrophe', 'divine intervention']:
                return event_type
            print("Invalid type. Please choose 'catastrophe' or 'divine intervention'.")

    
    def get_event_selection(self, event_kind):
        return input(f"Please select a {event_kind} by number: ").strip()
    
    def confirm_continue(self):
        """Asks player if they want to continue the simulation."""
        return self.confirm_continue("Continue to next cycle? (yes/no): ")
    

    def prompt_for_event(self):
        response = self.ask_yes_no("Would you like to trigger an event? (yes/no)")
        return response
    
    def list_events(self, events):
        for index, event in enumerate(events, start=1):
            print(f"{index}. {event.name}")


    def handle_event_trigger(self):
        if not self.prompt_for_event():
            print("No event will be triggered.")
            return

        event_type = self.get_event_type()
        events = self.game_state.CATASTROPHES if event_type == 'catastrophe' else self.game_state.DIVINE_INTERVENTIONS
        self.list_events(events)

        event_index = int(self.get_event_selection(event_type)) - 1
        if 0 <= event_index < len(events):
            selected_event = events[event_index]
            self.trigger_event(selected_event, event_type)
        else:
            print("Invalid selection. No event triggered.")

    def ask_yes_no(self, question):
        """Ask a yes/no question and return True for 'yes' and False for 'no'."""
        while True:
            response = input(question + " (yes/no): ").strip().lower()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")


