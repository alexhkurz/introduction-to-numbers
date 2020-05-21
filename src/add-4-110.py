"""
Use this template to test addition  (called op for operation below) of 4 numbers {0, ...,3} with 1+1=0
Make sure that 0 is the neutral element and that the operation is commutative
Run this template template with `python add-4-110.py`
"""

import Group
from Group import *

carrier = [0,1,2,3]

def op(x,y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif x==y:
        return 1
    elif x==1 and y==2:
        return 3
    elif x==1 and y==3:
        return 2
    elif x==2 and y==3:
        return 3
    else:
        return op(y,x) # op(x,y) = op(y,x)

Group.__init__(carrier,op)
Group.print_table([[op(x,y) for x in carrier] for y in carrier])
Group.test_group()
