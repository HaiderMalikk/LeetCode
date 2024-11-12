# number of balloons
# given a string text return the maximum number of baloons that can be obtained from its letters only count the word 'balloon' no 's'
# there is only really one way to solve this problem and thats to use the min function 
# the get() methof gets the ocurrences of a letter in a string and returns 0 if the letter is not in the string so we can safely access it in the min function
# the min function returns the minumim occurences of the letters in the string here the letters are 'b', 'a', 'l', 'o', 'n'
# this minmum value is the number of balloons that can be obtained from the letters in the string

""" 
Explained in depth:

the min function uses the idea of the limiting letter meaning it will get the minumum occurences of the letters in the string
here the minimum number of occurences of the letters in the string determines the number of balloons that can be obtained from the letters in the string

if b was 0 than min would return 0 and we would return 0 as no balloons can be obtained from the letters in the string as no 'b' exists in the string
using the same logic if we had multiple letters lets say 5 of 'a', 'l', 'o', 'n' but only 1 b we would get the following
# min(1, 5, 5, 5, 5) = 1 so number of balloons that can be obtained from the letters in the string is 1 as b is the limiting letter beacuse once the b is used once we can no longer obtain any more balloons from the letters in the string
this logic works for all cases
"""

def maxNumberOfBalloons(text):
    map = {} # empty dictionary
    
    for letter in text: # loop through each letter in the string
        if letter == " ": # if the letter is a space
            continue  # skip the letter
        
        if letter not in map: # if the letter is not in the dictionary
            map[letter] = 0 # add the letter to the dictionary with a count of 0
            
        map[letter] += 1 # increment the count of the letter in the dictionary, if the letter was new as was added in the if statement it will have a count of 1 after this line
    
    balloon_count = min(map.get('b', 0), map.get('a', 0), map.get('l', 0) // 2, map.get('o', 0) // 2, map.get('n', 0)) # get the minimum number of occurences of the letters in the string that are in the string 'balloon'
    
    return balloon_count # return the number of balloons that can be obtained from the letters in the string
    
print(maxNumberOfBalloons("nlaebolko")) # 1
print(maxNumberOfBalloons("loonbalxballpoon")) # 2
print(maxNumberOfBalloons("leetcode")) # 0
            