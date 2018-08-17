def signed_shoelace(x, y, n):
    '''Takes a list x, a list y, and an int n.

    Returns the signed area of the polygon created by points x, y.
    To get the actual area of the polygon, call abs(signed_shoelace(x, y, n)).
    However, the sign of the result of this function will tell you whether the
    points inputted were in clockwise or anticlockwise order.'''
    a, b = 0, 0
    for i in range(n-1):
        a += (x[i] * y[i+1])
        b += (y[i] * x[i+1])
    a += x[n-1] * y[0]
    b += y[n-1] * x[0]
    return (a-b)/2.0
