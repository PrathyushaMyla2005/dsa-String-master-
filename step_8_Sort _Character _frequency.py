'''What it means:

You are given a word (string).
You must rearrange the letters so that the letters which appear more times come first.

📘 Example 1:

Input: "tree"

Let’s count how many times each letter appears:

Letter	Count
t	1
r	1
e	2

Now, the letter ‘e’ comes 2 times, so it should come first.
After that, we can write ‘t’ and ‘r’ (since both come once).

✅ Output: "eert" or "eetr"
(Both are okay.)'''
#brute force approach
def frequencySort(s):
    # Step 1️⃣: Create an empty dictionary to store character counts
    freq = {}

    # Step 2️⃣: Count how many times each character appears in the string
    for ch in s:
        if ch in freq:
            freq[ch] += 1      # if already present, increase its count
        else:
            freq[ch] = 1       # if not present, set count to 1

    # Step 3️⃣: Sort the characters based on frequency (highest first)
    # 'key=lambda x: freq[x]' means: sort by frequency value of each character
    # 'reverse=True' means: from highest to lowest
    sorted_chars = sorted(freq, key=lambda x: freq[x], reverse=True)

    # Step 4️⃣: Build the final string
     
    # Step 4️⃣: Build the final string
    result = ""
    for ch in sorted_chars:
        result += ch * freq[ch]   # repeat each character by its frequency

    # Step 5️⃣: Return the final sorted string
    return result
# Example usage:
input_str = "tree"
output_str = frequencySort(input_str)
print(output_str)  # Output could be "eert" or "eetr"
#tc O(n log n) why means each line is traversed and sorted
#sc O(n) for dictionary

#optimal approach

