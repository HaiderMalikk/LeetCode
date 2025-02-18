
def gcdOfStrings(str1,str2):
    str2builder = str2
    stop = len(str2)
    for i in range(len(str2)):
        flag = True
        ran = False
        for _ in range(len(str1)//len(str2builder) - 1):
            ran = True
            newstr = str2builder
            nextnewstr = str1[len(str2builder):len(str2builder) + len(str2builder)]
            if newstr != nextnewstr:
                flag = False
                break
        if flag and ran: return str2builder
        stop -= 1
        str2builder=str2builder[:stop]
    return ""
    
print(gcdOfStrings("ABCABC", "ABC"))# out: ABC
print(gcdOfStrings("ABABAB", "ABAB"))# out: AB
print(gcdOfStrings("LEET", "CODE"))# out: ""
print(gcdOfStrings("ABABABAB", "ABAB"))# out: ""ABAB""
