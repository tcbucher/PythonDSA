import sys
sys.setrecursionlimit(10000)

def factorial(n):
    assert n >= 0 and int(n) == n, 'Input must be a nonnegative integer' # Step 3: Check the input

    if n in (0,1): # Step 2: The constraint
        return 1
    else: 
        return n * factorial(n - 1) # Step 1: The function calls itself

print(factorial(4))