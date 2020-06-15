'''
/**************************************************************
    Problem: 529
    User: seolyu
    Language: Python3
    Result: Success
    Time:33 ms
    Memory:25044 kb
****************************************************************/
''' 
 
height, weight = map(int, input().split())
 
obesity = weight+100-height
print(obesity)
 
if obesity > 0:
    print('Obesity')

'''
h, w = list(map(int, input().split()))
print(w + 100 - h)
if w + 100 - h > 0:
    print('Obesity')
'''