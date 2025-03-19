from math import gcd

A, B, N = map(int, input().split())

def solve(a, b):
    x, y = 0, 0 
    steps = []

    while x != N and y != N:
        if x == 0:
            x = a
            steps.append(">A")
        elif y == b:
            y = 0
            steps.append("B>")
        else:
            pour = min(x, b - y)
            x -= pour
            y += pour
            steps.append("A>B")
        
        if x == N or y == N:
            return steps

    return steps

if N > max(A, B) or N % gcd(A, B) != 0:
    print("Impossible")
else:
    steps1 = solve(A, B)
    steps2 = solve(B, A)
    
    result = min(steps1, steps2, key=len)
    print("\n".join(result))
