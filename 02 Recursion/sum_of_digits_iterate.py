# Section 3-16 
# Question: How do we find the sum of the digits of a positive integer using recursion?

# perform sum function iteratively

input_value = 349587
expected = 3 + 4 + 9 + 5 + 8 + 7
outcome = 0

while input_value >= 10: # Base condition
    outcome += input_value % 10 
    input_value = int(input_value / 10) # recursive case

outcome += input_value

# Show the output
print('Expected: ', expected)
print('Outcome: ', outcome)
assert outcome == expected, 'outcome does not match expected value.  Check logic and try again.'