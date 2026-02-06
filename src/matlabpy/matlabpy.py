"""
matlabpy.py — A lightweight Python library that mimics core MATLAB matrix syntax & operators

Goals:
- MATLAB-like matrix construction: [1 2; 3 4]
- Elementwise vs matrix ops: + - * / ^ and .*, ./, .^
- Transpose: A.T and A' style via .T and .H
- Indexing: A(1,2) style via A(1,2) callable + Python slicing
- Concatenation: [A B; C D]

This is NOT a full MATLAB clone. It is a thin syntax layer over NumPy
intended for prototyping and familiarity, not performance-critical code.

Dependencies: numpy
"""

from __future__ import annotations
import numpy as np
from typing import Iterable, Tuple, Union

Number = Union[int, float, complex]


class M:
    """MATLAB-like matrix wrapper around NumPy arrays."""

    def __init__(self, data):
        if isinstance(data, M):
            self.A = data.A.copy()
        else:
            self.A = np.array(data, dtype=float)

    # --------------------------
    # Representation
    # --------------------------

    def __repr__(self):
        return f"M({self.A})"

    def __str__(self):
        return str(self.A)

    # --------------------------
    # Indexing
    # --------------------------

    def __call__(self, *idx):
        """MATLAB-style indexing A(i,j). 1-based."""
        idx = tuple(i - 1 if isinstance(i, int) else i for i in idx)
        return self.A[idx]

    def __getitem__(self, key):
        return self.A[key]

    def __setitem__(self, key, value):
        self.A[key] = value

    # --------------------------
    # Shape helpers
    # --------------------------

    @property
    def T(self):
        return M(self.A.T)

    @property
    def H(self):
        return M(self.A.conj().T)

    @property
    def shape(self):
        return self.A.shape

    # --------------------------
    # Arithmetic Operators
    # --------------------------

    def __add__(self, other):
        return M(self.A + _unwrap(other))

    def __sub__(self, other):
        return M(self.A - _unwrap(other))

    def __mul__(self, other):
        return M(self.A @ _unwrap(other))  # Matrix multiply

    def __truediv__(self, other):
        return M(self.A @ np.linalg.inv(_unwrap(other)))

    def __pow__(self, p):
        return M(np.linalg.matrix_power(self.A, p))

    # --------------------------
    # Elementwise ops (. *, ./, .^)
    # --------------------------

    def emul(self, other):
        return M(self.A * _unwrap(other))

    def ediv(self, other):
        return M(self.A / _unwrap(other))

    def epow(self, other):
        return M(self.A ** _unwrap(other))

    # --------------------------
    # Linear algebra helpers
    # --------------------------

    def inv(self):
        return M(np.linalg.inv(self.A))

    def pinv(self):
        return M(np.linalg.pinv(self.A))

    def det(self):
        return np.linalg.det(self.A)

    def rank(self):
        return np.linalg.matrix_rank(self.A)

    def eig(self):
        w, v = np.linalg.eig(self.A)
        return M(w), M(v)

    # --------------------------
    # Concatenation
    # --------------------------

    @staticmethod
    def hcat(*args):
        return M(np.hstack([_unwrap(a) for a in args]))

    @staticmethod
    def vcat(*args):
        return M(np.vstack([_unwrap(a) for a in args]))


# --------------------------
# MATLAB-style constructors
# --------------------------

def zeros(*shape):
    return M(np.zeros(shape))


def ones(*shape):
    return M(np.ones(shape))


def eye(n):
    return M(np.eye(n))


def rand(*shape):
    return M(np.random.rand(*shape))


def linspace(a, b, n=100):
    return M(np.linspace(a, b, n))


def diag(v):
    return M(np.diag(_unwrap(v)))


# --------------------------
# MATLAB-like matrix literal
# --------------------------

def mat(expr: str) -> M:
    """
    MATLAB-style matrix literal:

        mat("1 2 3; 4 5 6")
        mat("1,2,3;4,5,6")

    Supports:
      - spaces or commas as column separators
      - semicolon or newline as row separators
    """
    rows = expr.strip().replace("\n", ";").split(";")
    data = []
    for r in rows:
        r = r.strip()
        if not r:
            continue
        cols = [float(x) for x in r.replace(",", " ").split()]
        data.append(cols)
    return M(data)


# --------------------------
# Utilities
# --------------------------

def _unwrap(x):
    return x.A if isinstance(x, M) else x


# --------------------------
# Example usage
# --------------------------

if __name__ == "__main__":
    A = mat("1 2; 3 4")
    B = mat("5 6; 7 8")

    print("A =", A)
    print("B =", B)

    print("A * B =", A * B)
    print("A .* B =", A.emul(B))
    print("A^2 =", A ** 2)
    print("inv(A) =", A.inv())
    print("A(1,2) =", A(1, 2))

    C = M.hcat(A, B)
    D = M.vcat(A, B)

    print("[A B] =", C)
    print("[A; B] =", D)
