arr = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]

'''
Current Input:
11 12 13 14
15 16 17 18
19 20 21 22
23 24 25 26
'''

'''
Output Required:
11 15 19 23
24 20 16 12
13 17 21 25
26 22 18 14

This is wave traversal
'''
for j in range(len(arr)):
    #need to increase row constraint when going down and that too on every alternative iteration

    if j % 2 == 0:
        for i in range(len(arr[0])):
            print(arr[i][j], end=" ") #colums is 0th so we used the outer loop to access the column
    else:
        for i in range(len(arr[0])-1,-1,-1):
            print(arr[i][j], end =" ") #going up on every odd iteration rows get decreased
    
    print()
