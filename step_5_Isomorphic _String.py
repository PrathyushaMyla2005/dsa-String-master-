'''What is an Isomorphic String?

Two strings s and t are isomorphic if you can replace letters in s to get t without changing the order, and no two letters in s map to the same letter in t.

Think of it like a “one-to-one mapping”

Each letter in s has a partner letter in t.

The same letter in s must always map to the same letter in t.

No two letters in s can map to the same letter in t.

Example 1:
s = "egg"
t = "add"


Step by step:

'e' → 'a'

'g' → 'd'

'g' again → still 'd' ✅

All letters match the rules ✅

Output: True

Example 2:
s = "foo"
t = "bar"


Step by step:

'f' → 'b' ✅

'o' → 'a' ✅

'o' again → should map to 'a' but in t it is 'r' ❌

Output: False'''
def isIsomorphic(s,t):
    # Step 1️⃣: If the lengths of the strings are different, they can't be isomorphic
    if len(s) != len(t):
        return False

    # Step 2️⃣: Create a dictionary to store mapping from characters in s to characters in t
    mapping = {}

    # Step 3️⃣: Create a set to store characters in t that are already mapped
    mapped_chars = set()

    # Step 4️⃣: Loop through all characters of s and t
    for i in range(len(s)):
        char_s = s[i]  # current character in s
        char_t = t[i]  # current character in t

        # Step 5️⃣: If char_s is already mapped
        if char_s in mapping:
            # Check if it maps to the same character in t
            if mapping[char_s] != char_t:
                return False  # conflict found, not isomorphic
        else:
            # Step 6️⃣: If char_t is already mapped to some other char_s, it's a conflict
            if char_t in mapped_chars:
                return False  # two chars from s mapping to same char in t
            # Step 7️⃣: Add the new mapping
            mapping[char_s] = char_t
            mapped_chars.add(char_t)

    # Step 8️⃣: All characters checked, no conflicts → strings are isomorphic
    return True
s1 = "egg"
t1 = "add"
print(isIsomorphic(s1, t1))  # Output: True

s2 = "foo"
t2 = "bar"
print(isIsomorphic(s2, t2))  # Output: False

s3 = "paper"
t3 = "title"
print(isIsomorphic(s3, t3))  # Output: True
#tc = O(n) n is the length of the string
#sc = O(1) because the dictionary and set will hold at most 26 characters (for lowercase letters)
#optimal approach
def isIsomorphic(s, t):
    # Step 1️⃣: If the lengths of the strings are different, they can't be isomorphic
    if len(s) != len(t):
        return False

    # Step 2️⃣: Create two dictionaries to store mappings in both directions
    map_s_to_t = {}
    map_t_to_s = {}

    # Step 3️⃣: Loop through all characters of s and t
    for i in range(len(s)):
        char_s = s[i]  # current character in s
        char_t = t[i]  # current character in t

        # Step 4️⃣: Check mapping from s to t
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False  # conflict found, not isomorphic
        else:
            map_s_to_t[char_s] = char_t

        # Step 5️⃣: Check mapping from t to s
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False  # conflict found, not isomorphic
        else:
            map_t_to_s[char_t] = char_s

    # Step 6️⃣: All characters checked, no conflicts → strings are isomorphic
    return True
s1 = "egg"
t1 = "add"
print(isIsomorphic(s1, t1))  # Output: True