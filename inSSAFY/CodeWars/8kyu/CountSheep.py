# If you can't sleep, just count sheep!!

def count_sheep(N):
    a = []
    for i in range(N):
        a.append(f'{i+1} sheep...')
    return ''.join(a)