import Group
from itertools import permutations, combinations

n=4
carrier = list(range(0,n))
list_of_permuatations = list(permutations(range(0, n)))
for table in combinations(list_of_permuatations, n):
    def op(x,y):
        return table[x][y]
    Group.__init__(carrier,0,op)
    if Group.is_group():
        print('found group:')
        Group.print_table(table)




