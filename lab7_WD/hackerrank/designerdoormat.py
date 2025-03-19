N, M = input().split()
a = '|'
b = '.'
N = int(N)
M = int(M)
c = N // 2 - 1
for i in range(N):
    if i == N // 2:
        print('WELCOME'.center(M, '-'))
    else:
        if i < N / 2:    
            print(((b + a + b) * (2 * i + 1)).center(M, '-'))
        else:
            print(((b + a + b) * (2 * c + 1)).center(M, '-'))
            c = c - 1