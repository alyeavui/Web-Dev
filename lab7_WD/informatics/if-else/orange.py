n = int(input())

if 11 <= n % 100 <= 14:
    print(n, "bochek")
elif n % 10 == 1:
    print(n, "bochka")
elif n % 10 in [2, 3, 4]:
    print(n, "bochki")
else:
    print(n, "bochek")
