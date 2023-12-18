import numpy as np
row=int(input("enter number of rows"))
col=int(input("enter number of cols"))
matrix1=[]
print("enetr elemnts of first matrix")
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix1.append(a)
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end="")
    print()

matrix2=[]
print("enter elmts of 2nd matrix")
for i in range (row):
    a=[]
    for j in range (col):
        a.append(int(input()))
    matrix2.append(a)
for i in range (row):
    for j in range(col):
        print(matrix2[i][j],end="")
    print()
sum=np.add(matrix1,matrix2)
print(sum)
subtract=np.subtract(matrix1,matrix2)
print(subtract)
product=np.multiply(matrix1,matrix2)
print(product)
divide=np.divide(matrix1,matrix2)
print(divide)


