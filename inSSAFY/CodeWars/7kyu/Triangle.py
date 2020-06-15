# Is this a triangle?

def is_triangle(a, b, c):
    if max(a, b, c) < a + b + c - max(a, b, c):
        return True
    else:
        return False

print(is_triangle(1, 2, 3))