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
    

        