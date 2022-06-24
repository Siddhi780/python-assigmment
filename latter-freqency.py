s = input("Enter the string: ")

d = {}

for i in s:
    if i not in d:
        d[i] = 1 
    else:
        d[i] += 1
#make it list
list = d.items()
cd = sorted(list,key=lambda x: x[1],reverse=True)
for x in cd:
  print(str(x[0])+" = "+str(x[1]))