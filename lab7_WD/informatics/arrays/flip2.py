N, A, B, C, D = map(int, input().split())

arr = list(range(1, N + 1))  
arr[A-1:B] = arr[A-1:B][::-1] 
arr[C-1:D] = arr[C-1:D][::-1]  

print(*arr)
