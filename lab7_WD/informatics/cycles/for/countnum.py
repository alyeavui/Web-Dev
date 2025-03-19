N = int(input())
zero_count = positive_count = negative_count = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        zero_count += 1
    elif num > 0:
        positive_count += 1
    else:
        negative_count += 1

print(zero_count, positive_count, negative_count)
