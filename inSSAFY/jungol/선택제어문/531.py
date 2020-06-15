'''
/**************************************************************
    Problem: 531
    User: seolyu
    Language: Python3
    Result: Success
    Time:43 ms
    Memory:25176 kb
****************************************************************/
'''
 
weight = float(input())
 
if weight > 88.45:
    print('Heavyweight')
elif weight > 72.57:
    print('Cruiserweight')
elif weight > 61.23:
    print('Middleweight')
elif weight > 50.80:
    print('Lightweight')
else:
    print('Flyweight')

'''
w = float(input())
 
if w <= 50.80:
    print('Flyweight')
elif w <= 61.23:
    print('Lightweight')
elif w <= 72.57:
    print('Middleweight')
elif w <= 88.45:
    print('Cruiserweight')
elif w > 88.45:
    print('Heavyweight')
'''