n = int(input())

b60 = n // 60
n %= 60

b10 = n // 10
n %= 10

b1 = n

if b1 * 15 > 125:
    b10 += 1
    b1 = 0

if b10 * 125 + b1 * 15 > 440:
    b60 += 1
    b10 = 0
    b1 = 0

print(b1, b10, b60)
