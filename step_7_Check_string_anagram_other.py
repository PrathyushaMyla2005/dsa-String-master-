'''explain question and the answer
Check if two strings are anagrams of each other
Problem Statement (in simple words):
You are given two strings, s and t.
Your task is to determine if t is an anagram of s. An anagram means that t can be formed by rearranging the letters of s, using all the original letters exactly once.
For example:
Example 1:
s = "anagram"
t = "nagaram"
# Step by step:
# Rearranging "anagram" can give "nagaram" ✅
# Output: True
# Example 2:
s = "rat"
t = "car"
# Step by step:
# Rearranging "rat" cannot give "car" ❌
# Output: False'''
#brute force approach
def is_anagram(s, t):
    # Step 1️⃣: If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False

    # Step 2️⃣: Sort both strings
    sorted_s = sorted(s)
    sorted_t = sorted(t)

    # Step 3️⃣: Compare the sorted versions
    return sorted_s == sorted_t
print(is_anagram("anagram", "nagaram"))  # Output: True
print(is_anagram("rat", "car"))  # Output: False
#tc = O(n log n) n is the length of the string
#sc = O(n)
#optimal approach
def are_anagrams(s1, s2):
    # Step 1️⃣: If lengths are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Step 2️⃣: Create a frequency dictionary for characters in s1
    freq = {}
    for char in s1:
        # If char is already in dictionary, increment its count
        if char in freq:
            freq[char] += 1
        # If char is not in dictionary, initialize count to 1
        else:
            freq[char] = 1

    # Step 3️⃣: Decrease the count based on characters in s2
    for char in s2:
        # If char not in freq dictionary, it's not in s1, return False
        if char not in freq:
            return False
        # Subtract 1 from the count
        freq[char] -= 1
        # If count becomes negative, s2 has extra char, return False
        if freq[char] < 0:
            return False

    # Step 4️⃣: If all counts matched, strings are anagrams
    return True

# ✅ Example usage:
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "bello"))    # False
#tc = O(n) n is the length of the string
#sc = O(1) because the dictionary will hold at most 26 characters (for
# lowercase letters)
#optimal approach using array
def are_anagrams(s1, s2):
    # Step 1️⃣: If lengths are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    # Step 2️⃣: Create a frequency array for characters (assuming lowercase a-z)
    freq = [0] * 26  # 26 letters in the alphabet

    # Step 3️⃣: Count characters in s1
    for char in s1:
        freq[ord(char) - ord('a')] += 1  # Increment count for this character

    # Step 4️⃣: Decrease count based on characters in s2
    for char in s2:
        freq[ord(char) - ord('a')] -= 1  # Decrement count for this character
        if freq[ord(char) - ord('a')] < 0:
            return False  # More occurrences in s2 than in s1

    # Step 5️⃣: If all counts are zero, they are anagrams
    return all(count == 0 for count in freq)
# ✅ Example usage:
print(are_anagrams("listen", "silent"))  # True
