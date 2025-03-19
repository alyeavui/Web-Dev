A = int(input())

a, b = 0, 1
n = 1 

while b < A:
    a, b = b, a + b
    n += 1

print(n if b == A else -1)
