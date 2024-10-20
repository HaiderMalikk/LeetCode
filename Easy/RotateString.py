# a simple solution to rotate string
# goal is so see if s the string is equal to goal the str by rotating it one rotaion is first element to end of array 
# here we see if n rotates can give us goal so s= "abcd" and goal = "bcda" is true as after one shift s == goal it can take 0 t on shifts where n is the length of the string as when we get back to the orignal str after n shifts we are done and return false 
def rotateString(s: str, goal: str) -> bool:
    # make two arrys for each string and goal
    strarr = []
    goalarr = []
    # loop over the strings and make a string array out of the two strings do we can rotate easily
    for char in s:
        strarr.append(char)
    for char in goal:
        goalarr.append(char)

    # loop over the array of strings the range here is the length of the strarr made of cahrs is 's' 
    # BUT! here you can choose any string to loop over as if the two strings are of different length they will never be equal and ist false
    for char in range(len(strarr)):
        temp = strarr[0] # store the first element in the array
        strarr.pop(0)  # with the first element stored we can pop it ie remove it from the list
        strarr.append(temp) # now we can append the first element witch we stored in temp, the append method always appends to the end of the list
        # if at any rotaion (ie any iteration of our loop) the two arrays are equal then we have found a rotation that statisfies s == g and we are done and can return true
        if strarr == goalarr:
            return True

    # if we escape our loop that means we have not found a rotation where s == goal so we return false
    return False

# some test cases
print(rotateString("abcde", "cdeab")) # True
print(rotateString("abcde", "abced"))  # False
print(rotateString("abcde", "cdab"))   # False
print(rotateString("abcde", "abcde"))  # True