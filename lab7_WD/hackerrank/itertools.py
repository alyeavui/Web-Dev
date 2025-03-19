from itertools import product
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
print(" ".join(map(str,product(a,b))))