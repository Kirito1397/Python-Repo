# Unpickling in Python

import pickle

# Pickling
with open("data.pickle","rb") as file_handle:
    retrieved_data = pickle.load(file_handle)
    print(retrieved_data)