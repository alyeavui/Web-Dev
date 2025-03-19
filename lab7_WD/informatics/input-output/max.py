a = int(input())
b = int(input())

print(a * ((a // b) + 1) % (b + 1) + b * ((b // a) + 1) % (a + 1))
