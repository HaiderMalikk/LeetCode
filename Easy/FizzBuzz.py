def fizzBuzz(n:int) -> list: # n is type int and function returns type list
        answer = [] # as the user can choose the length of list start with a empty list
        count = 1 # first element is the number "1" not "0"

        for i in range(n): # now i is not doing anything here but still need proper syntax n is the users choice for number in list
            if count % 3 == 0 and count % 5 == 0: # this statement has to be first as we aleays check in we have a fizzbuzz before cheking fizz and buzz
                answer.append("FizzBuzz")
            elif count % 3 == 0: # fizz
                answer.append("Fizz")
            elif count % 5 == 0: #buzz
                answer.append("Buzz")
            else:
                answer.append(str(count)) # if not fizz buzz or fizzbuzz simply insert the number
            count += 1 # remember user has list length choice the first iteration 'count' or answer[0] will be 1 this for loop for the first time ran with the number 1, after count +1 its running answer[1] the number 2 and so on

        return answer # return final list

# print
solution = fizzBuzz(15) # n = 15
print(solution)
