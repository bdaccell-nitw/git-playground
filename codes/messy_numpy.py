import numpy as np

# === BUGS ===
# 1. Which command allow for reproducible results?
arr = np.random.rand(5) * 100  # Random array

# 2. Inefficient filtering!
filtered = []
for x in arr:
    if x > 50:
        filtered.append(x)
filtered = np.array(filtered)

# 3. Any better method to calculate mean?
total = 0
for num in arr:
    total += num
mean_val = total / len(arr)

# 4. Three loops for matrix multiplication - that's definitely not optimal
def matrix_mult(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    return result
  
# 5. Heard of multidimensional slicing?
def get_submatrix(matrix, rows, cols):
    submatrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix[i][j])
        submatrix.append(row)
    return submatrix 

# 6. NumPy uses SIMD, Did you know that?
def square_elements(arr):
    return list(map(lambda x: x**2, arr))

# 7. Does this work for 2D arrays?
def stack_vertically(a, b):
    return a + b
