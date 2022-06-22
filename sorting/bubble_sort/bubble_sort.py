
def bubble_sort(a):
    swapped = False;
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            x = a[j]

            if x > a[j+1]:
                a[j] = a[j+1]
                a[j+1] = x
                swapped = True
        if swapped == False:
            break
    return a
