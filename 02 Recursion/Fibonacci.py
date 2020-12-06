def fibonacci(n):
    assert n == int(n) and n >= 0, 'n must be a nonnegative integer' # Step 3: Unintentional cases

    if n in (0, 1): # Step 2: The base condition
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2) # Step 1: The recursive case

for x in range(10):
    print(fibonacci(x)) # 13
# f(6) = f(5) + f(4)
# = f(4) + f(3) + f(3) + f(2)
# = f(3) + f(2) + f(2) + f(1) + f(2) + f(1) + 2 
# = f(2) + f(1) + 2 + 2 + 1 + 2 + 1 + 2
# = 2 + 1 + 2 + 2 + 1 + 2 + 1 + 2
# = 13

# The Fibonacci sequence is 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...