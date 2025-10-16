'''explain the question in detail
Given a string s that consists of digits 0-9 and parentheses '(' and ')'.
We define the nesting depth of the string s as the maximum depth of nested parentheses in s.
For example, the nesting depth of s = "(1+(2*3)+((8)/4))+1" is 3 because the deepest nested parentheses is "((8)/4)" which is 3 levels deep.
Similarly, the nesting depth of s = "1+(2*3)/(2-1)" is 1 because the parentheses are only 1 level deep.
Also, the nesting depth of s = "1" is 0 because there are no parentheses in the string.
Given a string s, return the nesting depth of s.
#example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3 how came to this answer?
First ( → depth 1

((2)) → max depth 2

(((3))) → max depth 3 → maximum depth = 3
'''
#brute force approach
def maxDepthBruteForce(s):
    max_depth = 0  # To store the maximum nesting depth found

    # Loop through each character in the string
    for i in range(len(s)):
        if s[i] == '(':  # Only check when we find an opening parenthesis
            current_depth = 0  # Start counting depth from this '('
            
            # Scan forward from this position to count nested '('
            for j in range(i, len(s)):
                if s[j] == '(':  
                    current_depth += 1  # Increase depth for each '('
                elif s[j] == ')':
                    current_depth -= 1  # Decrease depth for each ')'
                
                # Update max_depth if current_depth is higher
                max_depth = max(max_depth, current_depth)
                
                # If current_depth drops to 0, we are done with this '('
                if current_depth == 0:
                    break

    return max_depth  # Return the maximum nesting depth found
#example
s = "(1+(2*3)+((8)/4))+1"
print(maxDepthBruteForce(s))  # Output: 3
#tc O(n^2)because of nested loops for each '(' we are scanning the rest of the string 
# sc O(1) because  we are using only constant space
#optimal approach
def maxDepthOptimal(s):
    current_depth = 0  # To track the current depth of nested parentheses
    max_depth = 0  # To store the maximum depth found

    # Loop through each character in the string
    for char in s:
        if char == '(':  # When we find an opening parenthesis
            current_depth += 1  # Increase the current depth
            max_depth = max(max_depth, current_depth)  # Update max_depth if needed
        elif char == ')':  # When we find a closing parenthesis
            current_depth -= 1  # Decrease the current depth

    return max_depth  # Return the maximum nesting depth found
#example
s = "(1+(2*3)+((8)/4))+1"
print(maxDepthOptimal(s))  # Output: 3
#tc O(n) we are scanning the string only once
#sc O(1) we are using only constant space
