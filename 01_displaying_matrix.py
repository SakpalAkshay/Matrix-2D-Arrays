#program to display matrix elements


arr = [[1,2,3,], [9,87,6,23], [0,1], [1,2,3,4,5,6,7]]


#using for loop 
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()


