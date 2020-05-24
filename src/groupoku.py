"""
Fill in the table below
Run this program with `python groupoku.py`
"""

import Group

carrier = [0,1,2,3]

table = [
    [0,1,2,3],
    [1,2,3,0],
    [2,3,0,1],
    [3,0,1,2]
]

def op(x,y):
    return table[x][y]

Group.__init__(carrier,0,op)
Group.print_table(table)
Group.test_group()
