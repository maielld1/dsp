# Matrix Algebra


import numpy as np


A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])


print("1.1): " + str(A.shape))
print("1.2): " + str(B.shape))
print("1.3): " + str(C.shape))
print("1.4): " + str(D.shape))
print("1.5): " + str(u.shape))
print("1.6): " + str(w.shape))

a = 6

print("2.1): "  + str(u+v))
print("2.2): "  + str(u-v))
print("2.3): "  + str(a*u))
print("2.4): "  + str(u.dot(v)))
print("2.5): "  + str(np.linalg.norm(u)))

print("3.1): Not Defined")
print("3.2): \n"  + str(A-(C.transpose())))
print("3.3): \n"  + str(C.transpose() + 3*D))
print("3.4): \n"  + str(np.mat(B) * np.mat(A)))
print("3.5): Not Defined")
