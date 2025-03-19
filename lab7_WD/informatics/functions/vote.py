def election(x: int, y: int, z: int) -> int:
    return 1 if (x + y + z) >= 2 else 0

if __name__ == "__main__":
    x, y, z = map(int, input().split())
    print(election(x, y, z))
