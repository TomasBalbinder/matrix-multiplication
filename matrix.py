from colorama import Fore, Style    # just colored text
import random

# Creating Matrix A
print("Matrix A")
width_a = int(input("width: "))     # Rows
height_a = int(input("height: "))   # Columns

print()

# Creating Matrix B
print("Matrix B")
width_b = int(input("width: "))     # Rows
height_b = int(input("height: "))   # Columns

print()

# This if statement is checking your matrix for possibility to be multiplied
# If Matrix A Columns not equal to Matrix B Rows, the can't be multiplied
if width_a != height_b:
    print('A matrix width not equal to B matrix height!')
    raise SystemExit

def matrix_A(height_A, width_A):    # Creating Matrix A
    matrix_ar_A = []

    for i in range(height_A):
        matrix_ar_A.append([])
        for j in range(width_A):
            matrix_ar_A[i].append(random.randrange(1,9))
    return matrix_ar_A

def matrix_B(height_B, width_B):    # Creating Matrix B
    matrix_ar_B = []

    for i in range(height_B):
        matrix_ar_B.append([])
        for j in range(width_B):
            matrix_ar_B[i].append(random.randrange(1,9))

    return matrix_ar_B

def matrix_C(matrix_A, matrix_B):   # Making Matrix matrix_c
    matrix_ar_c = []

    for i in range(len(matrix_A)):  # First iteration is for Rows of Matrix A
        c_row = []
        for j in range(len(matrix_B[0])):  # Second for Rows of Matrix B
            total = 0
            for k in range(len(matrix_B)):  # Third for Columns
                value = matrix_A[i][k] * matrix_B[k][j]
                total += value
            c_row.append(total)
        matrix_ar_c.append(c_row)

    return matrix_ar_c

print("Matrix A values:")
for n in matrix_A(width_a, height_a):   # separates brackets for better readability
    print(Fore.RED + " ".join(str(s) for s in n))
print(Style.RESET_ALL)


print("Matrix B values:")
for n in matrix_B(width_b, height_b):
    print(Fore.RED + " ".join(str(s) for s in n))
print(Style.RESET_ALL)


print("Result:")    # Prints the resulting matrix
for n in matrix_C(matrix_A(width_a, height_a), matrix_B(width_b, height_b)):
   print(" ".join(str(s) for s in n))