# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:19:51 2022

@author: AnnaGerasimenko
"""
"""
** Playlist problem description**:
You are creating a song playlist for your next party. You have a collection of songs that can be represented as a list of tuples. Each
tuple has the following elements:
> name: the first element, representing the song name (non-empty string)
> song_length: the second, element representing the song duration (float >= 0)
> song_size: the third, element representing the size on disk (float >= 0)

You want to try to optimize your playlist to play songs for as long as possible while making sure that the songs you pick do not take
up more than a given amount of space on disk (the sizes should be less than or equal to the max_disk_size).
You decide the best way to achieve your goal is to start with the first song in the given song list. If the first song doesn't fit on
disk, return an empty list. If there is enough space for this song, add it to the playlist.

For subsequent songs, you choose the next song such that its size on disk is smallest and that the song hasn't already been chosen. You
do this until you cannot fit any more songs on the disk.

Write a function implementing this algorithm, that returns a list of the song names in the order in which they were chosen, with the
first element in the list being the song chosen first. Assume song names are unique and all the songs have different sizes on disk and
different durations.

You may not mutate any of the arguments.

For example,
If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 12.2, the function will
return ['Roar','Wannabe','Timber']
If songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)] and max_size = 11, the function will return
['Roar','Wannabe']

Paste your entire function (including the definition) in the box. Do not import anything. Do not leave any debugging print statements.
songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 11

"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    return_playlist = []
    if songs[0][2] <= max_size:
        return_playlist.append(songs[0][0])
    else:
        return return_playlist
    songs_sorted_without1st = sorted(songs[1:], key = lambda songs: songs[2], reverse =  False)
    space_left = max_size - songs[0][2]
    for i in songs_sorted_without1st:
        if i[2] <= space_left:
            return_playlist.append(i[0])
            space_left -= i[2]
    return return_playlist
    
print(song_playlist(songs, max_size))


import random
  
# You are given this function - do not modify
def createRandomGraph():
    """Creates a digraph with 7 randomly chosen integer nodes from 0 to 9 and
    randomly chosen directed edges (between 10 and 20 edges)
    """
    g = {}
    n = random.sample([0,1,2,3,4,5,6,7,8,9], 7)
    for i in n:
        g[i] = []
    edges = random.randint(10,20)
    count = 0
    while count < edges:
        a = random.choice(n)
        b = random.choice(n)
        if b not in g[a] and a != b:
            g[a].append(b)
            count += 1
    return g

# You are given this function - do not modify
def findPath(g, start, end, path=[]):
    """ Uses DFS to find a path between a start and an end node in g.
    If no path is found, returns None. If a path is found, returns the
    list of nodes """
    path = path + [start]
    if start == end:
        return path
    if not start in g:
        return None
    for node in g[start]:
        if node not in path:
            newpath = findPath(g, node, end, path)
            if newpath: return newpath
    return None
                
#########################        
## WRITE THIS FUNCTION ##
#########################        
#output = [5, 6, 7, 8, 9]

def allReachable(g, n):
    results = []
    for m in g:
        if findPath(g, n, m) != None:
            results.append(m)
    results.remove(n)
    return results

cases = [
    dict(
g = {2: [], 3: [1, 9], 4: [9, 7], 6: [4, 3], 7: [1, 3], 8: [4, 6], 9: []},
n = 2,
correct=[]
),dict(g = {0: [2], 1: [8, 3], 2: [4, 3, 8], 3: [4, 2, 0], 4: [8, 0], 5: [4, 1, 3], 8: [2, 0, 5, 3, 1]},
        n = 8, correct=[0, 1, 2, 3, 4, 5]), 
    dict(g = {0: [3, 6, 9], 1: [7], 3: [9, 1], 5: [9, 3, 1], 6: [], 7: [3, 9], 9: [1, 3, 0]}
      ,  n = 1, correct=[0, 3, 6, 7, 9]),
   dict(      g = {0: [7], 1: [9, 8], 5: [8, 6, 9], 6: [1], 7: [9], 8: [7, 5, 9], 9: [7, 5]}
       , n = 1, correct=[5, 6, 7, 8, 9]),
   dict(g = {1: [3, 4, 6, 2], 2: [8, 3], 3: [9, 1], 4: [9, 8], 6: [3], 8: [], 9: [2]},
        n = 1, correct=[2, 3, 4, 6, 8, 9]),
   dict(g = {0: [9, 2], 1: [6, 9, 2, 4], 2: [1, 9], 4: [0], 5: [0, 6, 2, 4], 6: [2, 9, 5, 4], 9: [2, 5, 4]},
        n = 0, correct=[1, 2, 4, 5, 6, 9]),
   dict(    g = {1: [8], 4: [9, 5], 5: [8, 7, 6], 6: [7, 5], 7: [6, 9], 8: [6, 7, 9], 9: [1, 6, 4]},
        n = 4, correct=[1, 5, 6, 7, 8, 9]),
   dict(g = {2: [4], 4: [7, 6], 5: [4, 6], 6: [8], 7: [5, 9, 8, 4, 2], 8: [], 9: [2, 6, 7]},
        n = 4, correct=[2, 5, 6, 7, 8, 9]),
   dict(g = {0: [3], 2: [0], 3: [7], 4: [9, 3], 5: [3, 2], 7: [2, 3], 9: [2, 4, 3]},
        n = 9, correct=[0, 2, 3, 4, 7]),
   dict(g = {0: [], 1: [], 2: [3, 8], 3: [0], 4: [5, 8], 5: [3, 2, 4, 0], 8: [5, 0]},
        n = 5, correct=[0, 2, 3, 4, 8]),
   dict(g = {1: [7], 2: [5], 4: [], 5: [1, 2, 4], 6: [4], 7: [4, 6, 1, 9], 9: [2, 6]},
        n = 5, correct=[1, 2, 4, 6, 7, 9]
        )
   ]
for case in cases:
    out = allReachable(case["g"], case["n"])
    print("out", out)
    print("Correct", case["correct"])
    

    
    

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    # IMPLEMENT THIS FUNCTION
    for i in range(0,101):
        if test(i) == True:
            return i
    for i in range(-100,0):
        if test(i) == True:
            return i
    return "not found"
        


    
