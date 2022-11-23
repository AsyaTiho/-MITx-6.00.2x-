###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict

# Problem 1
def greedy_cow_transport(cows,limit=10):
    trips = []
    temp = []       
    ship = []
    totalweight = 0
    cows_sorted = sorted(cows.items(), key = lambda cows : cows[1], reverse = True)
    while len(temp)< len(cows_sorted):
        for i in range(len(cows_sorted)):
            if cows_sorted[i] not in temp:
                if cows_sorted[i][1] + totalweight <= limit:
                    ship.append(cows_sorted[i][0])
                    temp.append(cows_sorted[i])
                    totalweight += cows_sorted[i][1]
                    
        trips.append(ship)
        ship = []
        totalweight = 0
    return trips
        

    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trips = []
    potential_trips = []
    every_part = sorted(get_partitions(cows), key = len)
    for partions in every_part:
        ship =[]
        for list1 in partions:
            weights = []
            for w in list1:
                weights.append(cows[w])
                # print(weights)
            ship.append(sum(weights))
        if all(el <= limit for el in ship):
            potential_trips.append(partions)
    clean_trips = []
    [clean_trips.append(x) for x in potential_trips if x not in clean_trips] 
    min_len = min(map(len, clean_trips))
    print(min_len)
    for y in clean_trips:
        if len(y)==min_len:
            return y

        
# Problem 3
def compare_cow_transport_algorithms():
    cows={'Maggie':3,'Herman':7,'Betsy':9, 'Oreo':6, 'Moo Moo': 3, 'Milkshake':2, 'Millie':5, 'Lola':2, 'Florence':2,'Henrietta':9}

    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    test_greedy = greedy_cow_transport(cows,limit=10)
    print(test_greedy)
    end = time.time()
    print(end - start)
    
    start = time.time()
    test_brute = brute_force_cow_transport(cows,limit=10)
    print(test_brute)
    end = time.time()
    print(end - start)



"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


