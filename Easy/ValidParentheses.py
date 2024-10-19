def is_valid(s: str) -> bool:
    # Dictionary to hold matching brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Initialize an empty stack
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in bracket_map:
            # Pop the topmost element from the stack if it's not empty, otherwise assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped bracket matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # The stack should be empty if all brackets are matched
    return not stack

# Example usage:
print(is_valid("()"))          # Output: True
print(is_valid("()[]{}"))      # Output: True
print(is_valid("(]"))          # Output: False
print(is_valid("([])"))        # Output: True
print(is_valid("([)]"))        # Output: False
