def phi(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    n = int(input())
    print(phi(n))
