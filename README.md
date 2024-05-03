OVERVIEW

Welcome to Planet Ghoomba! This is a simulation theory simulator that will test the viability of the Ghoomba species. You begin the game by assigning difficulty levels to various attributes. This will set the overall Ghoobma population growth rate. Next the simulation begins. You will have the opportunity to adjust these attributes at regular intervals in order to tweak the growth rate to your preference. If the population grows too slowly the species will go extinct. If the population grows too quickly, bad things will happen and the species will go extinct. The goal of the simulation is to have the Ghoomba species make it through 10,000 years of simulated progress. If the Ghoomba’s make it to year 10,000 you win and the population will be tallied and graded and a final score will be given.


ATTRIBUTES

You will assign a value between 1 and 10 to the first four attributes. Lifespan, luck, and growth rate are handled differently. Lifespan can be any positive number. Luck is a hidden attribute that is determined behind the scenes. Then, all of these attributes are calculated together to get the growth rate.

Environment Hostility: directly affects the growth rate with 1 being a positive factor, 5 being neutral, and 10 being a negative factor

Ghoombah Aggressiveness: inversely affects the growth rate with 1 being a negative factor, 5 being neutral, and 10 being a positive factor

Lifespan: how long before a typical Ghoomba dies of old age

Luck: some Ghoomba’s are just luckier than others (hidden stat that affects everything)

Growth Rate: determines how much the total population goes up or down each year

 
INTERACTIONS 

At specific intervals (currently every 100 simulated years) you will get a progress report that shows the current population. You will then be able to adjust the attributes (some or all, depending on the game mode chosen at the start of the simulation) before continuing the simulation. You will also be able to directly adjust the population by initiating one of two special events called Catastrophe’s and Divine Interventions. Catastrophe’s will decrease the population by a certain amount depending on the specific catastrophe and Divine Interventions will increase the population by a certain amount depending on the specific Divine Intervention. Once all of these decisions are complete the simulation will calculate the new current population and growth rate then simulate the next 100 years.


HOW TO CLONE AND RUN THIS PROGRAM 

1. Install python: sudo apt install python3
2. Clone the repository: git clone https://github.com/brootul/ghoomba.git
3. Run the main file: python main.py
