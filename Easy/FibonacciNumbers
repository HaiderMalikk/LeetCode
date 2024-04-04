def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2) # each number is the sum of the two prevous ones ones

print(fib(4))
# explaination: n = 4
# F(4) = F(4-1) + F(4-2) F(3) + F(2) // this is ran recusivly in else statement
# F(3) = F(3-1) + F(3-2) = F(2) + F(1) // here F(2) = F(1) + F(0) as now n <=1 so it returns 1 for F(1) as 1 = n and 0 for F(0) as 0 = n 
# so F(2) = 1 + 0 = 1 // and F(1) = 1 from above
# so F(3) = F(2) + F(1) = 1 + 1 = 2
# then we go back to F(4), which becomes F(3) + F(2) = 2 + 1 = 3
# so F(4) is 3