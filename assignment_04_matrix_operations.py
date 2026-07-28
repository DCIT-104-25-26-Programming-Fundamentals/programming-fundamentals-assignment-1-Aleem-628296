# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row_data = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix.append(row_data)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("  ".join(f"{num:4}" for num in row))

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(mat1[i][j] + mat2[i][j])
        result.append(new_row)
    return result

def multiply_matrices(mat1, mat2):
    rows_a = len(mat1)
    cols_a = len(mat1[0])
    cols_b = len(mat2[0])
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += mat1[i][k] * mat2[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

def main():
    # --- PART A ---
    print("--- PART A: Transpose Matrix ---")
    r1 = int(input("Enter number of rows: "))
    c1 = int(input("Enter number of columns: "))
    mat_a = read_matrix(r1, c1)
    
    print("\nOriginal Matrix:")
    print_matrix(mat_a)
    print("\nTransposed Matrix:")
    print_matrix(transpose(mat_a))

    # --- PART B ---
    print("\n--- PART B: Add Two Matrices ---")
    r2 = int(input("Enter number of rows: "))
    c2 = int(input("Enter number of columns: "))
    
    print("Matrix 1:")
    mat_b1 = read_matrix(r2, c2)
    print("Matrix 2:")
    mat_b2 = read_matrix(r2, c2)
    
    print("\nMatrix 1:")
    print_matrix(mat_b1)
    print("\nMatrix 2:")
    print_matrix(mat_b2)
    print("\nSum:")
    print_matrix(add_matrices(mat_b1, mat_b2))

    # --- PART C ---
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter rows for Matrix A: "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B: "))
    p = int(input("Enter columns for Matrix B: "))
    
    print("Matrix A:")
    mat_c1 = read_matrix(m, n)
    print("Matrix B:")
    mat_c2 = read_matrix(n, p)
    
    print("\nMatrix A:")
    print_matrix(mat_c1)
    print("\nMatrix B:")
    print_matrix(mat_c2)
    print("\nProduct (A x B):")
    print_matrix(multiply_matrices(mat_c1, mat_c2))

if __name__ == "__main__":
    main()
