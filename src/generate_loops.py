'''
generate_loops.py
A loop is a square table with elements taken from the list [0,...,n-1] such
  - first row and column are identical to the list
  - all rows and columns are permutations of the list (such a square is known as a latin square)
More mathematical, a loop is a quasi-group with a neutral element.

compared to generate_loops1, here table is passed by reference, save approx 25% runtime on n=6
'''

import copy
from Group import *

n = 6 # number of elements

carrier = list(range(0,n)) # [0,1,... n-1]
small_carrier = list(range(0,n)) # [1,... n-1]
table = [['x' for y in carrier] for y in carrier] # each row and column will be a permutation of carrier
available = [[ [] for y in small_carrier] for x in small_carrier] # elements available to build table

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

# all tables must have the carrier as first row and first column
for x in carrier:
    table[0][x]=x
    table[x][0]=x

# at the beginning all elements are available for all positions
# with the exception that table[x][y] cannot contain x or y
# since x is already in row x and y is already in column y
for x in small_carrier:
    for y in small_carrier:
        available[x-1][y-1] = [a for a in carrier if a!=x and a!= y] # python lists are indexed from 0

# we will iterate through all positions of the table with the help of next
def next_x(x,y):
    if y < n-1:
        return x
    elif x < n-1 and y == n-1:
        return x+1
    else:
        print('Error in next_x(): variable x out of bounds:', x)

def next_y(x,y):
    if y < n-1:
        return y+1
    elif x < n-1 and y == n-1:
        return 1
    else:
        print('Error in next_y(): variable y out of bounds:', y)

# generate all possible tables and check their properties
def generate(x,y,table,available):
    for z in available[x-1][y-1]:
        # new_table = copy.deepcopy(table)
        table[x][y] = z
        new_available = copy.deepcopy(available)
        for i in small_carrier:
            new_available[x-1][i] = [a for a in available[x-1][i] if a != z]
            new_available[i][y-1] = [a for a in available[i][y-1] if a != z]
        if not ( x == n-1 and y == n-1 ):
            generate(next_x(x,y), next_y(x,y), table, new_available)
        else: 
            # print('')
            # print('loop found')
            # print_table(new_table)
            init(carrier,0,table)
            # fill in your code
# size 6: half_associative implies has_inverses, half_associative implies associative
generate(1,1, table, available)




