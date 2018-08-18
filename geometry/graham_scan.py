def direction(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

def graham_scan(pts):
    '''Given a list of points in the form [(x1, y1), (x2, y2), ...],
    return the convex hull in anticlockwise order starting with the lexicographically
    smallest point.'''
    # Remove duplicates
    pts = set(pts)
    n = len(pts)

    # Trivial case
    if n == 1:
        return pts

    pts = sorted(pts)

    U = []
    L = []
    for p in pts:
        while len(U) > 1 and direction(U[-2], U[-1], p) > 0:
            U.pop()
        while len(L) > 1 and direction(L[-2], L[-1], p) < 0:
            L.pop()
        L.append(p)
        U.append(p)
    H = L + U[1:-1][::-1]
    return H
