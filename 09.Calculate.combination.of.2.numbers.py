# (n,r) = n!/(r!(n-r!))
# (5,2) = 5!/ (2!((5-2)!))= 10

def do_fact(a):
    s = 1
    for i in range(1, a + 1):
        s *= i
    return s


n = 5
r = 2
x = do_fact(n) / (do_fact(r) * do_fact(n - r))
print(int(x))
