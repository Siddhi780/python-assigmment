filename = input("Input the Filename: ")
fileExtList = {"py": "python", "java": "Java"}
file_arr = filename.split(".")
print("The extension of the file is : " + fileExtList[file_arr[-1]])
