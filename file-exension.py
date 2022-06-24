# Python Program to find Extension of the filename
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + f_extns[len(f_extns) - 1])