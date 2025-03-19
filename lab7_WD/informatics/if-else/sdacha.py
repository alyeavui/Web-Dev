a = int(input())
b = int(input())
c = int(input())
d = int(input())

cost = a * 100 + b
paid = c * 100 + d
change = paid - cost

print(change // 100, change % 100)
