import numpy as np

from itertools import permutations

class LinearSystem:
    def __init__(self, i, **kwargs):
        self.i = i
        self.A = np.array(kwargs['A'], dtype=float)
        self.b = np.array(kwargs['b'], dtype=float) if 'b' in kwargs else np.zeros(len(self.A[0]))
        self.x = np.array(kwargs['x'], dtype=float) if 'x' in kwargs else np.zeros(len(self.A[0]))
        self.N = kwargs['N'] if 'N' in kwargs else 100
        self.t = kwargs['t'] if 't' in kwargs else 0.001
        self.validate_dimensions()
        self.d = self.is_diagonally_dominant(self.A)
        if not self.d:
           self.d = self.make_diagonally_dominant()

    def validate_dimensions(self):
        """Ensure A and b have compatible dimensions."""
        if self.A.shape[0] != self.b.shape[0]:
            err = 'O vetor "b" deve corresponder ao número de linhas da matriz A.'
            raise ValueError(err)
        if self.A.shape[0] != self.x.shape[0]:
            err = 'O vetor "x" deve corresponder ao número de linhas da matriz A.'
            raise ValueError(err)

    def is_diagonally_dominant(self, matrix=None):
        """Check if the matrix (or self.A) is diagonally dominant."""
        if matrix is None:
            matrix = self.A

        for i in range(matrix.shape[0]):
            sum_non_diag = np.sum(np.abs(matrix[i])) - abs(matrix[i, i])
            if abs(matrix[i, i]) <= sum_non_diag:
                return False
        return True

    def make_diagonally_dominant(self):
        """Attempt to rearrange rows to make A diagonally dominant."""
        n = self.A.shape[0]
        print('\nPermutando linhas da matriz A do sistema "%s"...' % self.i)
        for perm in permutations(range(n)):
            permuted_A = self.A[list(perm), :]
            if self.is_diagonally_dominant(permuted_A):
                self.A = permuted_A
                self.b = self.b[list(perm)]
                print('Permutação concluída. Agora a nova matriz é:\n%s' % self.A)
                return True
        print('Não foi possível permutar, não há diagonal dominante.')
        return False

    def __str__(self):
        return f"Matriz dos coeficientes A:\n{self.A}\n\nVetor das constantes b:\n{self.b}"
