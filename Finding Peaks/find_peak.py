import numpy as np
from math import ceil

def findPeak_1d_sf(lst):
    max = 0
    for i in range(1,len(lst)-1):
        if i == len(lst)-2:
            if lst[i+1] > max:
                max= lst[i+1]
        elif lst[i-1] < lst[i] and lst[i+1] < lst[i]:
            if lst[i] > max:
                max= lst[i]
    return max


def findPeak_1d_optimized(lst, low, high):
    n= len(lst)
    middle = low + (high - low) / 2
    middle = int(middle)
    if (middle==0 or lst[middle]>= lst[middle-1]) and\
            (middle==n-1 or lst[middle]>= lst[middle+1]):

        return lst[middle]

    if (middle > 0 and (lst[middle] <= lst[middle -1] and lst[middle -1] >= lst[middle +1])) :
        return findPeak_1d_optimized(lst, low, middle-1)

    elif (middle > 0 and (lst[middle] <= lst[middle +1] and lst[middle +1] >= lst[middle -1])) :
        return findPeak_1d_optimized(lst,middle+1,high)



def findPeak_2d_optimized(arr,mid):
    row, col = arr.shape[0], arr.shape[1]
    max =0
    for i in range(row):
        if arr[i][mid] > max:
            max = arr[i][mid]
            max_indx=i
    if (mid == 0 or mid == columns - 1):
        return max

    if (arr[max_indx][mid-1]< arr[max_indx][mid] and arr[max_indx][mid+1]< arr[max_indx][mid]):
        return max

    if (max < arr[max_indx][mid - 1]):
        return findPeak_2d_optimized(arr, mid - ceil(mid / 2.0))

    if (max < arr[max_indx][mid + 1]):
        return findPeak_2d_optimized(arr, mid + ceil(mid / 2.0))




if __name__ == '__main__':
    import time
    arr = np.array([[50, 8, 10, 10],
           [14, 13, 12, 11],
           [15, 9, 11, 21],
           [16, 17, 19, 20]])
    #arr= np.array([[10,20,15], [21,30,14],[7,16,32]])

    # Number of Columns
    rows = 4
    columns = 4
    mid= arr.shape[1]//2
    print(findPeak_2d_optimized(arr,mid))
    #print(findPeak(arr, rows, columns))
"""
    l= [1,2,4,1,20,1,40,3,1,100,4]
    l=[1, 3, 20, 4, 1, 0]
    t1 = time.time()
    x= findPeak_1d_sf(l)
    t2= time.time()
    y= findPeak_1d_optimized(l, 0, len(l)-1)
    #y= findPeak(l, len(l))
    t3= time.time()

    print(y)
    opt= t3 - t2
    fst= t2-t1
    print(opt)
    print(fst)
    print(fst-opt)
    """