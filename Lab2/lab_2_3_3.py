def getmax(u, v):
    if u > v:
        return u
    return v

print("Beginning")

a = int(input("Enter a: ")) #2
b = int(input("Enter b: ")) #1
c = int(input("Enter c: ")) #3

# max1 = getmax(a, b)
# max2 = getmax(b, c)
# max3 = getmax(max1, max2)
# print(max3)

print(getmax(getmax(a, b), getmax(b, c)))

print("The end")
