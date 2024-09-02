import numpy as np

def solve_quasilin_utility_maximization(util_func, prices, budget):
    '''Solve the utility maximization problem with quasilinear preferences, i.e. excess budget is added to utility: 
    max u(x) + y - p*x
    s.t. p*x <= y
    Solution method: brute force.'''
    # unpack params
    nb_goods = len(prices)
    max_good_amount = util_func.shape[0]
    # solve via brute force (allows for non-monotonic/ non-concave utility functions)
    utility = 0
    for i in range(max_good_amount**nb_goods):
        basket = np.unravel_index(i, (max_good_amount,)*nb_goods)
        excess_budget = budget - np.dot(prices, basket)
        if excess_budget < 0:
            continue
        basket_utility = util_func[basket] + excess_budget
        if basket_utility > utility:
            highest_utility = basket_utility
            optimal_amounts = np.array(basket)

    return optimal_amounts, highest_utility