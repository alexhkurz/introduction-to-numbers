'''
Verify whether op is a group operation on carrier
'''

import itertools

def __init__(mycarrier, myzero, myone, myplus, mymult):
    global carrier
    carrier = mycarrier
    global zero
    zero = myzero
    global one
    one = myone
    global plus
    plus = myplus
    global mult
    mult = mymult
    global small_carrier
    small_carrier = [x for x in carrier if not(x==zero)]
    global smaller_carrier
    smaller_carrier = [x for x in small_carrier if not(x==one)]

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

# VERIFY RING/FIELD STRUCTURE

def plus_is_associative():
    for x,y,z in itertools.product(small_carrier, repeat=3):
        if plus(x,plus(y,z))!=plus(plus(x,y),z):
            return False
    return True

def mult_is_associative():
    for x,y,z in itertools.product(smaller_carrier, repeat=3):
        if mult(x,mult(y,z))!=mult(mult(x,y),z):
            return False
    return True

def has_zero():
    for x in carrier:
        if not plus(x,zero) == x or not plus(zero,x)==x:
            return False
    return True

def mult_zero_is_zero():
    for x in carrier:
        if not mult(x,zero) == zero or not mult(zero,x) == zero:
            return False
    return True
            
def has_one():
    for x in small_carrier:
        if not mult(x,one) == x  or not mult(one,x)==x:
            return False
    return True
            
def plus_is_commutative():
    for x in small_carrier:
        for y in small_carrier:
            if not(plus(x,y) == plus(y,x)):
                return False
    return True
            
def mult_is_commutative():
    for x in smaller_carrier:
        for y in smaller_carrier:
            if not(mult(x,y) == mult(y,x)):
                return False
    return True
            
def is_distributive():
    #print('is dist')
    for x  in smaller_carrier:
        for y,z in itertools.combinations_with_replacement(small_carrier, 2):
            if mult(x,plus(y,z))!=plus(mult(x,y),mult(x,z)):
                return False
    return True
            
def has_minus():
    for x in small_carrier:
        exists_unit = False
        for y in small_carrier:
            if plus(x,y)==zero:
                exists_unit = True
        if not exists_unit:
            return False
    return True

def has_division():
    for x in smaller_carrier:
        exists_unit = False
        for y in smaller_carrier:
            if mult(x,y)==one:
                exists_unit = True
        if not exists_unit:
            return False
    return True

# Verify whether a ring, commutative ring, field

def is_ring():
    return has_zero() and has_one() and has_minus() and is_distributive() and plus_is_associative() and mult_is_associative() and plus_is_commutative() 

def is_commutative_ring():
    return is_ring() and mult_is_commutative()

def is_field():
    return is_commutative_ring() and has_division()

