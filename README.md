# Matrix_42

A comprehensive Python implementation of fundamental Linear Algebra operations using Vector and Matrix classes. This project formalizes vector spaces, matrices, and linear transformations through practical implementations.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Exercises Overview](#exercises-overview)
- [Requirements](#requirements)
- [Examples](#examples)

## Features

This library implements the following Linear Algebra operations:

- **Vector Operations**: Addition, subtraction, scaling, dot product, norms, cross product
- **Matrix Operations**: Addition, subtraction, scaling, multiplication, transpose
- **Advanced Matrix Operations**: 
  - Trace computation
  - Row echelon form reduction
  - Determinant calculation
  - Matrix inversion
  - Rank determination
- **Utility Functions**:
  - Linear combination
  - Linear interpolation (lerp)
  - Cosine similarity / angle calculation
  - Linear mapping

## Project Structure

```
matrix_42/
├── vector.py                          # Base Vector class
├── matrix.py                          # Base Matrix class
├── init.sh                            # Setup script
├── Exercise00/                        # Add, Subtract, Scale
│   ├── add_subtract_scale.py
│   └── main.py
├── Exercise01/                        # Linear Combination
│   ├── linear_combination.py
│   └── main.py
├── Exercise02/                        # Linear Interpolation
│   ├── linear_interpolation.py
│   └── main.py
├── Exercise03/                        # Dot Product
│   ├── dot_product.py
│   └── main.py
├── Exercise04/                        # Vector Norms
│   ├── norm.py
│   └── main.py
├── Exercise05/                        # Cosine Similarity
│   ├── cosine.py
│   └── main.py
├── Exercise06/                        # Cross Product
│   ├── cross_product.py
│   └── main.py
├── Exercise07/                        # Matrix Multiplication
│   ├── linear_map_matrix_multiplication.py
│   └── main.py
├── Exercise08/                        # Matrix Trace
│   ├── trace.py
│   └── main.py
├── Exercise09/                        # Matrix Transpose
│   ├── transpose.py
│   └── main.py
├── Exercise10/                        # Row Echelon Form
│   ├── row_echelon_form.py
│   └── main.py
├── Exercise11/                        # Determinant
│   ├── determinant.py
│   └── main.py
├── Exercise12/                        # Matrix Inverse
│   ├── inverse.py
│   └── main.py
└── Exercise13/                        # Matrix Rank
    ├── rank.py
    └── main.py
```

## Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd matrix_42
```

2. **Run the initialization script** (if needed):
```bash
bash init.sh
```

3. **Ensure Python 3.x is installed**:
```bash
python3 --version
```

4. **Install dependencies** (if any):
```bash
pip install numpy
```

## Usage

### Basic Vector Operations

```python
from vector import Vector

# Create vectors
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Addition
v1.add(v2)  # v1 becomes [5, 7, 9]

# Subtraction
v1.sub(v2)  # v1 becomes [1, 2, 3]

# Scaling
v1.scl(2)   # v1 becomes [2, 4, 6]

# Dot product
dot = v1.dot(v2)

# Norm (Euclidean by default)
norm = v1.norm()
```

### Basic Matrix Operations

```python
from matrix import Matrix

# Create matrices
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# Addition
m1.add(m2)

# Subtraction
m1.sub(m2)

# Scaling
m1.scl(2)

# Matrix multiplication
result = m1.mul_mat(m2)

# Transpose
transposed = m1.transpose()

# Determinant (for square matrices)
det = m1.determinant()

# Trace
trace = m1.trace()

# Inverse
inv = m1.inverse()

# Rank
rank = m1.rank()

# Row echelon form
ref = m1.row_echelon()
```

## Exercises Overview

### Exercise 00: Add, Subtract, Scale
Basic vector and matrix operations using decorator pattern to extend functionality.

### Exercise 01: Linear Combination
Computes linear combinations of vectors: `a × v1 + b × v2 + ... + m × vn`

### Exercise 02: Linear Interpolation (lerp)
Interpolates between two values (scalars, vectors, or matrices) using parameter `t ∈ [0, 1]`.

### Exercise 03: Dot Product
Calculates the dot product between two vectors.

### Exercise 04: Norms
Implements various vector norms (Euclidean, Manhattan, etc.).

### Exercise 05: Cosine Similarity
Computes the cosine of the angle between two vectors.

### Exercise 06: Cross Product
Calculates the cross product of two 3D vectors.

### Exercise 07: Matrix Multiplication
Implements linear mapping and matrix-matrix multiplication.

### Exercise 08: Trace
Computes the trace (sum of diagonal elements) of a square matrix.

### Exercise 09: Transpose
Transposes a matrix (swaps rows and columns).

### Exercise 10: Row Echelon Form
Reduces a matrix to row echelon form using Gaussian elimination.

### Exercise 11: Determinant
Calculates matrix determinant using Gaussian elimination with partial pivoting.

### Exercise 12: Matrix Inverse
Computes the inverse of an invertible square matrix.

### Exercise 13: Matrix Rank
Determines the rank of a matrix (dimension of column/row space).

## Requirements

- Python 3.x
- NumPy (for type hints and some utilities)
- No other external dependencies

## Examples

### Running Individual Exercises

Each exercise has a `main.py` file with example usage:

```bash
cd Exercise00
python3 main.py
```

### Linear Combination Example

```python
from vector import Vector
from Exercise01.linear_combination import linear_combination

# Define vectors and coefficients
vectors = [Vector([1, 0]), Vector([0, 1])]
coefficients = [2, 3]

# Compute linear combination: 2*[1,0] + 3*[0,1] = [2,3]
result = linear_combination(vectors, coefficients)
```

### Linear Interpolation Example

```python
from Exercise02.linear_interpolation import lerp
from vector import Vector

u = Vector([0, 0])
v = Vector([10, 10])

# Get midpoint
mid = lerp(u, v, 0.5)  # Returns Vector([5, 5])
```

### Matrix Operations Example

```python
from matrix import Matrix

# Create a 3x3 matrix
m = Matrix([[1, 2, 3],
            [0, 1, 4],
            [5, 6, 0]])

# Get various properties
print(f"Shape: {m.shape()}")           # (3, 3)
print(f"Is square: {m.is_square()}")   # True
print(f"Determinant: {m.determinant()}")
print(f"Rank: {m.rank()}")
print(f"Trace: {m.trace()}")
```

## Learning Objectives

This project helps you understand:

- Vector spaces and linear combinations
- Matrix operations and properties
- Linear transformations
- Gaussian elimination and row reduction
- Determinants and their properties
- Matrix invertibility
- Rank and dimension concepts

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License

This project is part of the 42 curriculum.

---

**Note**: This implementation uses a decorator pattern to extend the functionality of the base `Vector` and `Matrix` classes, keeping the code modular and organized.
