n = int(input())

if 11 <= n % 100 <= 14:
    print(n, "korov")
elif n % 10 == 1:
    print(n, "korova")
elif n % 10 in [2, 3, 4]:
    print(n, "korovy")
else:
    print(n, "korov")
