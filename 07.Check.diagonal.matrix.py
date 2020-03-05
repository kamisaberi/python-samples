# 1 0 2
# 0 5 0
# 0 0 0
m = [[1, 0, 2], [0, 5, 0], [0, 0, 0]]
# print(m[1][1])
is_diagonal = True
for i in range(3):
    for j in range(3):
        if i != j and m[i][j] != 0:
            is_diagonal = False

if is_diagonal:
    print("it is a diagonal matrix")
else:
    print("it is not a diagonal matrix")
