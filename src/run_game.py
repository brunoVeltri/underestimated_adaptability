from utility_functions import pure_random_utility, monotonic_random_utility, concave_random_utility
import numpy as np
from utility_functions import pure_random_utility, monotonic_random_utility
from solve import solve_quasilin_utility_maximization


def prompt_developer_settings(params, utility_function, prices):
    print("DEVELOPER SETTINGS:")
    print("Would you like to overwrite the default parameters? (y/n)")

    overwrite = input()
    if overwrite == 'y':
        print("Please enter the number of goods:")
        params['nb_goods'] = int(input())
        print("Please enter the maximum amount per good:")
        params['max_good_amount'] = int(input())
        print("Please enter the maximum marginal utility:")
        params['max_utility_increment'] = int(input())

print("Would you like to overwrite the default utility function? (y/n)")
overwrite = input()
if overwrite == 'y':
    print("You can choose between the following utility functions:")
    print("1: Unrestricted")
    print("2: Monotonic")
    print("3: Concave")
    utility_function_choice = int(input())
    if utility_function_choice == 1:
        utility_function = pure_random_utility(params)
    elif utility_function_choice == 2:
        utility_function = monotonic_random_utility(params)
    elif utility_function_choice == 3:
        utility_function = concave_random_utility(params)
    else:
        utility_function = monotonic_random_utility(params)

    print("Would you like to overwrite the default prices? (y/n)")
    overwrite = input()
    if overwrite == 'y':
        print("Please enter the prices for each good:")
        for i in range(params['nb_goods']):
            prices[i] = int(input("Price for good " + str(i) + ": "))
    
    return params, utility_function, prices

def print_instructions(params):
    print("INSTRUCTIONS:")
    print("Welcome to the game!")
    print("This game consists of " + str(params['nb_rounds']) + " rounds.")
    print("In each round, you will choose a basket of goods to buy. Your payoff depends on the utility you derive from the goods and the money you have left.")
    print("You have a budget of " + str(budget) + " every round. All remaining money will be added to your payoff.")
    print("There are " + str(params['nb_goods']) + " goods. Each good can be bought in quantities from 0 to " + str(params['max_good_amount']) + ". \n")
    print("The game starts now. \n")

def purchasing_loop(params, utility_function, prices, budget):
    payoffs = [0] * params['nb_rounds']
    for round in range(params['nb_rounds']):
        print("Round " + str(round + 1) + ":")
        print("The prices are: " + str(prices))
        print("Please enter the quantities for each good:")
        quantities = np.zeros(params['nb_goods'])
        for i in range(params['nb_goods']):
            j = i + 1
            quantities[i] = int(input("Quantity of good " + str(j) + " (at price " + str(prices[i]) + "): "))
        expenditure = np.sum(prices * quantities)
        int_quantities = tuple(quantities.astype(int).tolist())
        utility = utility_function[int_quantities]
        payoff = budget - expenditure + utility
        print("\n")
        print("You bought goods for a total cost of " + str(np.sum(prices * quantities)) + ", which gives you a utility of " + str(utility) + ".")
        print("Your total payoff this round is " + str(payoff) + ".")
        print("--------------------")
        print("\n")
        payoffs[round] = payoff
    return payoffs



# set params, utility function, prices and budget
params = {
    'nb_goods': 3,
    'max_good_amount': 10,
    'max_utility_increment': 10,
    'nb_rounds': 10
}
utility_function = monotonic_random_utility(params)
prices = np.array(np.random.randint(1, params['max_utility_increment'], params['nb_goods']))
budget = params['max_good_amount'] * params['nb_goods'] * params['max_utility_increment']
developer_settings = False

if developer_settings:
    params, utility_function, prices = prompt_developer_settings(params, utility_function, prices)

# Game 
print_instructions(params)
payoffs = purchasing_loop(params, utility_function, prices, budget)
optimal_amounts, utility = solve_quasilin_utility_maximization(utility_function, prices, budget)
print("The payoffs for each round are: " + str(payoffs) + ".")
print("The optimal basket is: " + str(optimal_amounts) + " with a total payoff of " + str(utility) + ".")
print("Thank you for playing!")