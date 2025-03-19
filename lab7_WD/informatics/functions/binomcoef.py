def binomial_coefficient(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(binomial_coefficient(n, k))
