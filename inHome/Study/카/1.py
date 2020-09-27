def solution(new_id):
    filter1 = new_id.lower()
    # print(filter1)

    filter2 = ""
    for i in filter1:
        if i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-", "_", "."]:
            filter2 += i 
        else:
            continue
    # print(filter2)
    
    filter3 = ""
    for i in range(len(filter2)):
        if i == 0:
            filter3 += filter2[i]
        elif filter3[-1] == filter2[i] and filter3[-1] == ".":
            continue
        else:
            filter3 += filter2[i]
    # print(filter3)

    filter4 = ""
    if filter3 != "": 
        if filter3[0] == ".":
            filter4 =  filter3[1:]
    if filter4 != "":
        if filter4[-1] == ".":
            filter4 = filter4[:-1]
    if filter4 != "":
        if filter4[0] != "." and filter4[-1] != ".":
            filter4 = filter4
    else:
        filter4 = filter3
    # print(filter4)

    filter5 = ""
    if filter4 == "":
        filter5 += "a"
    else:
        filter5 = filter4
    # print(filter5)
    # print(filter5[-1])
    filter6 = ""
    if len(filter5) >= 16:
        filter6 = filter5[:15]
    else:
        filter6 = filter5
    print(filter6)
    if filter6[-1] == ".":
        if len(filter6) == 1 and filter6 == ".":
            filter6 = "a"
        else:
            filter6 = filter6[:-1]
    # print(filter6)
    if len(filter6) <= 2:
        while(len(filter6) < 3):
            filter6 = filter6 + filter6[-1]
    # print(filter6)
    return filter6





# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
print(solution("=.="))
# print(solution("123_.def"))
# print(solution("-_.~!@#$%^&*()=+[{]}:?,<>"))
# print(solution("*"))
