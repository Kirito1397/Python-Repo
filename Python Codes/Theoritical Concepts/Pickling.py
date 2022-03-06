
import pickle

# Python object
my_list = [11, 'Python', b'Love Python']

# Pickling
with open("data.pickle","wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)

print("Pickling completed!")

# This program creates data.pickle file in the current directory. Go and check for it :)