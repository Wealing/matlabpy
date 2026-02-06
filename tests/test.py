from matlabpy import *

A = mat("1 2; 3 4")
B = mat("5 6; 7 8")

print(A * B)          # matrix multiply
print(A.emul(B))     # elementwise multiply
print(A ** 2)
print(A(1,2))         # MATLAB-style indexing
