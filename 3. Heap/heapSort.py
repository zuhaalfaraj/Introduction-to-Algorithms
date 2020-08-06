import numpy as np


def max_heapify(arr,n,i):
    node = i
    left = 2*i+1
    right = 2*i+2
    larg= node
    if left<n and arr[left]> arr[node]:
        larg= left
    if right<n and arr[right]> arr[larg]:
        larg = right

    if larg != i:
        arr[i], arr[larg] = arr[larg], arr[i]
        max_heapify(arr, n, larg)


def max_heap(arr):
    n = len(arr)
    half= int(np.floor(n/2))
    while half>=0:
        max_heapify(arr, n, half)
        half-=1

    for i in range(n-1,0,-1):
        arr[i], arr[0]= arr[0], arr[i]
        max_heapify(arr, i, 0)


    return arr



if __name__=='__main__':
    import time
    arr= [4,1,3,2,16,9,10,14,8,7]
    lst = [4, 2, 1, 5, 3, 10, 2, 33, 100, 23, 3, 44, 3, 2323, 12, 45, 23, 55, 234]
    lst = np.random.rand(700)
    lst= list(lst)

    t1= time.time()
    c= max_heap(lst)
    t2 = time.time()

    print(t2-t1)

