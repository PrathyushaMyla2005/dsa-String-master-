'''Problem: Reverse Every Word in a String

Goal: Given a string s containing words separated by spaces, reverse each word individually, but keep the words in the same order.

Examples:

Input: "Hello World"
Output: "olleH dlroW"

Input: "I love coding"
Output: "I evol gnidoc'''
#brute force approach
def reverseWordsBruteForce(s):
    words = s.split(' ')  # Split the string into words based on spaces
    reversed_words = []   # List to store the reversed words

    for word in words:
        reversed_word = word[::-1]  # Reverse each word using slicing
        reversed_words.append(reversed_word)  # Add the reversed word to the list

    result = ' '.join(reversed_words)  # Join the reversed words back into a single string with spaces
    return result  # Return the final string with reversed words
# Example usage:
s = "Hello World"
print(reverseWordsBruteForce(s))  # Output: "olleH dlroW"
# Time Complexity: O(n) where n is the length of the string. We traverse the string to split it into words and then reverse each word.
# Space Complexity: O(n) for storing the list of reversed words.
# Optimal approach
def reverseWordsOptimal(s):
    def reverse_range(lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    # Convert the string to a list of characters for in-place modification
    char_list = list(s)
    n = len(char_list)

    # Step 1: Reverse the entire string
    reverse_range(char_list, 0, n - 1)

    # Step 2: Reverse each word in the reversed string
    start = 0
    for i in range(n + 1):
        if i == n or char_list[i] == ' ':
            reverse_range(char_list, start, i - 1)
            start = i + 1

    # Convert the list of characters back to a string
    result = ''.join(char_list)
    return result