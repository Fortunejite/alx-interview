def pascal_triangle(n):
    result = []
    prev = []
    if n <= 0:
        return []
    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        elif i == 1:
            result.append([1, 1])
            prev = [1, 1]
            continue
        current = []
        for j in range(len(prev)):
            if j == 0:
                current.append(1)
                continue
            current.append(prev[j]+prev[j-1])
        current.append(1)
        result.append(current)
        prev = current.copy()
    return result