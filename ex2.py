import numpy as np
matrix=np.array([[5,6,7],
                 [7,3,2],
                 [3,4,5]])
U,S,VT=np.linalg.svd(matrix)
print("left singular vectors")
print(U)
print("singular values")
S=np.diag(S)
print(S)
print("right singular vectors")
print(VT)
rec_matrix=np.dot(U,np.dot(np.diag(S),VT))
print(rec_matrix)