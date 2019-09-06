import sys
sys.stdin = open('possible_score_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    points = list(map(int, input().split()))

