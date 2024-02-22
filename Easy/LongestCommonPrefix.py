def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    # Find the minimum length string in the array
    min_len = min(len(s) for s in strs)
    
    # Compare characters at the same index for all strings
    for i in range(min_len):
        char = strs[0][i]  # Get the character at index i of the first string
        # Check if all other strings have the same character at index i
        if not all(s[i] == char for s in strs):
            # If not, return the longest common prefix up to index i
            return strs[0][:i]
    
    # If all characters match, return the longest common prefix as the shortest string
    return strs[0][:min_len]

strings = ["flower", "flow", "flight"]
print(longest_common_prefix(strings))  # result "fl"
