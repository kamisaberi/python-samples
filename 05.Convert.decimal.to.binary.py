# a = 13 ---> 1101
a = 13
s = 0
d = 1
while a > 0:
    k = a % 2
    a //= 2
    s = k * d + s
    d *= 10

print(s)
