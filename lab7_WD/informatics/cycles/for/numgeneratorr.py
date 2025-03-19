n = int(input())

sequence = []
num = 1

while len(sequence) < n:
    sequence.extend([num] * num)
    num += 1

print(*sequence[:n])
