def bubblesort(arr):
    n = len(arr)
    for i in range(1,n):
        j = (i-1)
        key = arr[i]
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr


if __name__ == '__main__':
    list1 = [2,4,1,78,45,12]
    isort = bubblesort(list1)
    print(isort)