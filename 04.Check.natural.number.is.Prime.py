# a = 7 --> (1 ,7) --> is Prime
# a = 9 --> (1 ,3 ,9) --> is not Prime
a = 9
is_prime = True
for i in range(2, a):
    if a % i == 0:
        is_prime = False
        break

if is_prime:
    print(str(a) + " is prime number")
else:
    print(str(a) + " is not prime number")
