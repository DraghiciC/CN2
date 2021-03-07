import math
#citire din fisier a matricei
eps=0.00001
n = 3
A = [[2.25, 3, 3],
    [3, 9.0625, 13],
    [3, 13, 24]]
b=[9,35.0625,61]
diagonal=[A[i][i] for i in range(n)]
print("A :")
for a in range(n):
    print(A[a])

print("Diagonal ",diagonal)
def Cholesky_Decomposition(A, n):
    for i in range(n):
        for j in range(n):
            if j<=i:
                A[i][j]=0
    print("A after replacement with 0")
    for a in range(n):
        print(A[a])
    for i in range(n):
        for j in range(i + 1):
            s = 0
            if (j == i):
                for k in range(j):
                    s += pow(A[j][k], 2)
                A[j][j] = float(math.sqrt(diagonal[j] - s))
            else:
                for k in range(j):
                    s += (A[i][k] * A[j][k]);
                if (A[j][j] > 0):
                    A[i][j] = float((A[j][i] - s) /
                                      A[j][j]);
        for a in range(n):
            print(A[a])
    print("After Cholesky Decomposition")
    print("A :")
    for a in range(n):
        print(A[a])
    return A

def Determinant(A,n):
    det=1
    for i in range(n):#calcul determinant L
        det*=A[i][i]
    det*=det #calcul determinant A
    return det
A=Cholesky_Decomposition(A, n)
d=Determinant(A,n)

