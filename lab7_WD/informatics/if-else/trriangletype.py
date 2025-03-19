a, b, c = sorted(map(int, input().split()))

if a + b <= c:
    print("impossible")
elif a**2 + b**2 == c**2:
    print("right")
elif a**2 + b**2 > c**2:
    print("acute")
else:
    print("obtuse")
