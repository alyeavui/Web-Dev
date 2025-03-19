def fast_power(a: float, n: int) -> float:
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * fast_power(a, n - 1)
    else:
        half = fast_power(a, n // 2)
        return half * half

if __name__ == "__main__":
    a, n = input().split()
    a, n = float(a), int(n)
    print(fast_power(a, n))
