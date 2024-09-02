# %%
from src.utility_functions import pure_random_utility, monotonic_random_utility, plot_utility_function_2d
import numpy as np
from src.solve import solve_quasilin_utility_maximization



# %%
params = {
    'nb_goods': 2,
    'max_good_amount': 5,
    'max_utility_increment': 10
}

prices = np.array([1, 1])
budget = 10

#%%
utility_function = monotonic_random_utility(params)
#plot_utility_function_2d(utility_function, params)
amount, utility = solve_quasilin_utility_maximization(utility_function, prices, budget)

# %%
