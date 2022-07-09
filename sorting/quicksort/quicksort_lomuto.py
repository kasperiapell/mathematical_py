// Quicksort algorithm using Lomuto partitioning scheme

def swap(array, i, j):
    x = array[i]
    array[i] = array[j]
    array[j] = x

def partition(array, m, M):
    pivot = array[M]
    i = m - 1

    for j in range(m, M):
        if (array[j] <= pivot):
            i = i + 1
            swap(array, i, j)

    swap(array, i + 1, M)
    return i + 1

def quicksort(array, m, M):
    if (m < M):
        p = partition(array, m, M)
        quicksort(array, m, p - 1)
        quicksort(array, p + 1, M)
    return array