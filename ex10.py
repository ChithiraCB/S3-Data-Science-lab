import numpy as np
matrix=np.array([[5,6,7],
                 [9,5,6],
                 [3,4,5]])
U,S,VT=np.linalg.svd(matrix)
print("Left singular values")
print(U)
print("singular vectors")
S=np.diag(S)
print(S)
print("right singular values")
print(VT)
rec_matrix=np.dot(U,np.dot(np.diag(S),VT))
print(rec_matrix)