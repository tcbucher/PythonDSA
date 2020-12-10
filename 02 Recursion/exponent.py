# Script to calculate and return a power of a number

base = 9
exponent = 12
solution = base**exponent

def power(base, exponent):
    
    assert exponent == int(exponent) and exponent >= 0, "Exponent must be a nonnegative integer"

    if exponent == 0:
        return 1
    
    return base * power(base, exponent - 1)


# Print the outcome
print(power(base, exponent))
print(solution)