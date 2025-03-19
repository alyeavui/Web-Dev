N = int(input())
arr = list(map(int, input().split()))
K = int(input())

K = K % N  
if K > 0:
    arr[:] = arr[-K:] + arr[:-K] 
elif K < 0:
    arr[:] = arr[-K:] + arr[:-K]  

print(*arr)
