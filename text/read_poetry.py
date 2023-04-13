import time 
import os

def read(filename):
    #function to read the poetry
    #also checks if the file exists in the directory
    #if not, it asks for a new file name
    #if the file exists, it reads the file and prints it out
    #with a delay of 0.8 seconds between each line
    #the delay is used to make the poem more readable
    #
    while os.path.exists(filename) == False:
        print(f"Error: The file '{filename}' does not exist.")
        filename = input("Enter the name of the poem:")
    else:
        with open(filename, encoding ='utf-8-sig') as f:
            ind = 0
            poem = f.read()
            for line in poem.split("\n"):
                if len(line.split()) == 1:
                    tabs = "\t"
                    print(tabs*ind + line)
                    time.sleep(0.8)  
                    ind+=1
                else:
                    ind = 0
                    tabs = ""
                    print(tabs + line )
                    time.sleep(0.8)

#
filename = input("Enter the name of the poem:")
read(filename)
