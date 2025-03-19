A = int(input())
B = int(input())

commands = []
while A > B:
    if A % 2 == 0 and A // 2 >= B:
        A //= 2
        commands.append(":2")
    else:
        A -= 1
        commands.append("-1")

for command in commands:
    print(command)
