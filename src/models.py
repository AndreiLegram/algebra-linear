import numpy as np

from itertools import permutations

class LinearSystem:
    def __init__(self, i, A, b):
        self.i = i
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.validate_dimensions()
        self.d = self.is_diagonally_dominant(self.A)
        if not self.d:
           self.d = self.make_diagonally_dominant()

    def validate_dimensions(self):
        """Ensure A and b have compatible dimensions."""
        if self.A.shape[0] != self.b.shape[0]:
            err = "O número de linhas em A deve corresponder ao número de linhas em b."
            raise ValueError(err)

    def is_diagonally_dominant(self, matrix=None):
        """Check if the matrix (or self.A) is diagonally dominant."""
        if matrix is None:
            matrix = self.A

        for i in range(matrix.shape[0]):
            sum_non_diag = np.sum(np.abs(matrix[i])) - abs(matrix[i, i])
            if abs(matrix[i, i]) < sum_non_diag:
                return False
        return True

    def make_diagonally_dominant(self):
        """Attempt to rearrange rows to make A diagonally dominant."""
        n = self.A.shape[0]
        for perm in permutations(range(n)):
            permuted_A = self.A[list(perm), :]
            if self.is_diagonally_dominant(permuted_A):
                self.A = permuted_A
                self.b = self.b[list(perm)]
                return True
        return False

    def __str__(self):
        return f"Matriz dos coeficientes A:\n{self.A}\n\nVetor das constantes b:\n{self.b}"
