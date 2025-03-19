import math

k = int(input())  
m = int(input()) 
n = int(input()) 

batches = math.ceil(n / k)
time_needed = batches * 2 * m

print(time_needed)
