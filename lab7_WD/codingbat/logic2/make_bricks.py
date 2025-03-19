def make_bricks(small, big, goal):
    return goal - min(goal // 5, big) * 5 <= small

print(make_bricks(3, 1, 8))  