# 리모컨
# 브루트포스

# 이동할 채널 C를 정함 -> C에 포함된 숫자 중 고장난 버튼 있는지 확인(이게 더 구현 쉬우니까)
# -> 고장난 버튼이 포함 안되어있다면 |C-N|을 계산해 + / - 버튼 몇 번 눌러야 하는지 계산
## 수를 문자열로 바꾼 후, 한 글자씩 검사
## 수를 10으로 계속해서 나누면서 하나씩 검사

# 숫자 버튼을 누르고 +/- 중 하나만 연속해서 눌러야 최소가 됨
# + / - 누르는 횟수는 뺄셈을 이용

n = int(input())
m = int(input())
broken = [False] * 10

if m > 0:
    a = list(map(int, input().split()))
else:
    a = []

for x in a:  # 고장난 버튼 기록
    broken[x] = True
    
def possible(c):  # 불가능하면 0, 가능하면 버튼을 눌러야 하는 횟수(수의 자릿수)를 리턴
    if c == 0:  # 예외 처리
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l  # 길이를 리턴

ans = abs(n-100) # 숫자 버튼을 누르지 않는 경우 먼저 처리

for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-n)
        if ans > l + press:
            ans = l + press
        
print(ans)