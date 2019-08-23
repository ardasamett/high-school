## Liste şekilde verilen 2 tane matrix'in aynı elemanlarını toplar ve yazdırır.

matrix_1 = [[1,1,2,5],[0,2,1,4],[1,0,3,6]]  
matrix_2 = [[0,2,1,2],[1,1,2,3],[0,3,0,1]]
matrix_sum = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range(len(matrix_1)): # 3 line
    for j in range (len(matrix_2)+1): # 4 column
        matrix_sum[i][j] = matrix_1[i][j] + matrix_2[i][j]

print(matrix_sum)