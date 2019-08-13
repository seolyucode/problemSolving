# 1545. 거꾸로 출력해 보아요

number = int(input())
for i in range(-1, number):
    i = number
    print(i, end = ' ')
    number = number - 1