def binarysearch(x, arr):

    # Define 'low' and 'high' values.
    low = 0
    high = (len(arr)-1)

    # Loop is run until 'low' is smaller than or equal to 'high'
    while(low <= high):

        # Define 'mid' value for each iteration
        mid = (low+high)//2

        if (x == arr[mid]):
            return mid
        
        # If x is smaller than middle element then ignore the
        # right-half section of list and update value of 'high'.
        elif (x < arr[mid]):
            high = mid - 1

        # If x is greater than middle element then ignore the 
        # left-hand section of list and update value of 'low'.
        elif (x > arr[mid]):
            low = mid + 1
    
    # If x(element) not found in list, then return -1.
    return -1

if __name__ == "__main__":

    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(binarysearch(70, arr))
