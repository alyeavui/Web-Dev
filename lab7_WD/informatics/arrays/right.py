N = int(input())
arr = list(map(int, input().split()))

last = arr[-1] 
for i in range(N - 1, 0, -1):
    arr[i] = arr[i - 1]  
arr[0] = last  

print(*arr)
