def solution(n, plans):
    # 이차원 배열
    # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    two_dimensional_array = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0) #[0, 0, 0, 0, 0]
        two_dimensional_array.append(temp)

    # 두번째 방법
    two_dimensional_array2 = [[0] * n for _ in range(n)] # [0, 0, 0, 0, 0]
    for i in range(n):
        for j in range(n):
            two_dimensional_array2[i][j] = 2

    print(two_dimensional_array,'\n', two_dimensional_array2)
    for line in two_dimensional_array:
        print(line)
    print(two_dimensional_array)
    print(two_dimensional_array2)



print(solution(5, ['R','R','R','U','D','D']))