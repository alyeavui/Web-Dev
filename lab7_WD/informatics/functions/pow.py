def power(a: float, n: int) -> float:
    return a ** n 

if __name__ == "__main__":
    a, n = input().split()
    a, n = float(a), int(n)
    print(power(a, n))
