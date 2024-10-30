b = [[1,2,3], [4,5,6], [7,8,9]]
c = [[1,1,1], [2,2,2], [3,3,3]]
d = [[0,0,0], [0,0,0], [0,0,0]]
#addition 
for i in range(len(b)):
    for j in range(len(b[i])):
        d[i][j]= b[i][j] + c[i][j]

#using for loop 
for i in range(len(b)):
    for j in range(len(b[i])):
        print(d[i][j], end=" ")
    print()

#subtraction
for i in range(len(b)):
    for j in range(len(b[i])):
        d[i][j]= b[i][j] - c[i][j]

#using for loop 
for i in range(len(b)):
    for j in range(len(b[i])):
        print(d[i][j], end=" ")
    print()
