# 2050. 알파벳을 숫자로 변환

str = input()
 
for i in range(len(str)):
    print(ord(str[i])-64, end=' ')