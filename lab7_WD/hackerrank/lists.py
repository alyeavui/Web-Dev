if __name__ == '__main__':
    N = int(input())  
    my_list = [input().split() for _ in range(N)]  
    
    g = []
    for command in my_list:
        if not command: 
            continue

        if command[0] == 'insert' and len(command) == 3:
            g.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(g)
        elif command[0] == 'remove' and len(command) == 2:
            g.remove(int(command[1]))
        elif command[0] == 'append' and len(command) == 2:
            g.append(int(command[1]))
        elif command[0] == 'pop':
            if g:
                g.pop()
        elif command[0] == 'sort':
            g.sort()
        elif command[0] == 'reverse':
            g.reverse()
