def heapify(arr, n, i):  # max heap
    largest = i
    l = 2 * i + 1    # left child
    r = 2 * i + 2    # right child
    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    #create max heap
    for i in range(n-1, -1, -1):
        heapify(arr, n, i)

    # heap sort 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


if __name__ == "__main__":
    import numpy as np
    for i in range(5):
        a = np.random.randint(0, 100, size= 10)
        print "origin:", a
        heapsort(a)
        print "sorted:", a

        
