
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def pure_random_utility(params):
    '''Generate a utility function with random values and integer support.'''
    # unpack params
    nb_goods = params['nb_goods']
    nb_choices_per_good = params['max_good_amount'] + 1
    max_utility_value = nb_goods * nb_choices_per_good * params['max_utility_increment']
    # populate utility function with random values
    utility_values = np.zeros((nb_choices_per_good,)*nb_goods)
    for i in range(nb_choices_per_good**nb_goods):
        utility_values.flat[i] = np.random.randint(0, max_utility_value)
    return utility_values


def monotonic_random_utility(params):
    '''Generate a monotonous increasing utility function with random values and integer support.'''
    # unpack params
    nb_goods = params['nb_goods']
    max_good_amount = params['max_good_amount'] + 1 
    max_utility_increment = 10000 # arbitrary value
    # populate utility function with random values
    utility_values = np.zeros((max_good_amount,)*nb_goods)
    for index in np.ndindex(utility_values.shape):
        if index == (0,)*nb_goods:
            utility_values[index] = 0
        else:
            parent_indeces = get_parent_indices(index)
            utility_values[index] = max([utility_values[parent_index] for parent_index in parent_indeces]) + np.random.randint(1, max_utility_increment)
    return utility_values
        

def concave_random_utility(params):
    # unpack params
    nb_goods = params['nb_goods']
    max_good_amount = params['max_good_amount'] + 1
    max_utility_increment = 10000 # arbitrary value
    # populate utility function with random values
    utility_values = np.zeros((max_good_amount,)*nb_goods)
    for index in np.ndindex(utility_values.shape):
        if index == (0,)*nb_goods:
            utility_values[index] = 0
        else:
            parent_indeces = get_parent_indices(index)
            min_utility = max([utility_values[parent_index] for parent_index in parent_indeces])
            max_local_increment = get_max_delta(index, utility_values, max_utility_increment)
            if max_local_increment == 1:
                utility_values[index] = min_utility + 1
            else:
                utility_values[index] = min_utility + np.random.randint(1, max_local_increment)
    return utility_values

def get_parent_indices(index):
    parent_indeces = []
    for i, value in enumerate(index):
        if value != 0:
            new_index = list(index)
            new_index[i] -= 1
            parent_indeces.append(tuple(new_index))
    return parent_indeces    

def get_max_delta(index, utility, max_utility_increment):
    ''' Get the discret equivalent of the maximum marginal utility 
    at a given index so that the function is still concave.'''
    deltas = []
    for parent in get_parent_indices(index):
        good_change_vector = np.array(index) - np.array(parent)
        relevant_grandparent = np.array(parent) - good_change_vector
        if all(relevant_grandparent >= 0):
            deltas.append(utility[parent] - utility[tuple(relevant_grandparent)])
    return max(deltas, default=max_utility_increment)

def normalize_utility_function(utility_function, params):
    '''Normalize the utility function to the interval [0, max_utility_value].'''
    max_utility_value = params['max_utility_value']
    utility_function -= utility_function.min()
    utility_function /= utility_function.max()
    utility_function *= max_utility_value
    return utility_function

#%%
# plot
def plot_utility_function_2d(utility_function, params):
    '''Plot a 2D slice of the utility function.'''
    max_good_amount = params['max_good_amount'] + 1
    # keep only first two dimensions
    utility_function_2d = utility_function.sum(axis=tuple(range(2, utility_function.ndim)))

    # create a grid of x and y values
    x = np.arange(max_good_amount)
    y = np.arange(max_good_amount)
    X, Y = np.meshgrid(x, y)

    # create a contour plot
    plt.contourf(X, Y, utility_function_2d, cmap='viridis')
    plt.colorbar()  # add a colorbar
    plt.xlabel('Good 1')
    plt.ylabel('Good 2')
    plt.title('2D slice of utility function')
    plt.show()