def count_frequency(arr):
    hash_map = dict()
    for i in arr:
        if i not in list(hash_map.keys()):
            # Check if element already present in list of Dictionary Keys or not
            hash_map.update({i:1})
            # Add Key in dictionary and set its Value as 1
        else:
            hash_map[i] = (hash_map.get(i)+1)
            #  Fetch the current value of Key and increment by 1
    return hash_map


if __name__ == "__main__":
    arr = [15,20,10,20,20,200,15,40]
    res = count_frequency(arr)
    print(res)


# Test:
# -----
# arr = [15,20,10,20,20,200,15,40]
