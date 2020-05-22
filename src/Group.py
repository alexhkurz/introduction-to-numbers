'''
Verify whether op is a group operation on carrier with neutral element
'''

import itertools

def __init__(mycarrier, myunit, myop):
    global carrier
    carrier = mycarrier
    global unit
    unit = myunit
    global op
    op = myop

# UTILITIES 

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

# VERIFICATION OF GROUP STRUCTURE

# Verify whether self is a group

def test_associative():
    result = True
    for x,y,z in itertools.combinations_with_replacement(carrier, 3):
        if op(x,op(y,z))!=op(op(x,y),z):
            result = False
            print('violates associativity: (',x, y,')', z,'=', op(op(x,y),z), ' and ' , x, '(', y, z, ')','=',op(x,op(y,z)))
    return result

def test_unit():
    result = True
    for x in carrier:
        if not(op(x,unit) == x) or not(op(unit,x)==x):
            result = False
            print('unit is not a neutral element')
            

def test_inverse():
    result = True
    for x in carrier:
        exists_unit = False
        for y in carrier:
            if op(x,y)==unit:
                exists_unit = True
        if not exists_unit:
            print(x, 'has no inverse')
            result = False
    return result

# Verify whether a group
def test_group():
    if test_associative():
        print('associative')
    if test_unit():
        print('has neutral element')
    if test_inverse():
        print('has inverses')


