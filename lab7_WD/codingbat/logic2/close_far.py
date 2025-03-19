def close_far(a, b, c):
    close = lambda x, y: abs(x - y) <= 1
    far = lambda x, y: abs(x - y) >= 2

    return (close(a, b) and far(b, c) and far(a, c)) or (close(a, c) and far(a, b) and far(b, c))

print(close_far(1, 2, 10))