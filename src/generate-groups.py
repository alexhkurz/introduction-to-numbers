import Group
from itertools import permutations, combinations

n = 5
carrier = list(range(0,n))
print('carrier: ',carrier)
list_of_permuatations = list(permutations(range(0, n)))
for table in permutations(list_of_permuatations, n):
    def op(x,y):
        return table[x][y]
    Group.__init__(carrier,0,op)
    if Group.has_unit() and Group.is_associative():
        print('found group:')
        Group.print_table(table)




