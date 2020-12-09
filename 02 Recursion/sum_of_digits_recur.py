# Section 3-16 
# Question: How do we find the sum of the digits of a positive integer using recursion?


# Step 1: The recursive case
# Add the current digit to a total

# Step 2: The Base Condition
# If there are no more digits, return the total

# Step 3: The unintended cases
# If the input is not a positive integer, throw an exception

# perform sum function recursively
test = 349587
expected = 3 + 4 + 9 + 5 + 8 + 7

def sum_digits(number):
    
    assert number >= 0 and int(number) == number, 'Input must be a nonnegative integer.' # Step 3: the unintended cases

    return 0 if number == 0 else (number % 10) + sum_digits(int(number / 10)) # Step 1 and 2

# Show the output
outcome = sum_digits(test)
print('Expected: ', expected)
print('Outcome: ', outcome)
assert outcome == expected, 'outcome does not match expected value.  Check logic and try again.'
