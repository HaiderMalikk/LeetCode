def freqAlphabets(s: str) -> str:
    # dictionary mapping the numbers to letters
    mapping = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
    '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', 
    '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'
    }
    newStr = '' # new string to store the new string we will create in the loop
    # the problem is that not each letter has a mapping some are numbers and some are letters FOR EX 10# is j but the loop with just character iteration will treat this as 3 chars
    # SOLUTION use index to iterate through the string this will keep track of where we are and allow us to skip indexs
    # as when we incounter a # we will take it and the next two chars and see if these 3 chars are in our dictionary but we need to skip over those 2 chars + # after we do this so we use the index i and increment it 
    i = 0 # index for loop
    
    # we will use a while loop as we have our own index to keep track of where we are
    while i < len(s):
        # if current char is '#', process the last three chars as a number with # included make sure to check the length of the str to make sure we dont go out of bounds
        if i + 2 < len(s) and s[i + 2] == '#':
            # grab the two characters ofer # plus the '#'
            num_with_hash = s[i:i + 2] + '#' # this says take the index of s starting at i and ending right before i + 2 and add '#' to it
            if num_with_hash in mapping: # now with this new key we check if its in teh mapping dictionary 
                newStr += mapping[num_with_hash] # if it is add it no new str
            i += 3  # skip the next two chars and '#' are skipped now as we are done with them 
        else:
            # otherwise it's a single digit we know we can treat it as a char
            if s[i] in mapping:
                newStr += mapping[s[i]] # if it is add it to the new string
            i += 1  # move to the next character by 1 only as we incounterd a single char here
    
    return newStr # return the new string

# test cases
print(freqAlphabets("10#11#12"))  # output: "jkab"
print(freqAlphabets("1326#"))     # output: "acz"
