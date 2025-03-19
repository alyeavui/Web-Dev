M, N = map(int, input().split())
x, y = map(int, input().split())

neighbors = []
if y > 1:
    neighbors.append((x, y - 1))  
if y < N:
    neighbors.append((x, y + 1)) 
if x > 1:
    neighbors.append((x - 1, y))  
if x < M:
    neighbors.append((x + 1, y))  

for neighbor in neighbors:
    print(*neighbor)
