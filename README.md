# matlabpy

A Python library that replicates MATLAB-style matrix syntax and operators on top of NumPy.

It gives you:

✅ **MATLAB-like syntax & behavior**

## Features

### Matrix literals

```python
A = mat("1 2; 3 4")
```

### Matrix multiplication

```python
C = A * B
```

### Elementwise operations

```python
A.emul(B)   # A .* B
A.ediv(B)   # A ./ B
A.epow(2)   # A .^ 2
```

### Power

```python
A ** 2
```

### Transpose

```python
A.T
```

### MATLAB-style indexing

```python
A(1,2)   # 1-based indexing
```

### Concatenation

```python
M.hcat(A, B)   # [A B]
M.vcat(A, B)   # [A; B]
```

### Linear algebra helpers

```python
A.inv(), A.pinv(), A.det(), A.rank(), A.eig()
```

## Example usage

```python
from matlabpy import *

A = mat("1 2; 3 4")
B = mat("5 6; 7 8")

print(A * B)          # matrix multiply
print(A.emul(B))      # elementwise multiply
print(A ** 2)
print(A(1,2))         # MATLAB-style indexing
```

## Design philosophy

Instead of fighting Python syntax, this library:

*   Wraps NumPy cleanly
*   Preserves MATLAB mental models
*   Keeps everything fast + vectorized
*   Lets you gradually migrate MATLAB-style thinking into Pythonic code

This approach keeps cognitive friction extremely low, especially for engineers migrating MATLAB workflows into Python-based data platforms.

