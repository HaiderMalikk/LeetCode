# TODO: FIX FAIL
def sol(arr):
    i = 0
    lenofpops = 0
    while i != len(arr) - 1:
        didrun = False
        if len(arr) == 1:
            return 0
        if i == 0:
            if arr[i+1] < arr[i]:
                arr.pop(i+1)
                lenofpops += 1
                i -= 1
        
        if arr[i+1] < arr[i]:
            if arr[i-1] <= arr[i+1]:
                arr.pop(i)
                lenofpops += 1
                didrun = True
                i -= 1
            elif arr[i-1] >= arr[i+1]:
                arr.pop(i+1)
                lenofpops += 1
                didrun == True
                i -= 1
        if didrun is False:
            i += 1        
    return lenofpops
        
print(sol([1,2,3,10,4,2,3,5])) # 3
print(sol([5,4,3,2,1])) # 4
print(sol([1,2,3])) # 0
print(sol([0,16,3,13,14,11,1,24,20,20,18,15,20])) # ! FAIL