import sys
sys.stdin = open('Contact_input.txt', 'r')

T = 10
for t in range(1, T+1):
    length, start = map(int, input().split())
    from_to = list(map(int, input().split()))
    edge = []

    for s in range(length//2):
        edge.append(from_to[2*s:2*s+2])

    q = [start]
    visited = [start]
    path = []

    while q:
        current_length = len(q)
        next_numbers = []

        for i in range(current_length):
            current = q.pop(0)

            for send, receive in edge:
                if current == send and receive not in visited:
                    q.append(receive)
                    visited.append(receive)
                    next_numbers.append(receive)

        path.append(next_numbers)
    print("#{} {}".format(tc, max(path[-2])))