import time 
import os

def read(filename):
    while os.path.exists(filename) == False:
        print(f"Error: The file '{filename}' does not exist.")
        filename = input("Enter the name of the poem:")
    else:
        with open(filename, 'r') as f:

            poem = f.read()
            for line in poem.split("\n"):
                if len(line) == 1:
                    tabs = "\t"
                else:
                    tabs = ""
                print(tabs + line)
                time.sleep(0.8)  

#
filename = input("Enter the name of the poem:")
read(filename)
