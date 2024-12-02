""" 
check if a word occurs as a prefix of any word in a sentence.

given a sentence and a search word, check if the search word is a prefix of any word in the sentence. if it is return the index of the word (1 indexed) else return -1
a prefix is a string that appears at the beginning of a word.
so if the search word is "ab" and the sentence is "abnormal abduct abducts" then "ab" is a prefix of "abnormal" and "abduct" but not "abducts"
so in this case we return 1 as thats the first word that starts with "ab" i.e the number of words that has a prefix "ab"
"""
# ! sol
def isPrefixOfWord(sentence, searchWord):
    wordcount = 1 # count the first word and keep track of the current word count as thats what we are looking for to return
    for charindex in range(len(sentence)): # loop through the sentence
        if sentence[charindex] == " ": # if we hit a space, we've moved to a new word
           wordcount += 1   # increment the word count

        # (if we are on a first letter of a word or (we are on the first word and first letter)) and the current letter is the first letter of the search word
        if (sentence[charindex-1] == " " or (wordcount == 1 and charindex == 0)) and sentence[charindex] == searchWord[0]:
            match = False # initialize match to false
            for i in range(0, len(searchWord)): # loop through the search word
                if charindex + i == len(sentence): # if we are at the end of the sentence we have run out of characters to match
                    match = False # set match to false we have no more characters and no match was found yet
                    break # break out of the loop
                # if the next letter in the sentence is not the same as the next letter in the search word (no nned to check if letter exists we did that in last if statement)
                if sentence[charindex + i] != searchWord[i]:
                    match = False # set match to false as if the next letter is not the same we can't match
                    break # break out of the loop
                match = True # if we have made it through the loop without breaking i.e we went inside no conditions then we have a match
            
            if match == True: # if we make it out the loop with match never being set to false then we have a match
                return wordcount # return the word count 
            
    # if we have gone through the loop and we have not found a match i.e match was set to false initially or before a break theres no match
    return -1 # return -1 as no match was found
    

print(isPrefixOfWord("i love eating burger", "burg")) # 4
print(isPrefixOfWord("this problem is an easy problem", "pro")) # 2
print(isPrefixOfWord("i am your dad", "daddy")) # -1
print(isPrefixOfWord("leetcode corona", "leetco")) # 1
print(isPrefixOfWord("hellohello hellohellohello", "ell")) # -1


