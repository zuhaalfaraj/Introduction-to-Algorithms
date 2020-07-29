def insertionSort(lst):
    for i in range(1,len(lst)):
        if lst[i] < lst[i-1]:

            for j in range(len(lst[:i])):
                if lst[len(lst[:i])-j] < lst[len(lst[:i])-j-1]:

                    temp = lst[len(lst[:i])-j-1]
                    lst[len(lst[:i])-j-1]= lst[len(lst[:i])-j]
                    lst[len(lst[:i])-j]= temp
                else:
                    break
    return lst



def mergeSort(arr):
    def merege(L,R):
        i = j = k = 0

        while i< len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k]= L[i]
                i+=1
            else:
                arr[k]= R[j]
                j+=1
            k+=1
        return arr

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        arr = merege(L,R)
    return arr

if __name__=='__main__':
    import time
    lst= [4,2,1,5,3,10,2,33,100,23,3,44,3,2323,12,45,23,55,234]
    #lst= np.asarray(lst)
    #lst = np.random.rand(700)
    #lst= list(lst)
    t1= time.time()
    y= insertionSort(lst)
    t2 = time.time()
    x= mergeSort(lst)
    t3 = time.time()

    tim1= t3-t2
    tim2= t2-t1
    print(x)
    print(tim1)
    print(tim2)
    print(tim1/tim2)



