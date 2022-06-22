def insertion_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        for j in range(i, 0, -1):
        	if a[j-1] > x:
        		a[j] = a[j-1]
        		a[j-1] = x
    return a