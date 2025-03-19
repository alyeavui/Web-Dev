N = int(input())
found_zero = False

for _ in range(N):
    if int(input()) == 0:
        found_zero = True

print("YES" if found_zero else "NO")
