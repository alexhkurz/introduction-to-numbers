'''
generate_latin_squares.py, version 2
compared to generate_latin_squares1.py, generate() passes table by reference (on 5 elements a speed-up of 27%)
'''

import copy

from latin_squares import init, has_unit, is_commutative, is_associative

n = 5 # number of elements

carrier = list(range(0,n)) # [0,1,... n-1]
table = [['x' for y in carrier] for y in carrier] # each row and column will be a permutation of carrier
available = [[ [] for y in carrier] for x in carrier] # elements available to build table

for x in carrier:
    for y in carrier:
        available[x][y] = carrier

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

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
        return 0
    else:
        print('Error in next_y(): variable y out of bounds:', y)

# generate all possible tables and check their properties
def generate(x,y,table,available):
    for z in available[x][y]:
        table[x][y] = z # we dont need to revert changes on backtracking, recursive call be reference works
        new_available = copy.deepcopy(available) # we need to revert changes on backtracking, deepcopy needed
        for i in carrier:
            new_available[x][i] = [a for a in available[x][i] if a != z]
            new_available[i][y] = [a for a in available[i][y] if a != z]
        if not ( x == n-1 and y == n-1 ):
            generate(next_x(x,y), next_y(x,y), table, new_available)
        else: 
            init(carrier,table)
            print('')
            print_table(table)

generate(0,0, table, available)




