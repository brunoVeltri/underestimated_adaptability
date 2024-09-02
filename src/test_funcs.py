# %%
from utility_functions import pure_random_utility, monotonic_random_utility, concave_random_utility
from utility_functions import normalize_utility_function, plot_utility_function_2d
import numpy as np
from solve import solve_quasilin_utility_maximization



# %%
params = {
    'nb_goods': 2,
    'max_good_amount': 10,
    'max_utility_value': 2000
}

prices = np.array([4, 4])
budget = 100

#%%
# generate utility function
utility_function = concave_random_utility(params)
utility_function = normalize_utility_function(utility_function, params)


# plot 2d slice of utility function
plot_utility_function_2d(utility_function, params)

#%%
# solve before price change
prices = np.array([4, 4])
amount, utility = solve_quasilin_utility_maximization(utility_function, prices, budget)
print("Amounts: ", amount)
print("Utility: ", utility)
# solve after price change
prices = np.array([4, 7])
amount, utility = solve_quasilin_utility_maximization(utility_function, prices, budget)
print("Amounts: ", amount)
print("Utility: ", utility)
# %%
