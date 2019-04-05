def make_bricks(small, big, goal):
    if goal >= 5 * big:
        remainder = goal - (5 * big)
    else:
        remainder = goal % 5

    return small >= remainder