def solution(info, query):
    lst = [0 for i in range(len(query))]
    a = 0
    for con in query:
        i = con.split(' ')
        cnt = 0
        for person in info:
            j = person.split(' ')
            if (i[0] == j[0] or i[0] == '-') and (i[2] == j[1] or i[2] == '-') and (i[4] == j[2] or i[4] == '-') and (i[6] == j[3] or i[6] == '-') and (int(j[4]) >= int(i[7])):
                cnt += 1
        lst[a] = cnt 
        a+=1
    return lst


print(solution(
    ["java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"]))