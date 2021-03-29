import statistics

def init_matrix(fisier, fisier2):
    g = open(fisier,"r")
    ng = int(g.readline())
    xg = int(g.readline())
    yg = int(g.readline())
    g.readline()
    a=[]
    b=[]
    c=[]
    for i in range(ng):
        a.append(float(g.readline()))
    g.readline()
    for i in range(ng-1):
        b.append(float(g.readline()))
    g.readline()
    for i in range(ng-1):
        c.append(float(g.readline()))
    g.readline()

    h = open(fisier2, "r")
    nh = int(h.readline())
    h.readline()
    f1 = []
    for i in range(nh):
        for line in h:
            numar = float(line)
            f1.append(numar)
    g.close()
    return(a, b, c, f1)


def check_a(a1,a2,a3,a4,a5):
    if 0 in a1:
        print("A1 are element nul in diagonala")
    elif 0 in a2:
        print("A2 are element nul in diagonala")
    elif 0 in a3:
        print("A3 are element nul in diagonala")
    elif 0 in a4:
        print("A1 are element nul in diagonala")
    elif 0 in a5:
        print("A5 are element nul in diagonala")
    else:
        return True
    return False


a1, b1, c1, f1= init_matrix("a1.txt","f1.txt")

a2, b2, c2, f2= init_matrix("a2.txt","f2.txt")

a3, b3, c3, f3= init_matrix("a3.txt","f3.txt")

a4, b4, c4, f4= init_matrix("a4.txt","f4.txt")

a5, b5, c5, f5= init_matrix("a5.txt","f5.txt")

def init_A(a,b,c):
    A = []
    for i in range(len(a)):
        dict = {}
        A.append(dict)

    A[0][0] = a[0]
    A[0][1] = b[0]

    i = 1
    while i < len(a):
        if i == len(a) - 1:
            A[i][i - 1] = c[i - 1]
            A[i][i] = a[i]
        else:
            A[i][i - 1] = c[i - 1]
            A[i][i] = a[i]
            A[i][i + 1] = b[i]
        i += 1
    return A

A1 = init_A(a1,b1,c1)

A2 = init_A(a2,b2,c2)

A3 = init_A(a3,b3,c3)

A4 = init_A(a4,b4,c4)

A5 = init_A(a5,b5,c5)

if check_a(a1,a2,a3,a4,a5):
    print("Diagonale nenule")

p = -2
epsilon = 10 ** p


def solve_eq(a,b,c,f,epsilon, A):
    xp = [0]*len(a)
    xc = [0]*len(a)

    xc[0] = f[0] / A[0][0]
    i = 1

    while i < len(a) - 1:
        xc[i] = (f[i] - A[i][i - 1] * xc[i - 1]) / A[i][i]
        i += 1

    delta = xc.copy()
    k = 1

    while min(delta) > epsilon and max(delta) < 10**8 or k < 10000:

        xp.clear()
        xp = xc.copy()

        xc[0] = f[0] / A[0][0]
        i = 1
        while i < len(a) - 1:
            xc[i] = ( f[i] - A[i][i-1] * xc[i-1] - A[i][i+1] * xp[i+1]) / A[i][i]
            i += 1

        i = 0
        while i < len(xc):
            delta[i] = abs(xc[i] - xp[i])
            i += 1

        if min(delta) <= epsilon:
            k = 1000000

        k += 1

    return xc




result1 = solve_eq(a1,b1,c1,f1,epsilon,A1)
print(statistics.mean(result1))

result2 = solve_eq(a2,b2,c2,f2,epsilon,A2)
print(statistics.mean(result2))

result3 = solve_eq(a3,b3,c3,f3,epsilon,A3)
print(result3)

result4 = solve_eq(a4,b4,c4,f4,epsilon,A4)
print(result4)

result5 = solve_eq(a5,b5,c5,f5,epsilon,A5)
print(statistics.mean(result5))










