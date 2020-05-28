'''
Verify whether op is a group operation on carrier
'''

import itertools

def init(mycarrier, myunit, mytable):
    global carrier
    carrier = mycarrier
    global unit
    unit = myunit
    global table
    table = mytable

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

# TEST GROUP STRUCTURE AND PRINT COUNTEREXAMPLES

def test_associative():
    result = True
    for x,y,z in itertools.product(carrier, repeat=3):
        if table[x][table[y][z]]!=table[table[x][y]][z]:
            result = False
            print('violates associativity: (',x, y,')', z,'=', table[table[x][y]][z], ' and ' , x, '(', y, z, ')','=', table[x][table[y][z]])
    return result


# VERIFY GROUP STRUCTURE AND RETURN BOOLEAN

def is_associative():
    for x,y,z in itertools.product(carrier, repeat=3):
        if table[x][table[y][z]]!=table[table[x][y]][z]:
            return False
    return True

def has_unit():
    for x in carrier:
        if not(table[x][unit] == x) or not(table[unit][x]==x):
            return False
    return True
            
def is_commutative():
    for x in carrier:
        for y in carrier:
            if not table[x][y] == table[y][x]:
                return False
    return True
            
def has_inverses():
    for x in carrier:
        exists_unit = False
        for y in carrier:
            if table[x][y]==unit and table[y][x]==unit:
                exists_unit = True
        if not exists_unit:
            return False
    return True

# Not needed to check for groups

# requires has_inverses()
def minus(x): 
    for y in carrier:
        if table[x][y]==unit and table[y][x]==unit:
            return y
    print(x,'has no inverse')

# it is not checked whether left-minus is unique
def left_minus(x): 
    for y in carrier:
        if table[y][x]==unit:
            return y
    print(x,'has no left-inverse')

# it is not checked whether right-minus is unique
def right_minus(x): 
    for y in carrier:
        if table[x][y]==unit:
            return y
    print(x,'has no right-inverse')

# requires has_inverses()
def is_half_associative():
    for x,y in itertools.product(carrier, repeat=2):
        if table[left_minus(x)][table[x][y]]!=y or table[table[y][x]][right_minus(x)]!=y:
            return False
    return True


# Verify whether a group
def is_group():
    return has_unit() and has_inverses() and is_associative()

