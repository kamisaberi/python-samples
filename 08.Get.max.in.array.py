a = [1, 5, 8, 9, 14, 2, 3, 5, 8]
mx = a[0]
for i in a:
    if i > mx:
        mx = i
mn = a[0]
for i in a:
    if i < mn:
        mn = i

print(mx)
print(mn)
