# a anagram in a string is a word or phrase formed by rearranging the letters of a different word or phrase
# so "cinema" and "iceman" are anagrams while car and rat are not the char's must be the same and there occurances too
# we can use sets but they dont track the frequencies of letter note that 'aabb' would be an anagram of 'ab' if we used sets but this is false
# insted we can use a frequncy counter with dictionaries like {'a':2,'b':1} then we can check if they are the same if one is {a: 1, b: 1} and the other is {b: 1, a: 2} then they are NOT anagrams they must have the same characters and have the same frequencies

def isAnagram(s: str, t: str) -> bool:
    # if the two strings are of different length return falseas they cant be anagrams
    if len(s) != len(t):
        return False
    
    # Initialize frequency counters as dictionaries
    freq_s = {}
    freq_t = {}
    
    # Count frequency of each character in s
    for char in s:
        # the get(char, 0) will return 0 if the char is not in the dictionary we can use this to initilize new keys
        # if it is in the dictionary it will return the value of the key ie the count of that letter 
        # by doing + 1 be incriment that letters count by 1
        # initially the get char returns 0 so we will add 1 to that keys value the next time we see get cahr will return 1 the + 1 will make the count 2 so now the letter (key) will have a count(value) of 2 if thast a  => {a:2}
        freq_s[char] = freq_s.get(char, 0) + 1
    
    # Count frequency of each character in t
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    # Compare the two frequency dictionaries if they are the same they are anagrams dont worry about the length we alredy checked that
    return freq_s == freq_t
   
    
    
print(isAnagram("cinema", "iceman")) # True
print(isAnagram("car", "rat")) # False
print(isAnagram("aabb", "ab")) # False (this is why we use frequency) 