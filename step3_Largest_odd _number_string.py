'''🧐 Wait, what does "largest odd number in string" mean?

Let’s take an example:

Example 1:Input: "35427"
We need to find the largest substring (from the start) that forms an odd number.

Let’s check from the end:

Last digit = 7 → (7 is odd) ✅
So "35427" itself is odd.

Hence, Largest Odd Number = "35427"

'''
# Function to find the largest odd number in a string
def largest_odd_number(num):
    # Step 1️⃣: Create an empty string to store the answer
    # We start with an empty answer because we haven't found any odd number yet
    largest = ""

    # Step 2️⃣: Loop through every character in the string using its index
    # range(len(num)) gives all index positions (0, 1, 2, ..., len-1)
    for i in range(len(num)):
        # Step 3️⃣: Take the substring from the start (0) to the current index (i)
        # We use num[:i+1] because slicing excludes the end index, so we add +1 to include it
        substring = num[:i + 1]

        # Step 4️⃣: Check if the last character of this substring is an odd number
        # We take substring[-1] → last character
        # Convert it to int → int(substring[-1])
        # Use % 2 == 1 → means the number is odd
        if int(substring[-1]) % 2 == 1:
            # Step 5️⃣: If it's odd, we store this substring as the current largest
            # We keep updating this whenever we find a new odd number
            largest = substring

    # Step 6️⃣: After checking all substrings, return the last stored odd substring
    # If no odd digit was found, 'largest' will still be an empty string ""
    return largest
num = "123456"
print(largest_odd_number(num))
#tc = O(n)  
#sc = O(1)
#optimal approach
# Function to find the largest odd number in a string
def largest_odd_number(num):
    # Step 1️⃣: Loop from the end of the string to the beginning
    # We use range(start, stop, step) → here step is -1 to go backwards
    for i in range(len(num) - 1, -1, -1): #why we use 3 parameters in range function
        #-1,-1

        # Step 2️⃣: Convert current character to integer
        digit = int(num[i])

        # Step 3️⃣: Check if the digit is odd (1,3,5,7,9)
        if digit % 2 == 1:
            # Step 4️⃣: If odd, return substring from start to this position (inclusive)
            # num[:i+1] takes all characters from index 0 to i
            return num[:i + 1]

    # Step 5️⃣: If loop finishes without finding any odd digit, return empty string
    return ""
num = "123456"
print(largest_odd_number(num))
#tc = O(n)
#sc = O(1)
#optimal approach
# Function to find the largest odd number in a string
