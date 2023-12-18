import numpy as np

row = int(input("enter no of rows"))
col = int(input("enter no of columns"))
matrix1 = []
print("enter elements of first matrix")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix1.append(a)

for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=" ")
    print()

matrix2 = []
print("enter elements of 2nd matrix")
for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input()))
    matrix2.append(a)
for i in range(row):
    for j in range(col):
        print(matrix2[i][j], end=" ")
    print()

sum = np.add(matrix1, matrix2)
print("sum is", sum)

subtract = np.subtract(matrix1, matrix2)
print("subtract is", subtract)

product = np.multiply(matrix1, matrix2)
print("product is :", product)

div = np.divide(matrix1, matrix2)
print("dividing :", div)

sqrt1 = np.sqrt(matrix1)
print("square root of matrix1 :", sqrt1)

sqrt2 = np.sqrt(matrix2)
print("square root of matrix2 :", sqrt2)

trans1 = np.transpose(matrix1)
print("transpose of matrix1 :", trans1)

trans2 = np.transpose(matrix2)
print("transpose of matrix2 :", trans2)

dot1 = np.dot(matrix1, matrix2)
print("dotproduct is:", dot1)





