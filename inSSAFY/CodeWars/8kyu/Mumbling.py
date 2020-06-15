# Mumbling

def accum(s):
    A = []
    for i, c in enumerate(s):
        A.append(c.upper()+c.lower()*i)
    return '-'.join(A)