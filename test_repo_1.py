print("Hello world")

#Now I will try something slightly more complicated. 

x = [1, 1]
for i in range(2, 10):
    x.append(x[i-1]+ x[i-2])
    print(x[-1])

print(x)