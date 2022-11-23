"""
Exercise 3
5.0/5.0 points (graded)
Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the lengths of the strings. Return float('NaN') if L is empty.

Recall that the standard deviation is computed by this equation:

where:

 is the mean of the elements in X.

 means the sum of the quantity  for t in X.

That is, for each element (that we name t) in the set X, we compute the quantity . We then sum up all those computed quantities.

N is the number of elements in X.

Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.

Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 11:40:20 2022

@author: AnnaGerasimenko
"""

import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import numpy as np
L = ['apples', 'oranges', 'kiwis', 'pineapples']

import math


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    lengths = []
    for element in L:
        lengths.append(len(element))
    #sum_of_the_elements = sum(lengths)
    mu = np.mean(lengths)
    x = [abs(i - mu)**2 for i in lengths]
    std = math.sqrt(np.mean(x))
    return std
    

        
