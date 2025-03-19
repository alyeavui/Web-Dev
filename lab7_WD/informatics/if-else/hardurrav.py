a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == 0 and b == 0:
    if c == 0:
        print("INF")
    else:
        print("NO")
elif a == 0:
    print("NO")
else:
    x = -b / a
    if x == int(x) and c * int(x) + d != 0:
        print(int(x))
    else:
        print("NO")
