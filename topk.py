from quicksort import partition, quicksort


def topk(arr, k):
    quickselect(arr, 0, len(arr)-1, k)
    return arr[:k]


def quickselect(arr, low, high, k):
    if low < high:
        p = partition(arr, low, high)
        if p < k:
            quickselect(arr, p+1, high, k)
        elif p > k:
            quickselect(arr, low, p-1, k)

if __name__ == "__main__":
    import numpy as np
    for i in range(5):
        a = np.random.randint(0, 100, size= 10)
        print "origin:", a
        b = topk(a, 3)
        print "topk:", b


