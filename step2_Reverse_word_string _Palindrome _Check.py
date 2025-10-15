''''1️⃣ Reverse Words in a Given String
Problem Statement (Simple Version):
You are given a sentence or string made up of words separated by spaces. Your task is to reverse the order of the words.
Key Points:
Only the order of words changes, not the letters in a word.
Words are separated by spaces.
Example:
Input:  "I love programming"
Output: "programming love I"
Explanation:
Original sentence → "I love programming"
Words are → ["I", "love", "programming"]
Reverse the order → ["programming", "love", "I"]
Join them back with spaces → "programming love I"'''
'''Time Complexity (TC)

Extracting words: Loop through each character → O(n), where n = length of string

Reversing words: Loop through all words → O(m), where m = number of words (~≤ n)
✅ Total TC: O(n)

Space Complexity (SC)

words list stores all words → O(n)

reversed_string stores final output → O(n)
✅ Total SC: O(n)'''
def reverse_words(s):
    words = []  # 1️⃣ List to store all words from the string
    word = ""   # 2️⃣ Temporary variable to build each word character by character

    # 3️⃣ Extract words manually from the string
    for char in s:              # Loop through each character in the input string
        if char != " ":         # If the character is not a space
            word += char        # Add the character to the current word
        else:                   # If the character is a space
            if word != "":      # If we have a word built
                words.append(word)  # Add the word to the words list
                word = ""           # Reset the word to start a new one
    if word != "":                 # After the loop, add the last word (if any)
        words.append(word)

    # 4️⃣ Reverse the words manually
    reversed_string = ""           # String to store the final reversed sentence
    for i in range(len(words)-1, -1, -1):  # Loop from last word to first word
        reversed_string += words[i]        # Add the current word to the reversed string
        if i != 0:                         # Add a space after the word except the last one
            reversed_string += " "

    # 5️⃣ Return the final reversed string
    return reversed_string


# Example usage
input_str = "I love coding"
print(reverse_words(input_str))  # Output: "coding love I"
#optimal approach
'''ime Complexity (TC)

split() → O(n)

reversing list → O(n)

' '.join() → O(n)
✅ Total: O(n)

Space Complexity (SC)

words list → O(n)

reversed_words → O(n)

final string → O(n)
✅ Total: O(n'''
def reverse_words_optimal(s):
    # Step 1: Split the string into words
    words = s.split()  # "I love coding" -> ["I", "love", "coding"]
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]  # ["coding", "love", "I"]
    
    # Step 3: Join the words back into a string
    reversed_string = ' '.join(reversed_words)  # "coding love I"
    
    return reversed_string

# Example
input_str = "I love coding"
print(reverse_words_optimal(input_str))  # Output: "coding love I"
#palindrome
'''Palindrome Check

Problem Statement (Simple Version):
A palindrome is a word, number, or sentence that reads the same forward and backward.
Your task is to check if a given string is a palindrome.

Key Points:

Ignore spaces and punctuation (sometimes, depends on question).

Case-insensitive (i.e., "Madam" is the same as "madam").

Example:

Input: "madam"
Output: True  (because "madam" reversed is also "madam")

Input: "racecar"
Output: True
Time Complexity (TC)

Loop to reverse string → O(n)

String comparison → O(n)
✅ Total TC = O(n)

Space Complexity (SC)

reversed_s stores reversed string → O(n)
✅ Total SC = O(n)'''
def is_palindrome(s):
    # Step 1: Preprocess the string
    s = s.lower()  # Convert to lowercase
    s = s.replace(" ", "")  # Remove spaces (optional, depends on problem)

    # Step 2: Reverse the string manually
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  # Add current char at the beginning

    # Step 3: Compare original and reversed strings
    if s == reversed_s:
        return True
    else:
        return False

# Examples
print(is_palindrome("madam"))     # True
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("A man a plan a canal Panama"))  # True
def is_palindrome_optimal(s):
    # Step 1: Preprocess the string
    s = s.lower()          # Make lowercase for case-insensitive check
    s = s.replace(" ", "") # Remove spaces (optional, can also remove punctuation if needed)

    # Step 2: Initialize two pointers
    left = 0
    right = len(s) - 1

    # Step 3: Compare characters from both ends
    while left < right:
        if s[left] != s[right]:
            return False  # Not a palindrome if mismatch
        left += 1
        right -= 1

    return True  # All characters matched, it is a palindrome

# Examples
print(is_palindrome_optimal("madam"))                    # True
print(is_palindrome_optimal("racecar"))                  # True
print(is_palindrome_optimal("hello"))                    # False
print(is_palindrome_optimal("A man a plan a canal Panama"))  # True
#optimal approach
'''Time Complexity (TC)
Loop with two pointers → O(n)
✅ Total TC = O(n)
Space Complexity (SC)
Only a few extra variables → O(1)
✅ Total SC = O(1)'''
