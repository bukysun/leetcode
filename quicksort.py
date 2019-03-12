

def partition(arr, low, high, reverse = False):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if not reverse:
            if arr[j] < arr[high]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        else:
            if arr[j] > arr[high]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high, reverse = False):
    if low < high:
        p = partition(arr, low, high, reverse=reverse)
        quicksort(arr, low, p-1, reverse=reverse)
        quicksort(arr, p+1, high, reverse=reverse)


if __name__ == "__main__":
    import numpy as np
    for i in range(5):
        a = np.random.randint(0, 100, size= 10)
        print "origin:", a
        quicksort(a, 0, len(a)-1, reverse=True)
        print "sorted:", a

