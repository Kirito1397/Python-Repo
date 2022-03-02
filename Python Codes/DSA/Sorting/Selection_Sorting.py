def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range((i+1), len(arr)):
            if (arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    list1 = [2, 4, 1, 78, 45, 1]
    s_sort = selection_sort(list1)
    print(s_sort)
