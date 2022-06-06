x = input("Write your First and Last name ")
for i in range(0,len(x)):
    y = x[i:i+1]
    if y == " ":
        Split = i
        break
z = x[i:len(x)]
a = x[0:i]
for s in range(0,len(z)):
    g = z[s:s+1]
    print(g)
print(" ")
for d in range(0,len(a)):
    f = a[d:d+1]
    print(f)