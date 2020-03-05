# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

# 1(0,0)
# 1(1,0) 1(1,1)
# 1(2,0) 2(2,1) 1(2,2)
# 1(3,0) 3(3,1) 3(3,2) 1(3,3)
# 1(4,0) 4(4,1) 6(4,2) 4(4,3) 1(4,4)
# 1(5,0) 5(5,1) 10(5,2) 10(5,3) 5(5,4) 1(5,5)


def do_fact(a):
    s = 1
    for i in range(1, a + 1):
        s *= i
    return s


rows = 6

for n in range(rows):
    for r in range(n + 1):
        k = do_fact(n) // (do_fact(r) * do_fact(n - r))
        print(k, end= " ")
    print()