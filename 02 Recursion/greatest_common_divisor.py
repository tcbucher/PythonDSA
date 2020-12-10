# A script to recursively find the greatest common divisor of two numbers

def greatest_divisor(first, second):

    assert first == int(first) and second == int(second) and first != 0 and second != 0, 'Numbers provided must be nonzero integers'

    if first < 0:
        first = -first
    if second < 0:
        second = -second

    if (first >= second):
        return gcd_ordered(first, second)
    elif (first < second):
        return gcd_ordered(second, first)


def gcd_ordered(higher, lower):

    if higher % lower == 0:
        return lower

    return gcd_ordered(lower, higher % lower)

# Test the function
print(greatest_divisor(18,48))
print(greatest_divisor(12,8))
print(greatest_divisor(49,21))
print(greatest_divisor(4,9))
print(greatest_divisor(9,9))