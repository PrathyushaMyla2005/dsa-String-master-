'''Problem Statement (in simple words):

You are given an array of strings (a list of words).
Your task is to find the longest prefix (starting part of the word) that is common to all the words in the list.

If there is no common prefix, return an empty string ("").

🧩 Let’s understand what “prefix” means:

A prefix means the beginning part of a word.

Example:

Prefixes of "flower" are:

"f", "fl", "flo", "flow", "flowe", "flower"

💡 Example 1:
Input:
["flower", "flow", "flight"]'''
#brute force approach
def longest_common_prefix(strs):
    if not strs:
        return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for string in strs:
            if i >= len(string) or string[i] != char:
                return strs[0][:i]
    return strs[0]
# Example usage:
words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))  # Output: "fl"
#tc = O(m*n) m is the length of the shortest string and n is the number of strings
#sc = O(1)
#optimal approach
def longest_common_prefix(strs):
    if not strs:
        return ""

    # Step 1️⃣: Find the shortest string in the list
    shortest = min(strs, key=len)

    # Step 2️⃣: Loop through each character index of the shortest string
    for i in range(len(shortest)):
        # Step 3️⃣: Check this character against all other strings
        for string in strs:
            # If a mismatch is found, return the prefix up to this point
            if string[i] != shortest[i]:
                return shortest[:i]

    # Step 4️⃣: If no mismatches, the entire shortest string is the common prefix
    return shortest
# Example usage:
words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))  # Output: "fl"
#tc = O(m*n) m is the length of the shortest string and n is the number of strings
#sc = O(1)