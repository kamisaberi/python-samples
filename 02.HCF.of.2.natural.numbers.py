a = 12
b = 11
# get minimum of a and b
if a > b:
    m = b
else:
    m = a
hcf = 1
for i in range(m, 0, -1):
    if a % i == 0 and b % i == 0:
        hcf = i
        break
print(hcf)
