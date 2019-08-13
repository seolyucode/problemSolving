# Multiples of 3 or 5

def solution(number):
    lst = []
    for i in range(1, number):
        if i%3==0 or i%5==0:
            lst.append(i)
    return sum(lst)