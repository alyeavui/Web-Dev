x = int(input())
y = int(input())
z = int(input())
n = int(input())
output=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k==n:
                continue
            else:
                output.append([i,j,k])
    
print(output)
