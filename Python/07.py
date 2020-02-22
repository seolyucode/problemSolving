'''
리스트와 내장함수(1)
'''

import random as r
a=[]
# print(a)
b=list()
# print(b)

a=[1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b=list(range(1, 11))
# print(b)

c=a+b
# print(c)

print(a)
a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)

# 3번 인덱스 값 빼기
a.pop(3)
print(a)

# 4라는 값 찾아서 제거
a.remove(4)
print(a)

# a 리스트에서 5라는 값을 찾아서 인덱스 번호
print(a.index(5))

a=list(range(1, 11))
print(a)
print(sum(a))

# a 리스트 중 제일 큰 값
print(max(a))

# 가장 작은 값
print(min(a))


# 인자값들 중 가장 작은 값
print(min(7, 3, 5))

print(a)
r.shuffle(a)
print(a)

# 내림차순
a.sort(reverse=True)
print(a)

# a 오름차순
a.sort()
print(a)

a.clear()
print(a)