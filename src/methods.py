import numpy as np

def gauss_jacobi(system, x=None, N=100, t=0.001):
    A = system.A
    b = system.b
    if x is None:
        x = np.zeros(len(A[0]))

    D = np.diag(A)
    R = A - np.diagflat(D)
    if D.max() == 0.0 and D.min() == 0.0:
        return x

    for k in range(1, N+1):
        print('%s - Interação %s: O vetor da solução é "%s"' % (system.i, k, x))
        x_old = x.copy()

        x = (b - np.dot(R,x)) / D

        LnormInf = max(abs((x - x_old))) / max(abs(x_old)) if k > 1 else 1
        print('%s - Interação %s: O valor da variação é "%s"' % (system.i, k, LnormInf))
        if LnormInf <= t:
            break

    return x

def gauss_seidel(system, x=None, N=100, t=0.001):
    A = system.A
    b = system.b
    if x is None:
        x = np.zeros(len(A[0]))

    if A.max() == 0.0 and A.min() == 0.0:
        return x

    for k in range(1, N+1):
        print('%s - Interação %s: O vetor da solução é "%s"' % (system.i, k, x))
        x_old = x.copy()

        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]

        LnormInf = max(abs((x - x_old))) / max(abs(x_old)) if k > 1 else 1
        print('%s - Interação %s: O valor da variação é "%s"' % (system.i, k, LnormInf))
        if LnormInf <= t:
            break

    return x
