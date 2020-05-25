'''
Verify whether op is a group operation on carrier
'''

import itertools

def __init__(mycarrier, myunit, myop):
    global carrier
    carrier = mycarrier
    global unit
    unit = myunit
    global op
    op = myop

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

# VERIFY GROUP STRUCTURE AND PRINT RESULTS

def test_associative():
    result = True
    for x,y,z in itertools.product(carrier, repeat=3):
        if op(x,op(y,z))!=op(op(x,y),z):
            result = False
            print('violates associativity: (',x, y,')', z,'=', op(op(x,y),z), ' and ' , x, '(', y, z, ')','=',op(x,op(y,z)))
        # else:
            # print('associative: (',x, y,')', z,'=', op(op(x,y),z), ' and ' , x, '(', y, z, ')','=',op(x,op(y,z)))
    return result

def test_unit():
    result = True
    for x in carrier:
        if not(op(x,unit) == x) or not(op(unit,x)==x):
            result = False
            print('unit is not a neutral element for', x)
    return result
            

def test_inverse():
    result = True
    for x in carrier:
        exists_unit = False
        for y in carrier:
            if op(x,y)==unit and op(y,x)==unit:
                exists_unit = True
        if not exists_unit:
            print(x, 'has no inverse')
            result = False
    return result

# Verify whether a group and print result
def test_group():
    if test_associative():
        print('is associative')
    if test_unit():
        print('has neutral element')
    if test_inverse():
        print('has inverses')

# VERIFY GROUP STRUCTURE AND RETURN BOOLEAN

def is_associative():
    for x,y,z in itertools.product(carrier, repeat=3):
        if op(x,op(y,z))!=op(op(x,y),z):
            return False
    return True

def has_unit():
    for x in carrier:
        if not(op(x,unit) == x) or not(op(unit,x)==x):
            return False
    return True
            
def is_commutative():
    for x in carrier:
        for y in carrier:
            if not(op(x,y) == op(y,x)):
                return False
    return True
            
def has_inverses():
    for x in carrier:
        exists_unit = False
        for y in carrier:
            if op(x,y)==unit and op(y,x)==unit:
                exists_unit = True
        if not exists_unit:
            return False
    return True

# Not needed to check for groups

# requires has_inverses()
def minus(x): 
    for y in carrier:
        if op(x,y)==unit and op(y,x)==unit:
            return y

# requires has_inverses()
def is_half_associative():
    for x,y in itertools.product(carrier, repeat=2):
        if op(minus(x),op(x,y))!=y or op(op(y,x),minus(x))!=y:
            return False
    return True


# Verify whether a group
def is_group():
    return has_unit() and has_inverses() and is_associative()

