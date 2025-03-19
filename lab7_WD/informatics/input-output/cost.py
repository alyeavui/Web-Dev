a = int(input()) 
b = int(input()) 
n = int(input())  

total_kop = (a * 100 + b) * n  
rubles = total_kop // 100  
kopecks = total_kop % 100 

print(rubles, kopecks)
