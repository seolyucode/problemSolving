'''
리스트와 내장함수(2)
'''

a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])

# len 은 리스트 값 몇 개
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

# 인덱스 번호와 값
for x in enumerate(a):
    print(x)

# 튜플은 값 변경 불가
b=(1, 2, 3, 4, 5)
print(b[0])

# 리스트는 값 변경 가능
b=[1, 2, 3, 4, 5]
print(b[0])
b[0] = 7
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

# all 은 조건이 모두 참이어야 참
if all(50>x for x in a):
    print("YES")
else:
    print("NO")

# any 는 한번이라도 참이면 참
if any(15>x for x in a):
    print("YES")
else:
    print("NO")