def lone_sum(a, b, c):
    s = 0
    if a != b and a != c:
        s += a

    if b != a and b != c:
        s += b

    if c != a and c != b:
        s += c

    return s