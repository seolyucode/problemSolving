# Count by X

def count_by(x, n):
    lst = []
    for i in range(n):
        lst.append(x+x*i)
    return lst