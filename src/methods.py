import numpy as np

def jacobi(system):
    A = system.A
    b = system.b
    x = system.x
    N = system.N
    t = system.t

    D = np.diag(A)
    R = A - np.diagflat(D)
    print('\n- Iniciando iteração do sistema "%s" pelo método "%s"' % (system.i, 'jacobi'))
    if not system.d:
        print('A matriz não é diagonal dominante, portanto, não é possível utilizar o método iterativo.')
        return None
    print('Iteração N: - (Vetor da solução) - (Vetor da variação)')

    v = np.zeros(len(A[0]))
    print('Iteração %s: - %s - %s' % (0, x, v))
    for k in range(N):
        x_old = x.copy()
        x = (b - np.dot(R,x)) / D
        for i in range(A.shape[0]):
            v[i] = abs((x[i] - x_old[i]))
        print('Iteração %s: - %s - %s' % (k+1, x, v))
        if v.max() <= t:
            break

    return x

def seidel(system):
    A = system.A
    b = system.b
    x = system.x
    N = system.N
    t = system.t

    print('\n- Iniciando iteração do sistema "%s" pelo método "%s"' % (system.i, 'seidel'))
    if not system.d:
        print('A matriz não é diagonal dominante, portanto, não é possível utilizar o método iterativo.')
        return None
    print('Iteração N: - (Vetor da solução) - (Vetor da variação)')

    v = np.zeros(len(A[0]))
    print('Iteração %s: - %s - %s' % (0, x, v))
    for k in range(N):
        x_old = x.copy()
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
            v[i] = abs((x[i] - x_old[i]))
        print('Iteração %s: - %s - %s' % (k+1, x, v))
        if v.max() <= t:
            break

    return x

def invert(system):
    print('\n- Iniciando inversão da matriz A do sistema "%s"' % system.i)
    copy_A = system.A.copy()
    det = np.linalg.det(copy_A)
    if not det:
        print('O determinante da matriz é nulo, portanto, não há matriz inversa.')
        return None
    inv_A = np.linalg.inv(copy_A)
    return inv_A
