bird=[
    [0,1],
    [1,1],
    [1,0],
    [1,2],
    [2,1]
]
board=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
hw=[
    [0,1,1,1,0],
    [0,1,0,0,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
]
for i in range(len(bird)):
    point=bird[i]
    x = point[0]
    y = point[1]
    board[x][y]=1
for i in board:
    for j in i:
        if j!=1:
            print(" ",end="")
        else:
            print(j,end="")
    print("\n")
