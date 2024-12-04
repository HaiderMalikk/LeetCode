def canMakeSubsequence(str1: str, str2: str) -> bool:
    str1_idx = 0  # Pointer to track position in str1

    for letter in str2:
        isfound = False

        while str1_idx < len(str1):  # Iterate over the remaining characters in str1
            char = str1[str1_idx]
            str1_idx += 1  # Move to the next character in str1

            if char == letter:  # Direct match
                isfound = True
                break
            else:
                # Check if we can increment char to match letter
                increments = (ord(letter) - ord(char)) % 26  # Cyclic increment distance
                if increments <= 1:  # Can only use at most one cyclic increment
                    isfound = True
                    break

        if not isfound:
            return False  # If any character in str2 cannot be matched, return False

    return True  # If all characters in str2 are matched, return True


# Test cases
print(canMakeSubsequence("abc", "ad"))  # T
print(canMakeSubsequence("zc", "ad"))  # T
print(canMakeSubsequence("ab", "d"))   # F
print(canMakeSubsequence("eao", "ofa"))  # F
