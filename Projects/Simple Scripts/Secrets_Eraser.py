import re
import tkinter as tk
from tkinter import filedialog

# Function to find and substitute the matches with desired string.
def secrets_eraser(text):
    return re.sub("((key*\w+\s\w+)|(secret\s\d+\s\w+)|(pass*\w+\s\w+))", '#########', text)

if __name__ == '__main__':

    # Removes the root tkinter window from the screen (without destroying it)
    root = tk.Tk()
    root.withdraw()

    # Define the FILE_PATH variable to get the Path/location of the file on Host.
    FILE_PATH = filedialog.askopenfilename(title='Select the file for Editing',
                                           initialdir="C:/Users/Kirito/Desktop/",
                                           filetypes=(("text files", "*.txt"),("all files", "*.*"),("log files", "*.log")))

    # Read the contents of the file, edit it and store it in a temp_file variable.
    with open(FILE_PATH, 'r') as file:
        temp_file = (secrets_eraser(file.read()))

    # Read the contents of temp_file and re-write it onto the original file.
    with open(FILE_PATH, 'w') as file:
        file.writelines(temp_file)
