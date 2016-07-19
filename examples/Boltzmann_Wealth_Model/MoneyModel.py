#combine sheilling with this one

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

import random

class MoneyAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.wealth = 1

    def step(self, model):
        if self.wealth == 0:
            return
        other_agent = random.choice(model.schedule.agents)
        other_agent.wealth += 1
        self.wealth -= 1

class MoneyModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()

# from mesa import Agent, Model
# from mesa.time import RandomActivation
# from mesa.space import MultiGrid

# from mesa.datacollection import DataCollector

# import random

# def compute_gini(model):
#     agent_wealths = [agent.wealth for agent in model.schedule.agents]
#     x = sorted(agent_wealths)
#     N = model.num_agents
#     B = sum( xi * (N-i) for i,xi in enumerate(x) ) / (N*sum(x))
#     return (1 + (1/N) - 2*B)


# class MoneyModel(Model):
#     """A model with some number of agents."""
#     def __init__(self, N, width, height):
#         self.num_agents = N
#         self.running = True
#         self.grid = MultiGrid(height, width, True)
#         self.schedule = RandomActivation(self)
#         self.datacollector = DataCollector(model_reporters={"Gini": compute_gini},
#                 agent_reporters={"Wealth": lambda a: a.wealth})
#         # Create agents
#         for i in range(self.num_agents):
#             a = MoneyAgent(i)
#             self.schedule.add(a)
#             # Add the agent to a random grid cell
#             x = random.randrange(self.grid.width)
#             y = random.randrange(self.grid.height)
#             self.grid.place_agent(a, (x, y))

#     def step(self):
#         self.datacollector.collect(self)
#         self.schedule.step()
    
#     def run_model(self, n):
#         for i in range(n):
#             self.step()

# class MoneyAgent(Agent):
#     """ An agent with fixed initial wealth."""
#     def __init__(self, unique_id):
#         self.unique_id = unique_id
#         self.wealth = 1

#     def move(self, model):
#         possible_steps = model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
#         new_position = random.choice(possible_steps)
#         model.grid.move_agent(self, new_position)

#     def give_money(self, model):
#         cellmates = model.grid.get_cell_list_contents([self.pos])
#         if len(cellmates) > 1:
#             other = random.choice(cellmates)
#             other.wealth += 1
#             self.wealth -= 1

#     def step(self, model):
#         self.move(model)
#         if self.wealth > 0:
#             self.give_money(model)
