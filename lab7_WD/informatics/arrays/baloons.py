N, *balls = map(int, input().split())

def count_destroyed(balls):
    i = 0
    while i < len(balls) - 2:
        j = i
        while j < len(balls) and balls[j] == balls[i]:  
            j += 1
        if j - i >= 3:  
            return j - i  
        i = j
    return 0  

print(count_destroyed(balls))
