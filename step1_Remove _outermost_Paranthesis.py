'''Problem Explanation

Given:

A valid parentheses string s.

A valid parentheses string is one where every opening ( has a corresponding closing ).

Examples of valid strings: "()", "(())", "(()())"

Remove the outermost parentheses of every primitive part of the string.
Step 2: What are outermost parentheses?

Outermost parentheses are the first ( and last ) that enclose a primitive string.
Example:
Input: "(()())(())"
Primitive decomposition: "(()())" + "(())"
Remove outermost: "()()" + "()"
Output: "()()()"
'''
#brute force approach 
'''1️⃣ Time Complexity (TC)

We traverse each character of the string exactly once.

stack.append() and stack.pop() are O(1) operations.

result.append() is O(1) per operation.

''.join(result) at the end takes O(n), where n is the length of s.

✅ Total TC:
O(n)
Linear in the length of the string.
2️⃣ Space Complexity (SC)
stack stores parentheses for nested depth.
Maximum depth = maximum number of nested parentheses in s.
In worst case, stack can hold n/2 elements (e.g., "(((())))") → O(n).
result stores the output string → O(n) in worst case.
✅ Total SC:
O(n)'''
def remove_outer(s):
    stack = []      # Stack to keep track of parentheses
    result = []     # To store characters after removing outermost parentheses

    for char in s:
        if char == '(':          # If it's an opening bracket
            if stack:            # Stack not empty → not outermost
                result.append(char)
            stack.append(char)   # Push to stack

        elif char == ')':        # If it's a closing bracket
            stack.pop()          # Pop matching '(' from stack
            if stack:            # Stack not empty → not outermost
                result.append(char)

    return ''.join(result)      # Convert list to string

# Example Usage
input_str = "(()())(())"
output_str = remove_outer(input_str)
print("Input:", input_str)
print("Output:", output_str)
#optimal approach
'''why we using count variable what is depth of parenthesis
Depth of parentheses refers to the level of nesting of parentheses in a string.
depth = 0 means no open parentheses.
depth = 1 means one open parenthesis without a matching close.
depth = 2 means two open parentheses nested within each other, and so on.

Instead of using a stack to track the depth of parentheses, we can use a simple counter variable
1️⃣ Time Complexity (TC)
We traverse each character of the string exactly once.
✅ Total TC:
O(n)
Linear in the length of the string.
2️⃣ Space Complexity (SC)
We use a counter variable (count) which takes O(1) space.
We use a list (result) to store the output string → O(n) in worst case.
✅ Total SC:
O(n)

'''
def remove_outer_optimal(s):
    count = 0       # To track the depth of parentheses
    result = []     # To store characters after removing outermost parentheses

    for char in s:
        if char == '(':          # If it's an opening bracket
            if count > 0:        # Not outermost if count > 0
                result.append(char)
            count += 1           # Increase depth

        elif char == ')':        # If it's a closing bracket
            count -= 1           # Decrease depth
            if count > 0:        # Not outermost if count > 0
                result.append(char)

    return ''.join(result)      # Convert list to string
# Example Usage
input_str = "(()())(())"
output_str = remove_outer_optimal(input_str)
print("Input:", input_str)
print("Output:", output_str)