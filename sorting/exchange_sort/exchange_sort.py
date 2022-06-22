def exchange_sort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            x = a[i]

            if x > a[j]:
                a[i] = a[j]
                a[j] = x
    return a