import math

def is_prime(n: int) -> str:
    if n < 2:
        return "composite"
    if n in (2, 3):
        return "prime"
    if n % 2 == 0 or n % 3 == 0:
        return "composite"

    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return "composite"
    
    return "prime"

if __name__ == "__main__":
    n = int(input())
    print(is_prime(n))
