def solution(ball, order):
    answer = []
    b = []
    for i in range(len(order)):
        if len(b) == 0:
            if len(ball) == 1:
                if ball[0] == order[i]:
                    answer.append(ball[0])
                    ball.pop()
            elif len(ball) == 2:
                for j in range(2):
                    if ball[j] == order[i]:
                        answer.append(ball[j])
                        ball.pop(j)
            else:
                if ball[0] == order[i]:
                    answer.append(ball[0])
                    ball.pop(0)
                elif ball[-1] == order[i]:
                    answer.append(ball[-1])
                    ball.pop()
                else:
                    for k in range(len(ball)):
                        if ball[k] == order[i]:
                            b.append(ball[k])
        else:
            while(ball[0] in b or ball[-1] in b):
                for a in range(len(b)):
                    if b[a] == ball[0]:
                        answer.append(ball[0])
                        ball.pop(0)
                        b.pop(a)
                        break
                    elif b[a] == ball[-1]:
                        answer.append(ball[-1])
                        ball.pop()
                        b.pop(a)
                        break
            if len(ball) == 1:
                if ball[0] == order[i]:
                    answer.append(ball[0])
                    ball.pop(0)
            elif len(ball) == 2:
                for j in range(2):
                    if ball[j] == order[i]:
                        answer.append(ball[j])
                        ball.pop(j)
            else:
                if ball[0] == order[i]:
                    answer.append(ball[0])
                    ball.pop(0)
                elif ball[-1] == order[i]:
                    answer.append(ball[-1])
                    ball.pop()
                else:
                    for k in range(len(ball)):
                        if ball[k] == order[i]:
                            b.append(ball[k])
                            
    return answer

# print(solution([1, 2, 3, 4, 5, 6], [6, 2, 5, 1, 4, 3]))
print(solution([11, 2, 9, 13, 24], [9, 2, 13, 24, 11]))

