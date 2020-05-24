# run as `python generate-rings.py`
# runs fast for n=4, needs a long time for n=5, didnt try for n=6

import Group
import Ring
from itertools import permutations, combinations

n=5
carrier = list(range(0,n))
print('carrier: ',carrier)
list_of_permutations = list(permutations(range(0, n)))
# all possible rows of the multiplication table (without the zero and one columns)
list_of_permutations1 = list(permutations(range(0, n),n-2))
# choose n-1 distinct rows (it doesnt harm to order them with combinations instead of permutations)
for table_plus in combinations(list_of_permutations, n):
    def plus(x,y):
        return table_plus[x][y]
    Ring.__init__(carrier,0,1,plus,plus) # the 2nd plus is redundant for now
    # any structure generated so far satisfies Ring.has_minus() because we use permutations
    if Ring.has_zero() and Ring.plus_is_associative():
        # Ring.print_table([[plus(x,y) for y in carrier] for x in carrier])
        # choose n-2 distinct rows (the first two rows are determined by the properties of zero and one)
        for table_mult in permutations(list_of_permutations1, n-2):
            def mult(x,y):
                if x==0:
                    return 0
                elif y==0:
                    return 0
                elif x==1:
                    return y
                elif y==1:
                    return x
                else: 
                    return table_mult[x-2][y-2]        
            Ring.__init__(carrier,0,1,plus,mult)
            # any structure generated above satisfies Ring.has_one() and Ring.mult_zero_is_zero()
            if Ring.is_distributive() and Ring.mult_is_associative():
                print('')
                print('FOUND RING')
                print('  plus:')
                Ring.print_table([[plus(x,y) for y in carrier] for x in carrier])
                print('  mult :')
                Ring.print_table([[mult(x,y) for y in carrier] for x in carrier])
                if Ring.mult_is_commutative():
                    print('is commutative')
                    if Ring.has_division():
                        print('is field')
            
            




