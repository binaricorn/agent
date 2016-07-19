
# The below is needed for both notebooks and scripts
import matplotlib.pyplot as plt
from MoneyModel import *

model = MoneyModel(100)
for i in range(50):
    model.step()

# all_wealth = []
# for j in range(100):
#     # Run the model
#     model = MoneyModel(10)
#     for i in range(10):
#         model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_wealth.append(agent.wealth)

agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)
#plt.hist(all_wealth, bins=range(max(all_wealth)+1))
plt.show()