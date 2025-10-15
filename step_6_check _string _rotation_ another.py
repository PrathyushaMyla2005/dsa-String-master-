'''explain the question and the answer
Check if String Rotation is another string
Problem Statement (in simple words):
You are given two strings, s1 and s2.
Your task is to determine if s2 is a rotation of s1.    
For example:
Example 1:'''
s1 = "waterbottle"
s2 = "erbottlewat"
# Step by step:
# "waterbottle" rotated can become "erbottlewat" ✅
# Output: True'''
#brute force approach
def is_rotation(s1, s2):
    # Step 1️⃣: Check if lengths are different, if yes return False
    if len(s1) != len(s2):
        return False

    # Step 2️⃣: Generate all rotations of s1 and check if any matches s2
    for i in range(len(s1)):
        # Create a rotation by slicing s1 at index i
        rotation = s1[i:] + s1[:i]
        # Step 3️⃣: Compare the rotation with s2
        if rotation == s2:
            return True  # Found a match, s2 is a rotation of s1

    # Step 4️⃣: If no rotations matched, return False
    return False
print(is_rotation(s1, s2))  # Output: True
#tc = O(n^2) n is the length of the string
#sc = O(n)
#optimal approach
def is_rotation(s1, s2):
    # Step 1️⃣: Check if lengths are different, if yes return False
    if len(s1) != len(s2):
        return False

    # Step 2️⃣: Concatenate s1 with itself
    doubled = s1 + s1

    # Step 3️⃣: Check if s2 is a substring of the concatenated string
    return s2 in doubled
print(is_rotation(s1, s2))  # Output: True
#tc = O(n) n is the length of the string
#sc = O(n)

