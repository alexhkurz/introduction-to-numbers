"""
Fill in the table below
Run this program with `python check_group.py`
"""

carrier = [0,1,2,3]

table = [
    [0,1,2,3],
    [1,2,3,2],
    [2,3,0,1],
    [3,0,1,2]
]

# print a 2d table in matrix form without commas, brackets and quotes
def print_table(t):
    for row in t:
        print(" ".join(map(str,row)))

def is_associative():
    for x in carrier:
        for y in carrier:
            for z in carrier:
                if not table[x][table[y][z]] == table[table[x][y]][z]:
                    print('not associative: for x =',x,', y =',y,', z =',z,'we have x(yz) =', table[x][table[y][z]], 'and (xy)z =', table[table[x][y]][z])
                    return False
    return True

print('')
print_table(table)
if is_associative():
    print('is associative')
print('')
