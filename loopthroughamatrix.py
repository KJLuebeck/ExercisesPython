# Exercise 25 - Loop through a matrix
#Write a program that uses nested loops to tackle the tasks below:
#Search for the coordinates of maximal value of the matrix

matrix = [[1,2,3],[1,2,3],[1,2,3]]

max_i = 0
max_j = 0
max_wert = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if max_wert < matrix[i][j]:
            max_wert = matrix[i][j]
            max_i = i
            max_j = j
print (max_i, max_j, max_wert)
#sum up all entries of the matrix
summe = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        summe = summe + matrix[i][j]
print (f"Die Summe ist {summe}.")
#Describe the multiplication of the components of two matrices in a third resulting matrix
result = 0
matrix2 = [[2,6,7],[4,6,3],[8,2,3]]
matrix3 =[[],[],[]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
            a = matrix[i][j]
            b = matrix2[i][j]
            result = a*b
            matrix3[i].append(result)
print (matrix3)
#anderer Ansatz für 3#
matrix4 = []
for i in range(len(matrix)):
    matrix4.append([])
    for j in range(len(matrix[i])):
            a = matrix[i][j]
            b = matrix2[i][j]
            result = a*b
            matrix4[i].append(result)
print (matrix4)

#anderer Ansatz für 3#
matrix5 =[[1,2,3],[4,6,3],[8,2,3]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
            a = matrix[i][j]
            b = matrix2[i][j]
            result = a*b
            matrix5[i][j] = result
print (matrix5)
