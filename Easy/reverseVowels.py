# reverse vowels (beats, Runtime: 51% 15ms Memory: 26% 17.9ms) solution (rater bloated but works and it simple)
# ! Idea
""" 
1) take the string given and build a array of chars.
2) take this array of chars loop over it and find any vowels using the charmap and store these vowels in a new array and right after replace this vowel in the char array with a place holder here "0". i used a index as i is a str and cannot be used as a index for a array.
3) reverse this vowels array.
4) now loop over the char array again and this time replace the "0" with the vowels from the reversed vowels array. theres 2 indexs to keep track of the two arrays (char arr and vowarr). there should be a 1to1 mapping between the "0"s and the vowels.
5) loop over this new finished char array and add its elemets to a string (return type is str).
6) return the string.
"""

def reverseVowels(s: str) -> str:
    charmap = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}  # charmap for vowels
    chararr = []   # array of chars
    vowarr = []      # array of vowels
    for char in s:    # loop over the string and build the char array
        chararr.append(char)   # add char to the char array
    
    index = 0 # as i is a str and cannot be used as a index for a array so we use an index
    for i in chararr: # loop over the char array
        if i in charmap: #  check if the char is a vowel
            vowarr.append(i) # if it is add it to the vowels array
            chararr[index] = 0  # replace the vowel with a place holder
        index += 1  # increment the index
    vowarr.reverse()  # reverse the vowels array we just made. now we have the vowels in the right order
    
    # two index as the char arr and vow arr are different sizes
    indexchararr = 0   # index for the char array
    indexvowarr = 0    # index for the vowels array
    for i in chararr:   # loop over the char array
        if i == 0:        # if the char is a place holder
            chararr[indexchararr] = vowarr[indexvowarr]  # replace the place holder with the vowel using the corrent index
            indexvowarr += 1  # increment the index of vowarr if we added from it 
        indexchararr += 1   # increment the index of chararr
    
    returnstr = ""  # string to return
    for i in chararr:   # loop over the char array and add its elements to the return string
        returnstr += i #  add the char to the return string
          
    return returnstr   # return the string
        
#  test cases
print(reverseVowels("leetcode"))  # result "leotcede"
print(reverseVowels("IceCreAm"))  # result "AceCreIm"
print(reverseVowels("aA"))  # result Aa