'''
Verify whether op is a group operation on carrier
'''

import itertools

def __init__(mycarrier, myop):
    global carrier
    carrier = mycarrier
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

def test_inverse():
    result = True
    for x in carrier:
        exists_zero = False
        for y in carrier:
            if op(x,y)== 0:
                exists_zero = True
        if not exists_zero:
            print(x, 'has no inverse')
            result = False
    return result

# Verify whether a group
def test_group():
    if test_associative():
        print('associative')
    if test_inverse():
        print('has inverses')


