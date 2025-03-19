def xor(x: int, y: int) -> int:
    return x ^ y 

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(xor(x, y))
