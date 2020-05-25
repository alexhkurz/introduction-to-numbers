"""
Fill in the table below
Run this program with `python groupoku.py`
"""

import Group

carrier = [0,1,2,3,4]

table = [
    [0,3,1,2,4],
    [3,2,4,1,0],
    [1,4,3,0,2],
    [2,1,0,4,3],
    [4,0,2,3,1]
]

def op(x,y):
    return table[x][y]

Group.__init__(carrier,0,op)
Group.print_table(table)
Group.test_group()
