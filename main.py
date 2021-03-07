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
def Calcul_X(A,n,b):
    print("Calculating X")
    x=[0 for i in range(n)]
    for i in range(n):
        aux=0
        for j in range(i):
            aux+=x[j]*A[i][j]
        x[i]=(b[i]-aux)/A[i][i]
    y = [0 for i in range(n)]
    for i in range(n):
        aux=0
        for j in range(i):
            aux+=y[n-j-1]*A[n-j-1][n-i-1]
        y[n-i-1]=(x[n-i-1]-aux)/A[n-i-1][n-i-1]
    print("x=",y)
    return y
def Calc_Norm(A,n,X,diagonal,b):
    print("testing result")
    result = [0 for i in range(n)]
    print(diagonal)
    for a in range(n):
        print(A[a])
    for i in range(n):
        aux=0
        for j in range(n):
            if i==j:
                aux+=diagonal[i]*X[j]
            elif j<i:
                aux+=X[j]*A[j][i]
            else:
                aux+=X[j]*A[i][j]
        result[i]=aux
    print("result=",result)
    print("b=",b)
    norm=0
    for i in range(n):
        norm+=pow(result[i]-b[i],2)
    norm=math.sqrt(norm)
    print("norm = ",norm)

A=Cholesky_Decomposition(A, n)
d=Determinant(A,n)
X=Calcul_X(A,n,b)
test=Calc_Norm(A,n,X,diagonal,b)

