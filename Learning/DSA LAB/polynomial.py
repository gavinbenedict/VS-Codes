def add(A, B, m, n):
    size = max(m, n)
    poly_sum = [0 for i in range(size)]
    for i in range(0, m, 1):
        poly_sum[i] = A[i]
    for i in range(n):
        poly_sum[i] += B[i]
    return poly_sum

def printPoly(poly, n):
    for i in range(n - 1, -1, -1):
        if poly[i] != 0:
            print(poly[i], end="")
            if i > 0:
                print("x^", i, end="")
            if i > 0:
                print(" + ", end="")

if __name__ == '__main__':
    A = [5, 0, 10, 6]
    B = [1, 2, 4]
    m = len(A)
    n = len(B)
    print("First polynomial is")
    printPoly(A, m)
    print("\n", end="")
    print("Second polynomial is")
    printPoly(B, n)
    print("\n", end="")
    poly_sum = add(A, B, m, n)
    size = max(m, n)
    print("sum polynomial is")
    printPoly(poly_sum, size)
