# NOTE: a pangram is a sentence that contains every letter on the alphabet at least once
# NOTE: the sentence consists of alphabets only if not we weoulduse isplah to check for numbers etc then add that to the set with letters.add(char)
def is_pangram(sentence:str) -> bool:
    letters = set(sentence) # sets in python do not contain repeting elements hence this will only store each letter once
    return len(letters) == 26 # if each letter is in the set once then it having a len of 26 Iie 26 letters means it has all the letters in the alphabet
        
print(is_pangram("thequickbrownfoxjumpsoverthelazydog"))