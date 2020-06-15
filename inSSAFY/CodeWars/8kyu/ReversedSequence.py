# Reversed sequence

def reverse_seq(n):
    lst = []
    for i in range(n):
        lst.append(n-i)
    return lst