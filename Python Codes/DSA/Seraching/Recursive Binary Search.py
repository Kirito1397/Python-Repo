def binarysearch(x, arr, low, high):

    mid = (low+high)//2

    # Base case, when we cannot find the elemendt in list
    if low > high:
        return -1

    # If element is present at the middle itself
    if x == arr[mid]:
        return mid

    # If element is smaller than mid, then it can only
	# be present in left subarray
    elif (x < arr[mid]):
        return binarysearch(x, arr, low, mid-1)

    # Else the element can only be present in right subarray
    elif (x > arr[mid]):
        return binarysearch(x, arr, mid+1, high)


if __name__ == "__main__":

    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(binarysearch(70, arr, 0, (len(arr)-1)))
