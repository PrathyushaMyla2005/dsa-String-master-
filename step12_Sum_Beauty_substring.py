'''roblem Statement

Given a string s consisting of lowercase English letters,
your task is to find the sum of the beauty values of all possible substrings of s.

💡 Definition

The beauty of a substring is defined as:

Beauty = (frequency of most frequent character) − (frequency of least frequent character)

⚠️ While calculating the least frequent character,
ignore characters that do not appear in the substring (i.e., frequency = 0).

🧠 What is a Substring?

A substring is a continuous sequence of characters within a string.

Example:
If s = "abc", the substrings are:

"a", "b", "c", "ab", "bc", "abc"

🧮 Example

Input:

s = "aabcb"
Output: 5
Explanation:
The substrings of "aabcb" are:
"a", "a", "b", "c", "b", "aa", "ab", "bc", "cb", "aab", "abc", "bcb", "aabcb"
The beauty values of these substrings are:
"a" -> 0
"a" -> 0
"b" -> 0
"c" -> 0
"b" -> 0
"aa" -> 0
"ab" -> 1 (most frequent: 'a' or 'b' = 1, least frequent: 'a' or 'b' = 1)
"bc" -> 1 (most frequent: 'b' or 'c' = 1, least frequent: 'b' or 'c' = 1)
"cb" -> 1 (most frequent: 'c' or 'b' = 1, least frequent: 'c' or 'b' = 1)
"aab" -> 1 (most frequent: 'a' = 2, least frequent: 'b' = 1)
"abc" -> 1 (most frequent: 'a', 'b', or 'c' = 1, least frequent: 'a', 'b', or 'c' = 1)
"bcb" -> 1 (most frequent: 'b' = 2, least frequent: 'c' = 1)
"aabcb" -> 2 (most frequent: 'a' or 'b' = 2, least frequent: 'c' = 1)
'''
#brute force
def beautySum(s):
    # Step 1️⃣: Initialize total beauty sum to 0
    total_beauty = 0

    # Step 2️⃣: Outer loop → choose starting index of substring
    for i in range(len(s)):
        # A dictionary to keep track of frequency of characters in the current substring
        freq = {}

        # Step 3️⃣: Inner loop → choose ending index of substring
        for j in range(i, len(s)):
            # Add current character s[j] to frequency dictionary
            freq[s[j]] = freq.get(s[j], 0) + 1

            # Step 4️⃣: Find max and min frequency in current substring
            max_freq = max(freq.values())  # most frequent character count
            min_freq = min(freq.values())  # least frequent (non-zero) character count

            # Step 5️⃣: Calculate beauty = max - min
            beauty = max_freq - min_freq

            # Step 6️⃣: Add this beauty value to the total sum
            total_beauty += beauty

    # Step 7️⃣: Return the total sum of beauty of all substrings
    return total_beauty
# Example usage
s = "aabcb"
print(beautySum(s))  # Output: 5
# Output: 5
#tc O(n^3) where n is the length of the string
#sc O(1) since the frequency dictionary will at most have 26 entries for each character in the alphabet
#optimized
def beautySumOptimized(s):
    total_beauty = 0

    # Step 2️⃣: Outer loop → choose starting index of substring
    for i in range(len(s)):
        # A list to keep track of frequency of characters in the current substring
        freq = [0] * 26  # Since there are 26 lowercase English letters

        # Step 3️⃣: Inner loop → choose ending index of substring
        for j in range(i, len(s)):
            # Add current character s[j] to frequency list
            freq[ord(s[j]) - ord('a')] += 1

            # Step 4️⃣: Find max and min frequency in current substring
            max_freq = max(freq)  # most frequent character count
            min_freq = min(f for f in freq if f > 0)  # least frequent (non-zero) character count

            # Step 5️⃣: Calculate beauty = max - min
            beauty = max_freq - min_freq

            # Step 6️⃣: Add this beauty value to the total sum
            total_beauty += beauty

    # Step 7️⃣: Return the total sum of beauty of all substrings
    return total_beauty
# Example usage
s = "aabcb"
print(beautySumOptimized(s))  # Output: 5
