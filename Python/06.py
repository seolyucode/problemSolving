'''
문자열과 내장함수
'''

msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)  # 원본은 그대로

tmp = msg.upper()
print(tmp)
print(tmp.find('T'))  # T를 찾아서 index 번호(처음으로 찾은)
print(tmp.count('T'))
print(msg)
print(msg[:2])  # 제일 처음부터 2번 전까지. 0번부터 1번까지
print(msg[3:5])  # 3, 4만
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end='')
print()

# 아스키넘버
# A 는 65
# Z 는 90
# ord() 는 아스키 넘버 출력해줌
tmp='AZ'
for x in tmp:
    print(ord(x))

tmp='az'
for x in tmp:
    print(ord(x))

tmp=65
print(chr(tmp))