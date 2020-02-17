# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    
    answer = True
    # if s[0] == ')':
    #     return False
    # elif s[0] == '(' and s[1] == '(':
    #     return False
    # elif s[0] == '(' and s[1] == ')' and len(s)==2:
    #     return True
    # else:
    count=0
    for i in s:
        if(i=="("):
            count+=1
        elif(count==0):
            return False
        else:
            count-=1
    
    return count==0

s=input()
print(solution(s))