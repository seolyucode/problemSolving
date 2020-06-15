# 2056. 연월일 달력

T = int(input())
DaysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(T):
    date = input()
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
 
    if (1<=month<=12 and 1<=day<=DaysOfMonth[month-1]):
         
        print('#', i+1, ' ', str(year).zfill(4), '/', str(month).zfill(2), '/', str(day).zfill(2), sep='')
    else:
        print('#',i+1, ' ', '-1', sep='')