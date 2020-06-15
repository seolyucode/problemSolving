# 2070. 큰 놈, 작은 놈, 같은 놈

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if a > b:
        print('#', i+1, sep='', end=' ')
        print('>')
    elif a == b:
        print('#', i+1, sep='', end=' ')
        print('=')
    else:
        print('#', i+1, sep='', end=' ')
        print('<')