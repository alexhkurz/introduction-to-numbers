from Group2 import *
from itertools import permutations, combinations

n = 6
carrier = list(range(0,n))
print('carrier: ',carrier)
list_of_permuatations = list(permutations(range(0, n)))
for table in combinations(list_of_permuatations, n):
    init(carrier,0,table)
    if has_unit() and has_inverses() and is_half_associative():
        print('')
        print('FOUND GROUPOKU:')
        print_table(table)
        if is_associative():
            print('is associative')
        if is_commutative():
            print('is commutative')





