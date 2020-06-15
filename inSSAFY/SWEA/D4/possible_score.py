# 3752. 가능한 시험 점수

import sys
sys.stdin = open('possible_score_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    points = list(map(int, input().split()))
    possible_scores = {0}

    for i in points:
        for j in list(possible_scores):
            possible_scores.add(i+j)

    print("#{} {}".format(tc, len(possible_scores)))