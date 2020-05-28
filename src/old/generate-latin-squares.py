'''
generate-latin-squares.py
'''

import copy

from latin_squares import has_unit, has_inverses, is_commutative, is_associative

n = 5 # number of elements

carrier = list(range(0,n)) # [0,1,... n-1]
table = [['x' for y in carrier] for y in carrier] # each row and column will be a permutation of carrier
available = [[ [] for y in carrier] for x in carrier] # elements available to build table

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
        new_table = copy.deepcopy(table)
        new_table[x][y] = z
        new_available = copy.deepcopy(available)
        for i in small_carrier:
            new_available[x][i] = [a for a in available[x][i] if a != z]
            new_available[i][y] = [a for a in available[i][y] if a != z]
        if not ( x == n-1 and y == n-1 ):
            generate(next_x(x,y), next_y(x,y), new_table, new_available)
        else: 
            print('')
            print('latin square found')
            print_table(new_table)
            latin_squares.__init__(carrier,new_table)
            if has_inverses():
                print_table(new_table)
                print('has inverses')
                if is_commutative:
                    print('is commutative')
                    if is_associative():
                        print('is associative')
                    #else:
                    #    test_associative()
            '''
            if is_half_associative() and not is_associative():
                print('is half associative, not associative')
            if not has_inverses() and is_half_associative():
                print('does not have inverses and is half associative')
            '''

# size 6: half_associative implies has_inverses, half_associative implies associative
generate(1,1, table, available)




