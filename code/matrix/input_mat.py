
row = int(input("Enter the number of rows : "))
col = int(input("Enter the number of columns : "))

mat = list(list())

for i in range(row):
    mat.append([])
    for j in range(col):
        val = int(input(f"Enter {i},{j} element : "))
        mat[i].append(val)
    

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end = ' ')
    
    print()