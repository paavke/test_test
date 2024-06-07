def perfect_squares(start, end):
    result = []
    for i in range(start, end + 1):
        if (i ** 0.5) % 1 == 0:
            result.append(i)
    return result
