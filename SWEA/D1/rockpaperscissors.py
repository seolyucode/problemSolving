# 1936. 1대1 가위바위보

a, b = map(int, input().split())
if (b - a) == 1 or (b - a) == -2:
    print('B')
else:
    print('A')