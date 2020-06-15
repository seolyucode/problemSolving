# 선택 정렬 함수(Selection Sort)를 재귀적 알고리즘으로 작성

def SelectionSort(A):

    n = len(A)

    for i in range(0, n-1):

        min = i

        for j in range(i+1, n):
            if A[j] < A[min]:
                min = j

        A[min], A[i] = A[i], A[min]

    return A

def rec_SelectionSort(A, s, e):
    if s == e:
        return A

    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j

    A[s], A[mini] = A[mini], A[s]
    rec_SelectionSort(A, s+1, e)

    return A

lst = [3, 4, 2, 1, 5, 6]
print(SelectionSort(lst))
print(rec_SelectionSort(lst, 0, 5))