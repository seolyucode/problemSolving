# [S/W 문제해결 기본] 2일차 - Sum

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
 
    row_sum=[]
    for i in arr:
        row_sum.append(sum(i))
 
    col_sum = []
    for i in range(len(arr[0])):
        col_num = []
        for j in range(len(arr)):
            col_num.append(arr[j][i])
        col_sum.append(sum(col_num))
 
    dia1=[]
    dia2=[]
    for i in range(len(arr)):
        dia1.append(arr[i][i])
        dia2.append(arr[len(arr)-(i+1)][i])
    dia1_sum = sum(dia1)
    dia2_sum = sum(dia2)
     
    print('#', tc, sep='', end=' ')
    print(max(max(row_sum), max(col_sum), dia1_sum, dia2_sum))