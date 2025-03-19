N = int(input())
heights = list(map(int, input().split()))
petya_height = int(input())

position = N + 1 
for i in range(N):
    if heights[i] < petya_height:
        position = i + 1
        break

print(position)
