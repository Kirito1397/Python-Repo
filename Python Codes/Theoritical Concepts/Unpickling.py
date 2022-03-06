# Unpickling in Python

import pickle

# Unpickling (Byte stream will be retrived from data.pickle file)
with open("data.pickle","rb") as file_handle:
    retrieved_data = pickle.load(file_handle)
    print(retrieved_data)