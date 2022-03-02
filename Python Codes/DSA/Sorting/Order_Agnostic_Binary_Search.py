def OrderAgnosticBinarySearch(arr, target_element):
    start = 0
    end = len(arr)-1
    isAsc = bool(arr[start] < arr[end]) # Will check if the array is Sorted in Ascending or Descending order
    while(start <= end):
        mid = start + ((end-start)//2) # Use this form to avoid getting error, in case the numbers are extremely large 
        if (arr[mid] == target_element):
            return mid
        if isAsc:
            if (target_element < arr[mid]):
                end = mid -1
            else:
                start = mid + 1
        else:
            if (target_element > arr[mid]):
                end = mid -1
            else:
                start = mid + 1
    return -1

if __name__ == '__main__' :
    arr = [4,7,9,12,25,26,29,44,52,65,77,81]
    arr1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,]
    my_search = OrderAgnosticBinarySearch(arr1,1)
    print (my_search)