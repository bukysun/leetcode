from heap_sort import heapify

def topk(arr, k):
    n = len(arr)
    # create max heap for the first k elements
    for i in range(k-1, -1, -1):
        heapify(arr[:k], k, i)

    # insert the last n-k elements to max heap
    for i in range(k, n):
        if a[i] < a[0]:
            a[i], a[0] = a[0], a[i]
            heapify(arr[:k], k, 0)
    return arr[:k]


if __name__ == "__main__":
    import numpy as np
    for i in range(5):
        a = np.random.randint(0, 100, size= 10)
        print "origin:", a
        b = topk(a, 3)
        print "topk:", b


