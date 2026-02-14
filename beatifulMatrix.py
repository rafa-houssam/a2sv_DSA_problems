import numpy as np

matrix=np.zeros((5,5),dtype=int)
for i in range(5):
    row=input().split()
    matrix[i]=row
row,col=np.where(matrix==1)
moves=abs(2-row[0])+abs(2-col[0])
print(moves)