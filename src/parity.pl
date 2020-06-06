
n=2

def parity(n):
    if n % 2 == 0:
        print(n,'is even')
    elif n % 2 == 1:
        print(n,'is odd')
    else:
        print(n, 'is not an integer')

parity(n)