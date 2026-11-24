def find_near(data, target, eps):
    for i, value in enumerate(data):
        if abs(value - target) <= eps:
            return i
    return -1
