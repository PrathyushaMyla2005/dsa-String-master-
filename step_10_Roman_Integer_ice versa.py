'''explain the question
Roman Numerals to Integer
Problem Statement:

You are given a Roman numeral as a string, and you need to convert it into its equivalent integer (number).
xample: "XIV"

Step by step:

Look at the first character: X = 10 → total = 10

Next: I = 1

Next: V = 5

Since I (1) comes before V (5), we subtract 1 from 5 → 4

Add the previous total: 10 + 4 = 14

✅ Output: 14

2️⃣ Integer → Roman Numeral

Example: 14

Step by step:

Start with the largest Roman numeral ≤ 14:

10 → X, remaining = 14 - 10 = 4

Next, 4 → IV, remaining = 4 - 4 = 0

✅ Output: "XIV"

So basically:

"XIV" → 14

14 → "XIV"

It works both ways!
'''
#brute force approach
def romanToInt(s):
    # Step 1️⃣: Create a dictionary with Roman numeral values
    roman_dict = {
        'I':1, 'V':5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000
    }

    total = 0      # To store the final integer value
    i = 0          # Index to traverse the string

    # Step 2️⃣: Loop through each character
    while i < len(s):
        # Example: s = "XIV"

        # Step 2a: Check if next symbol exists and is larger
        if i+1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
            # Subtract current from next and add to total
            # Example: i=1, s[i]='I', s[i+1]='V', 1<5 → total += 5-1 = 4
            total += roman_dict[s[i+1]] - roman_dict[s[i]]
            i += 2   # Skip the next symbol as we already counted it
        else:
            # Add value of current symbol
            # Example: i=0, s[i]='X', next is 'I' → 10 added
            total += roman_dict[s[i]]
            i += 1   # Move to next symbol

    return total  # Return the final integer value

# Test Example
print(romanToInt("XIV"))  # Output: 14
#tc O(n) we are scanning the string only once
#sc O(1) we are using only constant space
#optimal approach
def romanToIntOptimal(s):
    # Step 1️⃣: Create a dictionary with Roman numeral values
    roman_dict = {
        'I':1, 'V':5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000
    }

    total = 0      # To store the final integer value
    prev_value = 0 # To track the value of the previous symbol

    # Step 2️⃣: Loop through each character
    for char in s:
        current_value = roman_dict[char] 
        # Example: s = "XIV"
        # Step 2a: Check if current symbol is larger than previous
        if current_value > prev_value:
            # Subtract twice the previous value (as it was added before)
            total += current_value - 2 * prev_value
        else:
            # Add value of current symbol
            total += current_value
        prev_value = current_value  # Update previous value
    return total  # Return the final integer value
# Test Example
print(romanToIntOptimal("XIV"))  # Output: 14
#tc O(n) we are scanning the string only once
#sc O(1) we are using only constant space