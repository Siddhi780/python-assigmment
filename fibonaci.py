r = int(input(' enter the number where you want to print the fibonaci series: '))
def fibonacci(n):
     
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
     
     
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

for i in range(0, r):
    print(fibonacci(i))
