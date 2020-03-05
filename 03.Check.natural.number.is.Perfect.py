# 6 = 1,2,3 --> 1+2+3 = 6
# 6 is perfect
# 9 = 1,3 --> 1+3 = 4
# 9 is not perfect
s = 0
a = 28
for i in range(1, a):
    if a % i == 0:
        s += i

if a == s:
    print("yes")
else:
    print("no")
