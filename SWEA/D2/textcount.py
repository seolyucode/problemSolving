T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    count = {}
    for n in str1:
        cnt = 0
        for m in str2:
            if n == m:
                cnt += 1
            count[n] = cnt

    print('#', tc, sep='', end=' ')
    print(max(count.values()))