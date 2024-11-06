import numpy as np

def jacobi(system, x=None, N=100, t=0.001):
    A = system.A
    b = system.b
    if x is None:
        x = np.zeros(len(A[0]))

    D = np.diag(A)
    R = A - np.diagflat(D)
    print('- Iniciando iteração do sistema "%s" pelo método "%s"' % (system.i, 'jacobi'))
    print('Interação N: - (Vetor da solução) - (Valor da variação)')
    if not system.d or (D.max() == 0.0 and D.min() == 0.0):
        return x

    for k in range(N):
        x_old = x.copy()
        x = (b - np.dot(R,x)) / D
        v = max(abs((x - x_old))) / max(abs(x_old)) if k > 1 else 1
        print('Interação %s: - %s - %s' % (k, x_old, v))
        if v <= t:
            break

    return x

def seidel(system, x=None, N=100, t=0.001):
    A = system.A
    b = system.b
    if x is None:
        x = np.zeros(len(A[0]))

    print('- Iniciando iteração do sistema "%s" pelo método "%s"' % (system.i, 'seidel'))
    print('Interação N: - (Vetor da solução) - (Valor da variação)')
    if not system.d or (A.max() == 0.0 and A.min() == 0.0):
        return x

    for k in range(N):
        x_old = x.copy()
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
        v = max(abs((x - x_old))) / max(abs(x_old)) if k > 1 else 1
        print('Interação %s: - %s - %s' % (k, x_old, v))
        if v <= t:
            break

    return x

def invert(system):
    print('Iniciando inversão da matriz A do sistema "%s"' % system.i)
    copy_A = system.A.copy()
    inv_A = np.linalg.inv(copy_A)
    return inv_A
