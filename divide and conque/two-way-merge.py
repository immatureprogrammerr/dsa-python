def two_way_merge(a, b):
    c = []
    i = j = k = 0

    while(i < len(a) and j < len(b)):
        if a[i] < b[j]:
            c.append(a[i])
            k += 1
            i += 1
        else:
            c.append(b[j])
            k += 1
            j += 1
    if i < len(a):
        for _ in range(i, len(a)):
            c.append(a[i])
            k += 1
            i += 1
    if j < len(b):
        for _ in range(j, len(b)):
            c.append(b[j])
            k += 1
            j += 1
    return c

a = [2, 4, 6, 8, 10]
b = [1, 3, 5, 7]

print(two_way_merge(a, b))