def lengthOfLongestSubstring(s: str) -> int: # sliding window approach
    # Initialize a dictionary to store the last index of each character seen so far
    char_map = {}
    # Initialize the start of the window
    start = 0
    # Initialize the maximum length of the substring without repeating characters
    max_length = 0

    # Iterate over the characters in the string
    for end in range(len(s)):
        # If the current character is already in the window and its index is greater than or equal to the start of the window,
        # move the start of the window to the next index of the repeated character
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1
        # Update the last index of the current character
        char_map[s[end]] = end
        # Update the maximum length of the substring without repeating characters
        max_length = max(max_length, end - start + 1)

    # Return the maximum length of the substring without repeating characters
    return max_length

# Test cases
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 (The answer is "abc")
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1 (The answer is "b")
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3 (The answer is "wke")

"""A sliding window is a technique used for finding subarrays or substrings within a sequence that satisfy certain criteria. 
It involves maintaining a window (a range of indices) in the sequence and moving the window across the sequence to find 
the desired subarray or substring"""