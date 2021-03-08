import math
import numpy as np
import scipy
import scipy.linalg
#citire din fisier a matricei
eps=0.00001
n = 3
A = [[2.25, 3, 3],
    [3, 9.0625, 13],
    [3, 13, 24]]
b=[9,35.0625,61]
diagonal=[A[i][i] for i in range(n)]
print("Given A:")
for a in range(n):
    print(A[a])

def Cholesky_Decomposition(A, n):
    for i in range(n):
        for j in range(n):
            if j<=i:
                A[i][j]=0
    """
    print("A after replacement with 0")
    for a in range(n):
        print(A[a])
    """
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
        """
        for a in range(n):
            print(A[a])
   
    print("After Cholesky Decomposition")
    print("A :")
    for a in range(n):
        print(A[a])
    """
    return A

def ch_dec(A,n):
    L = np.linalg.cholesky(A)
    return (L,L.transpose())



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

def LU_decomposition(A):
   s_A = np.array(A)
   P, L, U = scipy.linalg.lu(s_A)
   return (L,U)

def solve_eq(A,b):
    L, U = LU_decomposition(A)
    b2 = np.array(b)
    x = np.linalg.solve(A,b2)
    print("x from Ax = b is: ",x)

def solve_eq2(A,b):
    #gasim Y a i L*y =  b
    L,U = LU_decomposition(A)
    L = np.array(L)
    U = np.array(U)
    x_ante_anterior = b[0] / L[0][0]
    x_anterior = (b[1] - L[1][0] * x_ante_anterior) / L[1][1]
    x3 =(b[2] - (L[2][0]*x_ante_anterior + L[2][1]*x_anterior))/L[2][2]
    x = [x_ante_anterior, x_anterior,x3]
    n = len(b)
    i = 3

    while i < n-1:
        j = 0
        sum = 0
        while j < i-1:
            sum = sum + L[i][j]*x[j]
            j += 1
        x.append(( b[i] - sum ) / L[i][i])
        i += 1

    y = x
    print("Y is: ", y)
    #second part: gasim x a.i. U*x = y
    xn = y[n-1] / U[n-1][n-1]
    xn2 = ( y[n-2] - U[n-2][n-1] * xn) / U[n-2][n-2]
    x3 = (y[n-3] - U[n-3][n-1]*xn2 - U[n-2][n-1]*xn ) / U[n-3][n-3]
    new_x = [x3, xn2,xn]
    j = i + 1
    sum = 0
    while j < n-1:
        sum = sum + U[i][j]*new_x[j]
        j += 1
    i = n - 4
    while i >= 0:
        sum = sum + U[i][i+1]*new_x[i+1]
        new_x.append((y[i] - sum) / U[i][i])
        i -= 1
    print("x is: ", new_x)







def inverse_Cholesky(A,n):
    A = Cholesky_Decomposition(A,n)
    inversa = np.linalg.inv(A)
    print("\n")
    return inversa


def inverse_Cholesky2(A,n):
    L = np.linalg.cholesky(A)
    T = L.transpose()
    j = 0
    size = n*n
    ej = [0] * size
    
    
    inversa = np.empty([n, n])
    print(inversa)
    while j < n - 1:
        ej[j] = 1
        matrix = np.array(ej)
        b = matrix.transpose()
        """
        y = np.linalg.solve(L,b)
        x = np.linalg.solve(T,y)
        """
        x = np.linalg.solve(A,b)
        inversa[j][:] = x
        j += 1

    print("Inversa: ")
    return inversa



"""
print("Inversa descompunerii Cholesky: ")
print(inverse_Cholesky(A,n))
"""
#solve_eq(A,b)
print("\n")
print(inverse_Cholesky2(A,n))
print("Cholesky Decomposition:")
print(np.array(Cholesky_Decomposition(A, n)))
print("\n Inverse of Cholesky:")
print(inverse_Cholesky(A,n))


"""
d=Determinant(A,n)
X=Calcul_X(A,n,b)
test=Calc_Norm(A,n,X,diagonal,b)
"""
