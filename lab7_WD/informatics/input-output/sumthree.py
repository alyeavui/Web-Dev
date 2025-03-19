n = int(input())

sum_digits = (n // 100) + ((n // 10) % 10) + (n % 10) 
print(sum_digits)
