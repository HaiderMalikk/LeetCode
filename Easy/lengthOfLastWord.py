def lengthOfLastWord(s):
    words = [x for x in s.strip().split(' ')] # strip delets leading and traling white space , split (" ") splits the string at spaces
    LastWord = words[-1] # words is now a array with all our words -1 gets the last word
    return len(LastWord) # return the length of the last word

print(lengthOfLastWord("   hello  my     name   is   ali  ")) # you can see it has odd spaces and leading/ trailing white space
