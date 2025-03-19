k = int(input())

for x in range(k // 3 + 1):
    if (k - 3 * x) % 5 == 0:
        print("YES")
        break
else:
    print("NO")
