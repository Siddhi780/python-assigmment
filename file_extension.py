filename = input("Input the Filename: ")
file_arr = filename.split(".")
file_extension = ''
if(file_arr[-1] == 'py'):  # checking the file extension
    file_extension = 'python'
else:
    file_extension = file_arr[-1]
print("The extension of the file is : " + repr(file_extension))
