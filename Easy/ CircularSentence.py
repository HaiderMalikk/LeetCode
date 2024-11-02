# plz note this sol might be a bit extra and bloated but it works and is rather simple
def isCircularSentence(sentence):
    words = sentence.split() # split at each space so this will tuen sentence into an array of words 
    index = 0 # since we caannot use 'i' with integers we impliment a index so theres no type problems 
    # next few vars are self explanatory 
    first_char_of_first_word_eq_last_char_of_last_word = False
    last_char_of_word_eq_first_char_of_next_word = False
    last_word_of_letter = ""
    first_letter_of_first_word = ""
    chararray = [] # holds all characters in a word get reset every time we finish a word
    for i in words: # this loop goes through each word
        for char in i: #  this loop goes through each character in the word
            if index == 0 and first_letter_of_first_word == "": # if this is our fiest iteration and the first letter of the first word is not set then we are on the first letter of first word we need this later to compare with last letter of last word
                first_letter_of_first_word = char # store  the first letter of the first word
            chararray += char # this stores each char in the word in an array
            
        if chararray[0] == last_word_of_letter and last_word_of_letter != "": # is the first letter of the arr ( the first letter of our word) is the same as the last letter of the last word and the last word is not empty (important as for the first word we dont have a last word to compare with)
            last_char_of_word_eq_first_char_of_next_word = True  # set this var to true 
        elif chararray[0] != last_word_of_letter and last_word_of_letter != "": # is at any word the first letter is not the same as the last letter of the last word and the last word is not empty (meaning this is not the first word)
            return False # return false as this cannot be a circular sentence
        last_word_of_letter = chararray[-1] # at each word we set the last letter of the last word to the last letter of the current word which is the last index of the chararray
        chararray = [] # we empty the chararray so we can start fresh for the next word this way we can set our last word of letter of the array (if we did not empty then theres no way to get the las tletter of any word as it would be one long array of chars, where dose one word and or start ?)
        
        index += 1  # we increment the index so we can keep track of how many words we have gone through
        
    if last_word_of_letter == first_letter_of_first_word: # here we check if the first of first word (we found in the first iteration of both loops) is the same as the last of last word, (before we emptied the array we stores this new las t letter of last word so after the loop ends this var holds the last letter of the last word chararr[-1])
        first_char_of_first_word_eq_last_char_of_last_word = True  # set this var to true
        
    if index == 1: # THIS IS IMPORTANT, if the loop ends and index is one that means we only has one word in that case there was no last word for this single word to compare with so we cannot return false hence we must set this to true as there is no last_char_of_word_eq_first_char_of_next_word as there is only one word
        last_char_of_word_eq_first_char_of_next_word = True   # set this var to true
        
    return last_char_of_word_eq_first_char_of_next_word and first_char_of_first_word_eq_last_char_of_last_word  # return true if both vars are true meaning the sentence is circular

print(isCircularSentence("leetcode exercises sound delightful"  )) # true
print(isCircularSentence("eetcode")) # true
print(isCircularSentence("Leetcode is cool")) # false
print(isCircularSentence("ab a a")) # false