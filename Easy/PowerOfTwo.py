def solution(x):
    if x == 1:
        return True
    
    sol = 2
    for i in range(x):
        if x == sol:
            return True
        else:
            sol = sol * 2

    else:
        return False
    

print(solution(16))