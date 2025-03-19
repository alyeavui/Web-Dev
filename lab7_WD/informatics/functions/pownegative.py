def power(a: float, n: int) -> float:
    if n == 0:
        return 1
    if n > 0:
        return a * power(a, n - 1)
    return 1 / power(a, -n)

if __name__ == "__main__":
    a, n = input().split()
    a, n = float(a), int(n)
    print(power(a, n))
