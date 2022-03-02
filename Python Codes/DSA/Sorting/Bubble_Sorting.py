def bubblesort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

if __name__ == '__main__':
    list1 = [2,4,1,78,45,1]
    bsort = bubblesort(list1)
    print(bsort)